# Learn Hadoop Using Docker
Goal: average selling price

# Download binary
- This Dockerfile build from existing hadoop image but, if you want to download the binary first instead build your own Dockerfile image :
https://archive.apache.org/dist/hadoop/common/hadoop-3.3.1/hadoop-3.3.1.tar.gz

# Kick-off Cluster
1. Clone this repos to your project directory, and `cd hadoop_docker`
2. Linux/MAC Just simply run `./run_cluster.sh`
3. Windows try run this command `docker build -t hadoop-base:3.3.1 . && docker-compose up`

# Run MapReduce Job
 RUN `python map_reduce/analyze_map_reduce.py data/Sales.csv` 

# Hadoop Configurations
1. core-site.xml default and description [here](https://hadoop.apache.org/docs/r3.3.1/hadoop-project-dist/hadoop-common/core-default.xml)
2. hdfs-site.xml default and description [here](https://hadoop.apache.org/docs/r3.3.1/hadoop-project-dist/hadoop-hdfs/hdfs-default.xml)
3. mapred-site.xml default and description [here](https://hadoop.apache.org/docs/r3.3.1/hadoop-mapreduce-client/hadoop-mapreduce-client-core/mapred-default.xml)
4. yarn-site.xml default and description [here](https://hadoop.apache.org/docs/r3.3.1/hadoop-yarn/hadoop-yarn-common/yarn-default.xml)
5. To calculate YARN and MapReduce memory configuration [here](https://docs.cloudera.com/HDPDocuments/HDP2/HDP-2.0.9.0/bk_installing_manually_book/content/rpm-chap1-11.html)
