package com.tetration.wordcount;

import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.SparkConf;

/**
 * Word Count example;
 *
 */
public class App 
{
    public static void main(String[] args) throws Exception {
        SparkConf conf = new SparkConf();
        JavaSparkContext sc = new JavaSparkContext(conf);
        long numberOfLines = sc.textFile(args[0]).count();
        System.out.printf("%d lines\n", numberOfLines);
    }
}
