# Airline Data Ingestion Pipeline

Welcome to the **Airline Data Ingestion Pipeline** project! This project provides a robust, automated data ingestion pipeline for processing daily airline flight data, leveraging a range of AWS services. The aim is to showcase a scalable and reliable approach to managing data ingestion, transformation, and loading (ETL) in a data lake architecture.

## ✈️ Project Overview

In the airline industry, the timely and accurate processing of flight data is critical for analytics, reporting, and decision-making. This project simulates the ingestion of daily flight data into a data lake architecture on AWS. The data is processed and stored in a Redshift data warehouse for further analysis. The pipeline ensures that data ingestion is automated, fault-tolerant, and provides real-time notifications on the data processing status.

## 🚀 Motivation

Data engineering solutions often require handling large volumes of incoming data with minimal manual intervention. This project demonstrates how to build an automated data pipeline using AWS services like S3, Glue, Step Functions, and Redshift. The key focus is on building a resilient pipeline that handles failure gracefully and provides stakeholders with timely updates.

## 🛠️ Key AWS Services Used

1. **Amazon S3 (Simple Storage Service):**  
   Acts as the data lake for storing daily flight data in a Hive-style partitioned format. Raw data files are uploaded to S3 on a daily basis.

2. **Amazon EventBridge:**  
   Configured with a rule that triggers the Step Function whenever new flight data is uploaded to S3. This allows the pipeline to run automatically without manual intervention.

3. **AWS Step Functions:**  
   Serves as the orchestrator of the ETL process. It sequentially triggers the Glue Crawler to update the data catalog and the Glue Job to perform transformations. Upon successful completion, data is ingested into the Redshift `flights` fact table. If a step fails, an Amazon SNS notification is sent via email.

4. **AWS Glue:**  
   - **Glue Crawler:** Automatically catalogs the incoming data in S3 and creates/update the metadata in the AWS Glue Data Catalog.  
   - **Glue Job:** Executes data transformation logic, such as cleaning and transforming the data to match the schema of the target Redshift table.

5. **Amazon Redshift:**  
   A fully managed data warehouse service where processed data is stored in a `flights` fact table. This allows for efficient querying and analysis.

6. **Amazon SNS (Simple Notification Service):**  
   Sends email notifications regarding the success or failure of the data ingestion process, ensuring that stakeholders are informed in real-time.

## 🏗️ Architecture Diagram

![Airline Data Ingestion Pipeline Architecture](https://github.com/desininja/Airline-Data-Ingestion-Pipeline/blob/main/Project%20Related%20Screenshots/Architecture%20Diagram%20of%20Airline-Data-Ingestion-Pipeline.png)

## 📚 Project Workflow

1. **Data Ingestion**:  
   Daily flight data is ingested into an Amazon S3 bucket. The data is partitioned in Hive-style format (e.g., `year=2024/month=09/day=07`) to facilitate easy querying and processing.

2. **Event-Driven Trigger**:  
   An Amazon EventBridge rule is configured to detect new uploads to the S3 bucket. When a new file is uploaded, the EventBridge rule triggers an AWS Step Function to start the ETL process.

3. **Orchestration with AWS Step Functions**:  
   The Step Function orchestrates the following steps in sequence:
   - **AWS Glue Crawler**: Crawls the data in S3, updates the AWS Glue Data Catalog, and defines the schema of the incoming data.
   - **AWS Glue Job**: Transforms the raw data into a format compatible with the Redshift `flights` fact table. The job cleans, filters, and enriches the data as needed.
   - **Data Insertion into Redshift**: Upon successful transformation, the data is loaded into the Redshift `flights` fact table for analytical querying.
   - **Failure Handling with SNS**: If any step in the process fails, Amazon SNS sends an email notification to alert stakeholders.

4. **Real-Time Notifications**:  
   At the end of each run, the pipeline sends a notification through Amazon SNS. If the pipeline is successful, a "Success" email is sent; otherwise, a "Failure" email is triggered with detailed error information.

## 📝 Requirements

- **AWS Account**  
- **Amazon S3** bucket for storing raw flight data  
- **AWS Glue**: Glue Crawler and Glue Job set up for cataloging and transforming data  
- **AWS Step Functions**: Configured state machine for orchestrating the workflow  
- **Amazon Redshift**: A `flights` fact table for storing processed data  
- **Amazon SNS**: An SNS topic and subscription for receiving notifications  
- **IAM Roles** with appropriate permissions for accessing S3, Glue, Redshift, SNS, and Step Functions  
- **Python** and **SQL** for custom scripts and queries used in AWS Glue Jobs

## 🔄 Step-by-Step Implementation

1. **Set Up Amazon S3 Bucket**:  
   - Create an S3 bucket to store daily flight data in Hive-style partitions.  

2. **Configure Amazon EventBridge Rule**:  
   - Set up an EventBridge rule that triggers the Step Function when new files are uploaded to the S3 bucket.  

3. **Define AWS Step Function Workflow**:  
   - Create a Step Function state machine that orchestrates the Glue Crawler, Glue Job, data loading to Redshift, and SNS notifications.  

4. **Create AWS Glue Crawler and Job**:  
   - Define a Glue Crawler to crawl the S3 bucket and update the Glue Data Catalog.  
   - Create a Glue Job using Python or Scala to perform data transformations.  

5. **Set Up Amazon Redshift**:  
   - Create a Redshift cluster and define the `flights` fact table schema to store processed data.  

6. **Integrate SNS for Notifications**:  
   - Configure an SNS topic and subscription to receive email notifications on the ETL process's success or failure.  

7. **Testing and Validation**:  
   - Upload sample data to the S3 bucket and verify that the entire pipeline triggers correctly. Check the data loaded in Redshift and ensure notifications are sent via SNS.

## 📈 Benefits and Outcomes

- **Automated and Scalable**: The pipeline is fully automated and scales seamlessly with data volume.
- **Real-Time Processing**: Reduces the latency of getting insights from daily flight data.
- **Error Handling and Notifications**: Provides robust error handling and instant notifications, ensuring transparency and reliability.

## 📂 Folder Structure

- **Project Screenshots**: Contains architecture diagrams and other relevant visuals.
- **scripts**: Scripts for AWS Glue Jobs and transformations.
- **config**: Configuration files for AWS services and IAM policies.
- **README.md**: This README file.

## 🤝 Conclusion

The **Airline Data Ingestion Pipeline** project showcases how to build a robust, serverless ETL pipeline using AWS managed services. It demonstrates efficient data ingestion, transformation, and loading practices while providing valuable real-time insights into the airline industry.

Feel free to explore the code, contribute, or reach out with any questions or feedback!
