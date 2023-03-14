# Steps
1. `docker network create hadoop_network`
2. `docker build -t hadoop-base:3.3.1 -f Dockerfile-hadoop .`
3. `docker-compose -f docker-compose-hadoop.yml up -d`
4. `cd airflow`
5. `./run_airflow.sh`
6. `cd ..`
7. `docker-compose -f docker-compose-airflow.yml up -d`
