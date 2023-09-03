def main(spark):
    df = spark.read.csv("path_to_your_file.csv", header=True, inferSchema=True)
    display(df)