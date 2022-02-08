import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node S3 bucket
S3bucket_node1 = glueContext.create_dynamic_frame.from_catalog(
    database="mydatafifa",
    table_name="fifadataforetl",
    transformation_ctx="S3bucket_node1",
)

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1644344210161 = glueContext.create_dynamic_frame.from_catalog(
    database="mydatafifa",
    table_name="fifadataforetl",
    transformation_ctx="AWSGlueDataCatalog_node1644344210161",
)

# Script generated for node ApplyMapping
ApplyMapping_node2 = ApplyMapping.apply(
    frame=S3bucket_node1,
    mappings=[
        ("col0", "long", "col0", "long"),
        ("col1", "string", "col1", "string"),
        ("col2", "string", "col2", "string"),
        ("col3", "string", "col3", "string"),
        ("col4", "string", "col4", "string"),
        ("col5", "string", "col5", "string"),
        ("col6", "string", "col6", "string"),
        ("col7", "string", "col7", "string"),
        ("col8", "string", "col8", "string"),
        ("col9", "string", "col9", "string"),
        ("col10", "string", "col10", "string"),
        ("col11", "string", "col11", "string"),
        ("col12", "string", "col12", "string"),
        ("col13", "string", "col13", "string"),
        ("col14", "string", "col14", "string"),
        ("col15", "string", "col15", "string"),
        ("col16", "string", "col16", "string"),
        ("col17", "string", "col17", "string"),
        ("col18", "string", "col18", "string"),
        ("col19", "string", "col19", "string"),
        ("col20", "string", "col20", "string"),
        ("col21", "string", "col21", "string"),
        ("col22", "string", "col22", "string"),
        ("col23", "string", "col23", "string"),
        ("col24", "string", "col24", "string"),
        ("col25", "string", "col25", "string"),
        ("col26", "string", "col26", "string"),
        ("col27", "string", "col27", "string"),
        ("col28", "string", "col28", "string"),
        ("col29", "string", "col29", "string"),
        ("col30", "string", "col30", "string"),
        ("col31", "string", "col31", "string"),
        ("col32", "string", "col32", "string"),
        ("col33", "string", "col33", "string"),
        ("col34", "string", "col34", "string"),
        ("col35", "string", "col35", "string"),
        ("col36", "string", "col36", "string"),
        ("col37", "string", "col37", "string"),
        ("col38", "string", "col38", "string"),
        ("col39", "string", "col39", "string"),
        ("col40", "string", "col40", "string"),
        ("col41", "string", "col41", "string"),
        ("col42", "string", "col42", "string"),
        ("col43", "string", "col43", "string"),
        ("col44", "string", "col44", "string"),
        ("col45", "string", "col45", "string"),
        ("col46", "string", "col46", "string"),
        ("col47", "string", "col47", "string"),
        ("col48", "string", "col48", "string"),
        ("col49", "string", "col49", "string"),
        ("col50", "string", "col50", "string"),
        ("col51", "string", "col51", "string"),
        ("col52", "string", "col52", "string"),
        ("col53", "string", "col53", "string"),
        ("col54", "string", "col54", "string"),
        ("col55", "string", "col55", "string"),
        ("col56", "string", "col56", "string"),
        ("col57", "string", "col57", "string"),
        ("col58", "string", "col58", "string"),
        ("col59", "string", "col59", "string"),
        ("col60", "string", "col60", "string"),
        ("col61", "string", "col61", "string"),
        ("col62", "string", "col62", "string"),
        ("col63", "string", "col63", "string"),
        ("col64", "string", "col64", "string"),
        ("col65", "string", "col65", "string"),
        ("col66", "string", "col66", "string"),
        ("col67", "string", "col67", "string"),
        ("col68", "string", "col68", "string"),
        ("col69", "string", "col69", "string"),
        ("col70", "string", "col70", "string"),
        ("col71", "string", "col71", "string"),
        ("col72", "string", "col72", "string"),
        ("col73", "string", "col73", "string"),
        ("col74", "string", "col74", "string"),
        ("col75", "string", "col75", "string"),
        ("col76", "string", "col76", "string"),
        ("col77", "string", "col77", "string"),
        ("col78", "string", "col78", "string"),
        ("col79", "string", "col79", "string"),
        ("col80", "string", "col80", "string"),
        ("col81", "string", "col81", "string"),
        ("col82", "string", "col82", "string"),
        ("col83", "string", "col83", "string"),
        ("col84", "string", "col84", "string"),
        ("col85", "string", "col85", "string"),
        ("col86", "string", "col86", "string"),
        ("col87", "string", "col87", "string"),
        ("col88", "string", "col88", "string"),
    ],
    transformation_ctx="ApplyMapping_node2",
)

# Script generated for node MySQL
MySQL_node1644345018038 = glueContext.write_dynamic_frame.from_catalog(
    frame=AWSGlueDataCatalog_node1644344210161,
    database="mydatafifa",
    table_name="fifadataforetl",
    transformation_ctx="MySQL_node1644345018038",
)

# Script generated for node S3 bucket
S3bucket_node3 = glueContext.write_dynamic_frame.from_options(
    frame=ApplyMapping_node2,
    connection_type="s3",
    format="json",
    connection_options={
        "path": "s3://fifadataforetl/athena-output/",
        "partitionKeys": [],
    },
    transformation_ctx="S3bucket_node3",
)

job.commit()
