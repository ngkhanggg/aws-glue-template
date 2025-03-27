from pyspark.context import SparkConf, SparkContext
from pyspark.sql import SparkSession

class MySpark:
    def __init__(self, account_id, raw_bucket):
        self.list_conf = [
            # AWS Glue Spark Config
            ("spark.sql.catalog.glue_catalog", "org.apache.iceberg.spark.SparkCatalog"),
            ("spark.sql.catalog.glue_catalog.catalog-impl", "org.apache.iceberg.aws.glue.GlueCatalog"),
            ("spark.sql.catalog.glue_catalog.glue.id", account_id),
            ("spark.sql.catalog.glue_catalog.io-impl", "org.apache.iceberg.aws.s3.S3FileIO"),
            ("spark.sql.catalog.glue_catalog.glue.lakeformation-enabled", "true"),
            ("spark.sql.catalog.glue_catalog.warehouse", f"s3://{raw_bucket}/warehouse"),
            ("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions"),

            # Performance Optimizations
            ("spark.sql.adaptive.enabled", "true"),
            ("spark.sql.adaptive.skewJoin.enabled", "true"),
            ("spark.sql.autoBroadcastJoinThreshold", "-1"),
            ("spark.sql.execution.arrow.enabled", "true")
        ]
        self.spark_context = None
        self.spark_session = None

    def init_session(self):
        spark_conf = SparkConf().setAll(self.list_conf)
        self.spark_context = SparkContext(conf=spark_conf)
        self.spark_session = SparkSession(self.spark_context).builder.enableHiveSupport().getOrCreate()

    def get_session(self):
        return self.spark_context, self.spark_session
