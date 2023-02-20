import logging

from Classes.Ingestion.BuilderDefault import BuilderDefault
from Classes.Etl.EtlResponse import EtlResponse
from Utils.spark_utils import read_data_from_source, write_data_to_target


class BuilderRedent(BuilderDefault):
    table = "REDENT"

    def __init__(self, etl_request):
        super().__init__(etl_request)

    def getQueryIngest(self):
        return self.dbConf.getIngestionQuery(self.table).format(additional_where=self.getAdditionalWhere())

    def getCount(self) -> int:
        #return self.dbSource.returnCount(self.dbConf.getCountQuery(self.table)
        #                                 .format(additional_where=self.getAdditionalWhere()))
        return 100
