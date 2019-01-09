import re
import sys
from pyspark import SparkConf, SparkContext

conf = SparkConf()
sc = SparkContext(conf=conf)

lines = sc.textFile(TEXT_FILE)
# 1. MAP: Convert each line into array of words
words = lines.flatMap(lambda i: re.split(r'[^\w]+', i))
# Create a key-value pair as a tuple
pairs = words.map(lambda w: (w, 1))

# 2. REDUCE
counts = pairs.reduceByKey(lambda x, y: x + y)

# Export Result
counts.saveAsTextFile('output')
sc.stop()
