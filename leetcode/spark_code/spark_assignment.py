from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count

lst = [2, 5, 3, 4, 5, 7, 2, 2, 2, 2, 2, 11, 7, 9, 2, 3]

spark_session = SparkSession.builder.getOrCreate()
number_df = spark_session.sparkContext.parallelize(lst).toDF(["number"])

# finding duplicate number  using spark
agg_df = number_df.groupBy(col("number")).agg(count("*").alias("cnt"))
duplicate_df = agg_df.filter(agg_df.cnt > 1).select(col("number"))
duplicate_df.show()

# finding first index of duplicate
# spark is distributed so not confident on this solution

number_df.createTempView("NumberTable")
temp_df = spark_session.sql(""" select number ,position 
                                 from (select number,position,row_number() over(parition by number order by number) as rn
                                from 
                                  (select number,row_number() over() as position from NumberTable)ds1
                                )ds2 where rn=1
                            
                            """)
# showing only duplicates and  doing inner join with duplicate dataframe so will get only duplicate count
temp_df.join(duplicate_df, temp_df['number'] == duplicate_df['number']).show()
