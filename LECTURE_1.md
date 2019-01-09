## What I would learn

* Mine Different types of data
* Use different models of computation
* Solve Real-world problems
* Various Tools

## End goal:

* Data --> (Chef, Data Scientist) --> Magic


## After this course

* CS341 Project in Data Mining 
* Research project on Big Data

## Large-Scale computing

* **Problem**: Machines do fail (1M clusters --> 1000 clusters fail every dat!)

* **Solution**:
    * Issue: Copying data over a network takes time. Instead of copying, perform computation on the
    * Idea:
        * Bring computation to the data:
            Do computation on where the data are.
        * Store files multiple times for reliability.
    * **Spark/Hadoop** address theses problems: --> abstracted low-level details on dealing with data for scientists / engineers.

## How Do Spark/Hadoop Work?

* **Storage Infrastructure - File System** : GFS (Google), HDFS (Hadoop), S3 (Amazon)
* **Programming Model**: MapReduce / Spark

## Storage Infrastructure:

* If nodes fail, how to store data persistently?
    * Use distributed file system (global file namespace)

* Typical Usage:
    * Huge Files (100s of GB to TB).
    * Data is rarely update in place.
    * Reads and appends are common.

## Distributed File System

* Chunk Servers:
    * File is split into contiguous chunks
    * Typically each chunk is 16-64MB.
    * Each chunk is replicated (usually 2x or 3x).
    * Try to keep replicas in different racks.

* Master Node:
    * a.k.a Name Node in Hadoop's HDFS.
    * Stores metadata about where files are stored.
    * Might be replicated

* Client Library (API):
    * Talks to the master to find chunk servers.
    * connects directly to chunk servers.


* Result:
    * **Reliable distributed file system**.
    * Data kept in "chunks" spread across machines.
    * Each chunk replicated on different machines.
        * **Seamless recovery** from disk or machine failure.

    * **BRING COMPUTATION DIRECTLY TO DATA!**
    * **CHUNK SERVERS ALSO SERVE AS COMPUTE SERVERS**.

## Programming Model (Computation over Distributed System)
* **MapReduce** is a style of programming:
    * Easy parallel programming.
    * Invisible management of hardware and software failures.
    * Easy management of very-large-scale data.
    * Several **implementations** (Hadoop, Spark, Flink, and original Google MapReduce).

* 3 steps of MapReduce:
    * **Map**:
        * Apply a user-written map function to each input element
        * Output: set of 0, 1 or more key-value pairs
    * **Group-by-key**: Sort and shuffle key-value pairs
        * Outputs: key-(list of values) pairs
    * **Reduce**: 
        * For every key, appy a reduce function to each key-(list of values).

Example: Word Counting in Document

* Split document into chunks.
* Apply map function to each chunk in parallel.
* Aggregate the result.


## Problems with MapReduce:
* Difficulty of Programming directly in MR.
    * Many problems aren't easily described as map-reduce.
* Performance bottlenecks, or batch not fitting the use cases.
    * Persistence to disk typically slower than in-memory work.

* In short, MR doesn't compose well for large applications
    * Many times one needs to chain multiple map-reduce steps.

## Spark (One of Data-Flow systems):
* Mapreduce uses two "ranks" of tasks: map, reduce
* Data-flow systems generaliza this in two ways:
    1. Allow any number of tasks / ranks.
    2. Allow functions other than map, reduce. As long as data flow is in one direction only, we can have the blocking property and allow recovery of tasks rather than whole jobs.

* **SPARK** :
    * Expressive computing system, not limited to map-reduce model.
    * Additions to MapReduce model:
        * Faster data sharing
            * Avoids saving intermediate results to disk.
            * Caches data for repetitive queries
    * General execution graphs (DAGs).
    * Richer functions than just map and reduce.
    * Compatible with Hadoop.
    * Open-source software
    * Supports: Java, Scala and Python.

* **Key idea**: Resilient Distributed Dataset (RDD).
* Higher-level APIs: DataFrames and DataSets
    * Introduced in more recent versions of Spark.
    * Different APIs for aggregate data, which allowed to introduce SQL support.


## Spark: RDD

* Paritioned collection of records (Generalized idea of (key-value) pairs).

* Spread across the cluster, read-only.
* Caching dataset in memory.
    * Different storage levels available.
    * Fallback to disk possible.
* RDDs can be created from Hadoop, or by transforming other RDDs.

* **Transformations**
    * map, filter, join, union, intersection, distinct.
    * **Lazy evaluation**: nothing computed until an action requires it.

* **DataFrames**:
    * Data organized into named columns
    * Imposes a structure onto a dist. collection of data, allowing higher-level abstraction.

* **Dataset**:
    * Extension of DataFrame API, which provides *type-safe, object-oriented programming interface* (compile-time error detection).


## Spark vs Hadoop
* Performance: **Spark normally faster** with caveats.
    * Spark can process data in-memory, but requires large amount of memory. Hadoop, on the other hand, persists back to disk after a map or reduce action.
    * MapReduce easily runs alongside other services with minor performance differences.
* Ease of Use : **Spark is easier to program** (higher level APIs).
* Data processing: **Spark more general**


Exmaple: large web cor