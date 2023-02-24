from Classes.Ingestion.BuilderDefault import BuilderDefault


class BuilderRedpvi(BuilderDefault):
    table = "REDPVI"

    def getCount(self) -> int:
        return 500


