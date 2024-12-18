import pandas as pd
import numpy as np
# import pyspark
# from collections import Counters
import matplotlib.pyplot as plt

from pyspark.sql import SparkSession


#data = pd.read_csv('the-reddit-climate-change-dataset-comments.csv')
#data = data.dropna() # drop any rows with missing values

# counter = Counter(data['subreddit.nsfw'])
# print(counter)

# print(data['score'])
#print(data['body'].iloc[20340])


# initialize spark session
spark = SparkSession.builder \
    .appName("Reddit Climate Change Comments") \
    .config("spark.driver.memory", "4g") \
    .config("spark.executor.memory", "8g") \
    .config("spark.sql.shuffle.partitions", "100") \
    .getOrCreate()

df = spark.read.csv("the-reddit-climate-change-dataset-comments.csv", header=True, inferSchema=True)
df = df.repartition(100)  # increase the number of partitions for large datasets
df.show()

df_original = df # save original dataset

# -- clean dataset ---
#remove null values first
df = df.dropna()

#create spark db
spark.sql("CREATE DATABASE reddit_db")

#create table with comments
spark.sql("USE reddit_db")
df.write.mode("overwrite").saveAsTable("reddit_db.comments")

spark.sql("SHOW TABLES").show()

col_names = df.columns
print(col_names)

filtered_db = spark.sql("SELECT id, body, score FROM comments LIMIT 5")
filtered_db.show()

print(filtered_db)