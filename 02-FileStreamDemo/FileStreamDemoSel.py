from pyspark.sql import SparkSession
from pyspark.sql.functions import *

from lib.logger import Log4j

if __name__ == "__main__":
    # Set up spark object
    spark = SparkSession \
        .builder \
        .master("local[1]") \
        .appName("File Stream Demo") \
        .config("spark.sql.streaming.schemaInference", "True") \
        .config("spark.streaming.stopGracefullyOnShutdown", "True") \
        .getOrCreate()

    logger = Log4j(spark)

    # read the raw file in stream
    raw_df = spark.readStream \
        .format("json") \
        .option("path", "input") \
        .option("maxFilesPerTrigger", 1) \
        .option("cleanSource", "archive") \
        .option("sourceArchiveDir", "archive-processed-file") \
        .load()

    # check schema
    # raw_df.printSchema()

    # Create DF with required columns
    explode_flattened_df = raw_df \
        .withColumn("LineItemExplode", explode(col("InvoiceLineItems"))) \
        .select(raw_df["InvoiceNumber"]
                , raw_df["CreatedTime"]
                , raw_df["StoreID"]
                , raw_df["PosID"]
                , raw_df["CustomerType"]
                , raw_df["PaymentMethod"]
                , raw_df["DeliveryType"]
                , raw_df["DeliveryAddress"].getItem("AddressLine").alias("AddressLine")
                , raw_df["DeliveryAddress"].getItem("City").alias("City")
                , raw_df["DeliveryAddress"].getItem("ContactNumber").alias("ContactNumber")
                , raw_df["DeliveryAddress"].getItem("PinCode").alias("PinCode")
                , raw_df["DeliveryAddress"].getItem("State").alias("State")
                , col("LineItemExplode").getItem("ItemCode").alias("ItemCode")
                , col("LineItemExplode").getItem("ItemDescription").alias("ItemDescription")
                , col("LineItemExplode").getItem("ItemPrice").alias("ItemPrice")
                , col("LineItemExplode").getItem("ItemQty").alias("ItemQty")
                , col("LineItemExplode").getItem("TotalValue").alias("TotalValue")
                )

    # explode_flattened_df.printSchema()

    invoiceWriteQuery = explode_flattened_df.writeStream \
        .format("json") \
        .queryName("Flattened Invoice Writer") \
        .outputMode("append") \
        .option("path", "output") \
        .option("checkpointLocation", "chk-point-dir") \
        .trigger(processingTime="1 minute") \
        .start()

    invoiceWriteQuery.awaitTermination()
    logger.info("Started....")