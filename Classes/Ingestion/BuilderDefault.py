import logging

from Classes.Etl.EtlResponse import EtlResponse
from Utils.DbUtils.DbConfMySql import DbConfMySql
from Utils.DbUtils.DbSourceMySql import DbSourceMySql
from Utils.spark_utils import read_data_from_source, write_data_to_target
from Classes.Etl import EtlRequest


class BuilderDefault:
    table = ""

    def __init__(self, etl_request: EtlRequest):
        self.etlRequest = etl_request
        self.banca = self.etlRequest.semaforo.abi
        self.dbConf = DbConfMySql()
        self.dbSource = DbSourceMySql(self.dbConf.getSourceParameters(self.table))

    def ingest(self):
        try:
            logging.info(f"Start ingestion table {self.table}")
            df_source = read_data_from_source(self.dbConf.getSparkParameters(self.table),
                                              query_ingestion=self.dbConf.getIngestionQuery(self.table)
                                              .format(additional_where=self.dbConf.getAdditionalWhere(self.table)),
                                              elements_count=self.getCount(),
                                              num_partitions=self.dbConf.getNumPartitions(self.table))
            write_data_to_target(df_source=df_source, table=self.dbConf.getIngestionTable(self.table))
            logging.info(f"End ingestion table {self.table}")
            return EtlResponse(processId=self.etlRequest.processId, status="OK", error=None)
        except Exception as e:
            logging.error(e)
            logging.error(f"Error in ingest while ingesting {self.table}")
            return EtlResponse(processId=self.etlRequest.processId, status="KO", error=e)

    def getCount(self):
        pass
