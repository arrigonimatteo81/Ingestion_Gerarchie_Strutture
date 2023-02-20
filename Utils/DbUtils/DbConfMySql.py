import configparser
import json
import logging

import mysql.connector

from Utils.DbUtils.interfaces.IDbConf import IDbConf


class DbConfMySql(IDbConf):

    def __init__(self, table):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.db_config = mysql.connector.connect(
            host=self.config['CONFIG']['db_host'],
            user=self.config['CONFIG']['db_user'],
            password=self.config['CONFIG']['db_password'],
            database=self.config['CONFIG']['db_name']
        )
        #TODO capire cosa sia meglio...valorizzare tutto qui o utilizzare i metodi sotto per tornare i singoli valori
        #query_cursor = self.db_config.cursor()
        #query_cursor.execute(f"SELECT Output_Table, Additional_Where, Num_Partitions,"
        #                     f"Sql_String_Ingestion, Db_Source_Params, Spark_Params"
        #                     f"Sql_String_Count from config_tables where Original_Table='{table}'")
        #self.output_table = query_cursor.fetchone()[0]
        #self.additional_where = self.getAdditionalWhere(query_cursor.fetchone()[1])
        #self.num_partitions = self.getNumPartitions(query_cursor.fetchone()[2])
        #self.string_ingestion = query_cursor.fetchone()[3]
        #self.db_source_param = self.getSourceParameters(query_cursor.fetchone()[4])
        #self.db_spark_params = self.getSparkParameters(query_cursor.fetchone()[5])
        #self.string_count = query_cursor.fetchone()[6]

    def getCountQuery(self, table):
        try:
            query_count_cursor = self.db_config.cursor()
            query_count_cursor.execute(f"SELECT Sql_String_Count from config_tables where Original_Table='{table}'")
            return query_count_cursor.fetchone()[0]
        except TimeoutError as te:
            logging.error(f"QueryExecutionException in getCountQuery: {te}")
            raise te

    def getIngestionQuery(self, table):
        try:
            query_ingestion_cursor = self.db_config.cursor()
            query_ingestion_cursor.execute(f"SELECT Sql_String_Ingestion from config_tables where Original_Table='{table}'")
            return query_ingestion_cursor.fetchone()[0]
        except TimeoutError as te:
            logging.error(f"QueryExecutionException in getIngestionQuery: {te}")
            raise te

    def getIngestionTable(self, table):
        try:
            query_cursor = self.db_config.cursor()
            query_cursor.execute(
                f"SELECT Output_Table from config_tables where Original_Table='{table}'")
            return query_cursor.fetchone()[0]
        except TimeoutError as te:
            logging.error(f"QueryExecutionException in getIngestionTable: {te}")
            raise te

    def getSparkParameters(self, table):
        try:
            query_cursor = self.db_config.cursor()
            query_cursor.execute(f"select Spark_Params from config_tables where Original_Table='{table}'")
            spark_confs = query_cursor.fetchone()[0]
            spark_params = json.loads(spark_confs)
            return spark_params
        except TimeoutError as te:
            logging.error(f"QueryExecutionException in getSparkParameters: {te}")
            raise te

    def getAdditionalWhere(self, table):
        try:
            query_cursor = self.db_config.cursor()
            query_cursor.execute(
                f"SELECT Additional_Where from config_tables where Original_Table='{table}'")
            add_where = query_cursor.fetchone()[0]
            if add_where is not None:
                return f"and {add_where}"
            else:
                return ""
        except TimeoutError as te:
            logging.error(f"QueryExecutionException in getAdditionalWhere: {te}")
            raise te

    def getNumPartitions(self, table):
        try:
            query_cursor = self.db_config.cursor()
            query_cursor.execute(
                f"SELECT Num_Partitions from config_tables where Original_Table='{table}' ")
            num_partitions = query_cursor.fetchone()[0]
            if num_partitions is not None:
                return int(num_partitions)
            else:
                return 100
        except TimeoutError as te:
            logging.error(f"QueryExecutionException in getNumPartitions: {te}")
            raise te

    def getSourceParameters(self, table):
        try:
            query_cursor = self.db_config.cursor()
            query_cursor.execute(f"select Db_Source_Params from config_tables where Original_Table='{table}'")
            db_source_confs = query_cursor.fetchone()[0]
            db_source_params = json.loads(db_source_confs)
            return db_source_params
        except TimeoutError as te:
            logging.error(f"QueryExecutionException in getSourceParameters: {te}")
            raise te
