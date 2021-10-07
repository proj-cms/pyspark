from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *

from lib.logger import Log4j

if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("Kafka read and sink to Kafka") \
        .master("local[1]") \
        .config("spark.streaming.stopGracefullyOnShutdown", "true") \
        .getOrCreate()

    logger = Log4j(spark)

    # As schema inference is not enabled for real time kafka streaming
    # create the schema
    stream_invoice_schema = StructType([
        StructField("InvoiceNumber", StringType())
        , StructField("CreatedTime", LongType())
        , StructField("StoreID", StringType())
        , StructField("PosID", StringType())
        , StructField("CashierID", StringType())
        , StructField("CustomerType", StringType())
        , StructField("CustomerCardNo", StringType())
        , StructField("TotalAmount", DoubleType())
        , StructField("NumberOfItems", IntegerType())
        , StructField("PaymentMethod", StringType())
        , StructField("CGST", DoubleType())
        , StructField("SGST", DoubleType())
        , StructField("CESS", DoubleType())
        , StructField("DeliveryType", StringType())
        , StructField("DeliveryAddress", StructType([
            StructField("AddressLine", StringType())
            , StructField("City", StringType())
            , StructField("State", StringType())
            , StructField("PinCode", StringType())
            , StructField("ContactNumber", StringType())
        ]))
        , StructField("InvoiceLineItems", ArrayType(StructType([
            StructField("ItemCode", StringType())
            , StructField("ItemDescription", StringType())
            , StructField("ItemPrice", DoubleType())
            , StructField("ItemQty", IntegerType())
            , StructField("TotalValue", DoubleType())
        ])))

    ])

    # once schema is set up
    # create the stream with kafka

    kafka_stream_df = spark.readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "localhost:9092") \
        .option("subscribe", "invoices") \
        .option("startingOffsets", "earliest") \
        .load()
    # print Kafka schema you will find its not readable it has value column with other kafak impo details
    # the column of importance is value column
    kafka_stream_df.printSchema()

    value_df = kafka_stream_df.select(from_json(col("value").cast("string"), stream_invoice_schema).alias("value"))

    value_df.printSchema()

    exploded_flattened_df = value_df \
        .withColumn("LineItemExplode", explode(value_df["value"].getItem("InvoiceLineItems"))) \
        .select(value_df["value"].getItem("InvoiceNumber").alias("InvoiceNumber")
                , value_df["value"].getItem("CreatedTime").alias("CreatedTime")
                , value_df["value"].getItem("StoreID").alias("StoreID")
                , value_df["value"].getItem("PosID").alias("CustomerType")
                , value_df["value"].getItem("CustomerType").alias("CustomerType")
                , value_df["value"].getItem("CustomerCardNo").alias("CustomerCardNo")
                , value_df["value"].getItem("TotalAmount").alias("TotalAmount")
                , value_df["value"].getItem("PaymentMethod").alias("PaymentMethod")
                , value_df["value"].getItem("DeliveryType").alias("DeliveryType")
                , value_df["value"].getItem("DeliveryAddress").getItem("AddressLine").alias("AddressLine")
                , value_df["value"].getItem("DeliveryAddress").getItem("City").alias("City")
                , value_df["value"].getItem("DeliveryAddress").getItem("ContactNumber").alias("ContactNumber")
                , value_df["value"].getItem("DeliveryAddress").getItem("PinCode").alias("PinCode")
                , value_df["value"].getItem("DeliveryAddress").getItem("State").alias("State")
                , col("LineItemExplode").getItem("ItemCode").alias("ItemCode")
                , col("LineItemExplode").getItem("ItemDescription").alias("ItemDescription")
                , col("LineItemExplode").getItem("ItemPrice").alias("ItemPrice")
                , col("LineItemExplode").getItem("ItemQty").alias("ItemQty")
                , col("LineItemExplode").getItem("TotalValue").alias("TotalValue")
                )

    exploded_flattened_df.printSchema()

    ##### Kafak stream for notification #####

    # Create the DF for notification
    notification_df = exploded_flattened_df \
        .select("InvoiceNumber"
                , "CustomerCardNo"
                , "TotalAmount") \
        .withColumn("EarnedLoyaltyPoints", expr("TotalAmount * 0.2"))

    notification_df.printSchema()

    # to write on to Kafka need to convert into  - KEY-value pair
    kafka_target_df = notification_df.selectExpr("InvoiceNumber as key",
                                                 """to_json(named_struct(
                                                 'CustomerCardNo', CustomerCardNo,
                                                 'TotalAmount', TotalAmount,
                                                 'EarnedLoyaltyPoints', TotalAmount * 0.2)) as value""")

    kafka_target_df.printSchema()

    kafka_target_df1 = notification_df \
        .withColumn("key", notification_df["InvoiceNumber"]) \
        .withColumn("value", to_json(struct("CustomerCardNo", "TotalAmount", "EarnedLoyaltyPoints"))) \
        .select("key", "value") \
        .dropDuplicates()

    kafka_target_df1.printSchema()

    notification_query_writer = kafka_target_df1 \
        .writeStream \
        .format("kafka") \
        .queryName("Notification Writer") \
        .option("kafka.bootstrap.servers", "localhost:9092") \
        .option("topic", "notifications") \
        .option("checkpointLocation", "chk-point-dir/notifications") \
        .outputMode("append") \
        .start()

    #### Req # 2  - write flattened record to file

    invoices_writer_query = exploded_flattened_df \
        .writeStream \
        .queryName("Falttened Invoice Writer") \
        .format("json") \
        .option("path", "output-invoices") \
        .option("checkpointLocation", "chk-point-dir/flattened-invoice") \
        .outputMode("append") \
        .start()

    #notification_query_writer.awaitTermination()

    ## Since there are 2 streams in this application those are writing the data out
    ## use spark.streams.awaitAnyTermination

    spark.streams.awaitAnyTermination()
