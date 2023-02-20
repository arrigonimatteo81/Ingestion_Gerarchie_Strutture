from Classes.Ingestion.BuilderDefault import BuilderDefault


class BuilderRedven(BuilderDefault):
    table = "REDVEN"

    def getCount(self) -> int:
        return self.dbSource.returnCount(self.dbConf.getCountQuery(self.table)
                                         .format(additional_where=self.dbConf.getAdditionalWhere(self.table)))
