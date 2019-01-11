# HDFS and MapReduce

## Terminologies

* **HDFS**: Hadoop Distributed File System (think S3, not file system aka cannot mount)
* **Cluster**: a group of computers working together.
* **Node**: an individual computer in the cluster.
* **daemon**: a program running on a node
* **NameNode** : store meta data for each "chunk" of
## Hadoop

* Optimizes for data streaming. 
* Not designed for small files.

## HDFS Command line examples

```bash
# Copy a file `foo.txt` from local disk to user's directory in HDFS.
$ hdfs dfs -put foo.txt foo.txt

# Get a directory listing of the user's home directory in HDFS.
$ hdfs dfs -ls

# Get a directory listing of the HDFS root directory
$ hdfs dfs -ls /
```

## YARN 
* **YARN** = Yet another resource negotiator
* **YARN** is a Hadoop processing layer that contains:
    - Resource manager
    - Job scheduler
* **YARN** allows multiple data processing engines to run on a single Hadoop cluster.
    - Batch Programs (e.g Spark, MapReduce).
    - Interactive SQL (Impala).
    - Advanced analytics (Spark, Impala).
    - Streaming (e.g Spark Streaming)

## Running App. on YARN

* **Containers** (not docker)
    - Created by the RM upon request
    - Allocate certain amount of resources (memory, CPU) on a slave node.
    - Applications run in one or more containers.

* **Application Master**
    - One per application.
    - Framework/application specific.
    - Runs in a container.
    - Requests more containers to run application tasks.

## MapReduce - Terminology

* **Job**: a full program
    - A complete execution of Mappers and Reducers over a dataset.
    - In MapReduce 2, the term *application* is often used in place of *job*.
* **Task**: the execution of a single Mapper or Reducer over a slice of data.
* **Task attempt**: a particular instance of an attempt to execute a task.
    * There will be at least as many task attempts as there are tasks.
    * If a task attempt **fails**, another will be started by the *JobTracker*.
    * *Speculative execuation* (see later) can also result in more task attempts than completed tasks.
    