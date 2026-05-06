import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
import re

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node S3-Flights-Raw-Data
S3FlightsRawData_node1724010778791 = glueContext.create_dynamic_frame.from_catalog(database="airline-database-glue", table_name="flights_data", transformation_ctx="S3FlightsRawData_node1724010778791")

# Script generated for node Amazon Redshift
AmazonRedshift_node1724012581603 = glueContext.create_dynamic_frame.from_catalog(database="airline-database-glue", table_name="dev_airline_airports_dim", redshift_tmp_dir="s3://aws-glue-assets-025066280149-us-east-1/temporary/", transformation_ctx="AmazonRedshift_node1724012581603")

# Script generated for node Filter
Filter_node1724010908895 = Filter.apply(frame=S3FlightsRawData_node1724010778791, f=lambda row: (row["depdelay"] > 60), transformation_ctx="Filter_node1724010908895")

# Script generated for node Origin Join
Filter_node1724010908895DF = Filter_node1724010908895.toDF()
AmazonRedshift_node1724012581603DF = AmazonRedshift_node1724012581603.toDF()
OriginJoin_node1724011732862 = DynamicFrame.fromDF(Filter_node1724010908895DF.join(AmazonRedshift_node1724012581603DF, (Filter_node1724010908895DF['originairportid'] == AmazonRedshift_node1724012581603DF['airport_id']), "left"), glueContext, "OriginJoin_node1724011732862")

# Script generated for node Change Schema
ChangeSchema_node1724012760945 = ApplyMapping.apply(frame=OriginJoin_node1724011732862, mappings=[("depdelay", "long", "dep_delay", "bigint"), ("arrdelay", "long", "arr_delay", "bigint"), ("destairportid", "long", "destairportid", "long"), ("carrier", "string", "carrier", "varchar"), ("city", "string", "dep_city", "varchar"), ("state", "string", "dep_state", "varchar"), ("name", "string", "dep_airport", "varchar")], transformation_ctx="ChangeSchema_node1724012760945")

# Script generated for node Join
ChangeSchema_node1724012760945DF = ChangeSchema_node1724012760945.toDF()
AmazonRedshift_node1724012581603DF = AmazonRedshift_node1724012581603.toDF()
Join_node1724013051749 = DynamicFrame.fromDF(ChangeSchema_node1724012760945DF.join(AmazonRedshift_node1724012581603DF, (ChangeSchema_node1724012760945DF['destairportid'] == AmazonRedshift_node1724012581603DF['airport_id']), "left"), glueContext, "Join_node1724013051749")

# Script generated for node Change Schema
ChangeSchema_node1724013098500 = ApplyMapping.apply(frame=Join_node1724013051749, mappings=[("carrier", "varchar", "carrier", "string"), ("dep_state", "varchar", "dep_state", "string"), ("state", "string", "arr_state", "string"), ("arr_delay", "bigint", "arr_delay", "long"), ("city", "string", "arr_city", "string"), ("name", "string", "arr_airport", "string"), ("dep_city", "varchar", "dep_city", "string"), ("dep_delay", "bigint", "dep_delay", "long"), ("dep_airport", "varchar", "dep_airport", "string")], transformation_ctx="ChangeSchema_node1724013098500")

# Script generated for node Flights-fact-target
Flightsfacttarget_node1724013502201 = glueContext.write_dynamic_frame.from_catalog(frame=ChangeSchema_node1724013098500, database="airline-database-glue", table_name="dev_airline_flights_fact", redshift_tmp_dir="s3://redshift-temp-data-airline-project/temp-folder/flights-fact/",additional_options={"aws_iam_role": "arn:aws:iam::025066280149:role/Redshift-Access"}, transformation_ctx="Flightsfacttarget_node1724013502201")

job.commit()