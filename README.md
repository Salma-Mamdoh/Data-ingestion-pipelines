Sure, here's the complete README.md for the "Data Ingestion Pipelines" project:

# Data Ingestion Pipelines

This project demonstrates the implementation of two different data ingestion approaches: batch data migration using Apache Sqoop and real-time data ingestion using Apache Flume and Apache Kafka.

## Task 1: Data Migration with Apache Sqoop
![sqoop](https://github.com/user-attachments/assets/3f991a07-9e99-4938-a539-74eaef3948a5)  ![Hadoop logo](https://github.com/user-attachments/assets/ae45fc28-73c9-4223-866a-a194cbfee855)

### Task Overview
This task focuses on migrating historical data from a local relational database to Hadoop's HDFS using Apache Sqoop. It includes periodic updates with incremental imports to handle new data additions.

### Requirements
- Relational database (MariaDB)
- Apache Hadoop (HDFS)
- Apache Sqoop

### Implementation Steps
1. Set up the relational database and create a sample table with historical data.
2. Configure Apache Hadoop and HDFS on your system.
3. Install and configure Apache Sqoop to connect to the relational database and HDFS.
4. Perform the initial full data import from the database to HDFS using Sqoop.
5. Implement a script or job to perform periodic incremental imports, capturing new data additions in the database.
6. Verify the data in HDFS and compare it with the source database.

### Expected Outcome
- Successful migration of historical data from the relational database to HDFS using Apache Sqoop.
- Implemented periodic incremental data imports to keep the HDFS data up-to-date.
- Validated the data integrity between the source database and the HDFS destination.

## Task 2: Real-Time Data Ingestion with Apache Flume and Kafka
![flume logo](https://github.com/user-attachments/assets/73ed4293-ec3d-48f5-a70c-c5e323e543d7) ![Kafka logo](https://github.com/user-attachments/assets/dcc6769f-fa0b-4fcc-b68d-acdc3a7370c5)


### Task Overview
This task focuses on setting up a real-time data ingestion pipeline using Apache Flume and Apache Kafka. It involves collecting log data from a local directory and streaming it to Kafka for real-time processing.

### Requirements
- Apache Hadoop (HDFS)
- Apache Flume
- Apache Kafka
- Python

### Implementation Steps
1. Set up Apache Hadoop and HDFS on your system.
2. Write a Python Script to generate log file data.
3. Install and configure Apache Flume to collect log data from a local directory.
4. Set up Apache Kafka and create a Kafka topic to receive the log data.
5. Configure Flume to use Kafka as the destination for the collected log data.
6. Test the real-time data ingestion pipeline by generating sample log data in the local directory and verifying the data in the Kafka topic.
7. Explore options to consume the data from the Kafka topic for real-time processing or further downstream analysis.

### Expected Outcome
- Successful setup of the real-time data ingestion pipeline using Apache Flume and Apache Kafka.
- Collected log data from a local directory and streamed it to a Kafka topic in real-time.
- Demonstrated the ability to consume the data from the Kafka topic for real-time processing or further analysis.

## Conclusion
This project showcases two distinct data ingestion approaches: batch data migration using Apache Sqoop and real-time data ingestion using Apache Flume and Apache Kafka. By completing these tasks, you will gain hands-on experience in setting up and managing data ingestion pipelines, which are essential for building robust and scalable data processing systems.
