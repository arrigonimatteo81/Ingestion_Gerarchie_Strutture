from Classes.Ingestion.BuilderDefault import BuilderDefault


class BuilderRedent(BuilderDefault):
    table = "REDENT"

    def getCount(self) -> int:
        return 100
