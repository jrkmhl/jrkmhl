from pyspark.sql import SparkSession
import pyspark.sql.functions as f


def load_source(spark_session, source_file_path):
    # spark = spark_session.builder.appName("MovieExtraction").getOrCreate()

    raw_df = spark_session.read.json("path")
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


def load_dimension(source_df, columns, table_name, spark_session):
    # create table
    attributes = ",".join([name + " " + dtype for name, dtype in columns])
    spark_session.sql(f"""
    create table if not exist {table_name}_dim(
    attributes
    )
    """)
