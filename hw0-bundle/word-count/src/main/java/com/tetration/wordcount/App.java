package com.tetration.wordcount;

import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.SparkConf;
// import org.apache.spark.api.java.JavaRDD;

/**
 * Word Count example;
 *
 */
public class App 
{
    public static void main(String[] args) {
        SparkConf conf = new SparkConf();
        JavaSparkContext sc = new JavaSparkContext(conf);
        long numberOfLines = sc.textFile(args[0]).count();
        System.out.printf("%d lines\n", numberOfLines);
//        System.out.println("Hello World");
        sc.close();
    }
}
