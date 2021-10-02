from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, LongType,  \
    IntegerType, ArrayType
from pyspark.sql.functions import col, explode, expr, from_json

from lib.logger import Log4j

if __name__ == "__main__":
    # Get spark Session
    spark = SparkSession \
        .builder \
        .appName("Kafka with Spark Streaming") \
        .master("local[1]") \
        .config("spark.streaming.stopGracefullyOnShutdown", "True") \
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
        .select(value_df["value"].getItem("InvoiceNumber")
                , value_df["value"].getItem("CreatedTime")
                , value_df["value"].getItem("StoreID")
                , value_df["value"].getItem("PosID")
                , value_df["value"].getItem("CustomerType")
                , value_df["value"].getItem("PaymentMethod")
                , value_df["value"].getItem("DeliveryType")
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

    invoice_writer_query = exploded_flattened_df.writeStream \
        .format("json") \
        .option("path", "output") \
        .outputMode("append") \
        .option("checkpointLocation", "chk-point-dir") \
        .trigger(processingTime="1 minute") \
        .start()

    invoice_writer_query.awaitTermination()
