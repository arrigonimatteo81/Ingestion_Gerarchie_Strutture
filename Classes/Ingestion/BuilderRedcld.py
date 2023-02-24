from Classes.Ingestion.BuilderDefault import BuilderDefault


class BuilderRedcld(BuilderDefault):
    table = "REDCLD"

    def getCount(self) -> int:
        return 10000


