from pyspark.sql import SparkSession
import pyspark.sql.functions as f

spark = SparkSession.builder.appName("MovieExtraction").getOrCreate()

raw_df = spark.read.json("path")

flatten_df = raw_df.select(f.col("title"),
                           f.col("year"),
                           f.col("href"),
                           f.col("extract"),
                           f.col("thumbnail"),
                           f.col("thumbnail_width"),
                           f.col("thumbnail_height"),
                           f.explode(f.col("cast")).alias("cast"),
                           f.explode(f.col("genres")).alias("genres"),
                           )
flatten_df.write.format("delta").partitionBy("year").mode("overwrite").save("path_to_delta_lake")

