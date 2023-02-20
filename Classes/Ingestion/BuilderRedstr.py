from Classes.Ingestion.BuilderDefault import BuilderDefault


class BuilderRedstr(BuilderDefault):
    table = "REDSTR"

    def getCount(self) -> int:
        return self.dbSource.returnCount(self.dbConf.getCountQuery(self.table)
                                         .format(additional_where=self.dbConf.getAdditionalWhere(self.table)))
