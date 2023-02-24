import logging

from pyspark.sql import SparkSession
from pyspark.sql.utils import QueryExecutionException, AnalysisException, PythonException
from Utils.constants import ROW_N

spark_session = SparkSession.builder.config("spark.jars",
                                            "/home/testspark/Layer_gestionale/config/jar/mysql-connector-j-8.0.32.jar").getOrCreate()


# TODO creazione spark_session per DATAPROC. In spark.jars probabilmente si dovrà mettere anche il jar di connessione a sql server
# spark_session = SparkSession.builder.config("spark.jars", "gs://spark-lib/bigquery/spark-bigquery-latest_2.12.jar").getOrCreate()

def read_data_from_source(source, query_ingestion, elements_count, num_partitions):
    try:
        df_imported_data = spark_session.read \
            .format("jdbc") \
            .option("driver", source['db_driver']) \
            .option("url", source['db_url_input']) \
            .option("dbtable", query_ingestion) \
            .option("user", source['db_user']) \
            .option("password", source['db_password']) \
            .option("partitionColumn", ROW_N) \
            .option("upperBound", str(elements_count)) \
            .option("lowerBound", "1") \
            .option("numPartitions", str(num_partitions)) \
            .load()
        return df_imported_data

    except AnalysisException as ae:
        logging.error(f"AnalysisException in read_data_from_source: {ae}")
        raise ae
    except QueryExecutionException as qee:
        logging.error(f"QueryExecutionException in read_data_from_source: {qee}")
        raise qee
    except PythonException as pe:
        logging.error(f"PythonException in read_data_from_source: {pe}")
        raise pe
    except TimeoutError as te:
        logging.error(f"TimeoutError in read_data_from_source: {te}")
        raise te


def write_data_to_target(df_source, table):
    try:
        df_source \
            .drop(ROW_N) \
            .write \
            .format("jdbc") \
            .option("driver", "com.mysql.cj.jdbc.Driver") \
            .option("url", "jdbc:mysql://localhost:3306/google_Output") \
            .option("dbtable", table) \
            .option("user", "teo") \
            .option("password", "Matteo1981") \
            .mode("overwrite") \
            .save()

        # .partitionBy(PARTITION_FIELD) \

        ##TODO scrittura dataframe su tabella bigquery
        # df_source \
        #    .drop(ROW_N) \
        #    .write \
        #    .format("bigquery") \
        #    .option("table", table) \
        #    .option("temporaryGcsBucket",f"{table}_temporary_bucket") \
        #    .partitionBy(PARTITION_FIELD) \
        #    .mode("overwrite") \
        #    .save()

    except Exception as e:
        logging.error(f"Exception in write_data_to_target: {e}")
        raise e

