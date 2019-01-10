import re
import argparse
import sys
from pyspark import SparkConf, SparkContext


def parse_args():
    args = argparse.ArgumentParser("Count word occurences in a text file.\n")
    args.add_argument('text_file', type=str, help="Path to text file.")
    args.add_argument('output', type=str, help="Path to output directory.")
    return args.parse_args()


def run_wordcount_task(text_file, output_dir):
    """Launch a Spark Task to count number of occurences for each word in a
    text file

    Arguments:
    ----------
        text_file : - string - path to input text file
        output_dir: - string - path to output directory
    
    Returns: 
    --------
        Persist result to output directory
    """
    conf = SparkConf()
    sc = SparkContext(conf=conf)

    # Read input file into RDD
    lines = sc.textFile(text_file)

    # 1. MAP: Convert each line into array of words
    words = lines.flatMap(lambda i: re.split(r'[^\w]+', i))
    # Create a tuple as key-value pair (word, 1)
    pairs = words.map(lambda w: (w, 1))

    # 2. REDUCE
    counts = pairs.reduceByKey(lambda x, y: x + y)

    # Export Result
    counts.saveAsTextFile(output_dir)
    sc.stop()


if __name__ == "__main__":
    args = parse_args()
    run_wordcount_task(args.text_file, args.output)
