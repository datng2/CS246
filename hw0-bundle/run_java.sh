# 
cd ./word-count

# Clean and build package
mvn -DskipTests clean package

# Submit Spark job
spark-submit --class com.tetration.wordcount.App ./target/word-count-1.0-SNAPSHOT.jar ../pg100.txt
