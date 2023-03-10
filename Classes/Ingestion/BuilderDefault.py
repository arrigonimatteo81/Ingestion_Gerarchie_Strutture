import logging
import sys
from os import path

from Utils.DbUtils.DbConfPostgres import DbConfPostgres
from Utils.DbUtils.DbSourceMySql import DbSourceMySql
from Utils.spark_utils import read_data_from_source, write_data_to_target

sys.path.append(path.abspath("../Classes")) #per importare il progetto "Classes" che contiene le classi di Etl, semaforo
from Classes.Etl.EtlRequestStrutture import EtlRequestStrutture
from Classes.Etl.EtlResponse import EtlResponse

class BuilderDefault:
    table = ""

    def __init__(self, etl_request: EtlRequestStrutture):
        self.etlRequest = etl_request
        self.banca = self.etlRequest.semaforo.abi
        self.dbConf = DbConfPostgres()
        self.dbSource = DbSourceMySql(self.dbConf.getSourceParameters(self.table))
        self.query_ingestion = self.dbConf.getIngestionQuery(self.table)
        self.additional_where = self.dbConf.getAdditionalWhere(self.table)
        self.num_partitions = self.dbConf.getNumPartitions(self.table)
        self.spark_parameters = self.dbConf.getSparkParameters(self.table)
        self.ingestion_table = self.dbConf.getIngestionTable(self.table)
        self.query_count = self.dbConf.getCountQuery(self.table).format(additional_where=self.additional_where)

    def ingest(self) -> EtlResponse:
        try:
            logging.info(f"Start ingestion table {self.table}")
            df_source = read_data_from_source(source=self.spark_parameters,
                                              query_ingestion=self.query_ingestion
                                              .format(additional_where=self.additional_where),
                                              elements_count=self.getCount(),
                                              num_partitions=self.num_partitions)
            write_data_to_target(df_source=df_source, table=self.ingestion_table)
            logging.info(f"End ingestion table {self.table}")
            return EtlResponse(processId=self.etlRequest.processId, status="OK", error=None)
        except Exception as e:
            logging.error(e)
            logging.error(f"Error in ingest while ingesting {self.table}")
            return EtlResponse(processId=self.etlRequest.processId, status="KO", error=e)

    def getCount(self):
        return self.dbSource.returnCount(self.query_count)
