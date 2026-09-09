from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("CSV_to_Delta_Pipeline").getOrCreate()

# Read CSV file
df = spark.read.option("header", True).option("inferSchema", True).csv(
    "orders.csv"
)

# Data transformation
df = df.withColumn(
    "total_amount",
    col("quantity") * col("price")
)

# Display transformed data
df.show()

# Write data as Delta
df.write.format("delta").mode("overwrite").save(
    "delta/orders"
)

print("CSV to Delta pipeline completed successfully!")
