from abc import ABC, abstractmethod


class IDbConf(ABC):

    @abstractmethod
    def getCountQuery(self, table) -> str:
        pass

    @abstractmethod
    def getIngestionQuery(self, table) -> str:
        pass

    @abstractmethod
    def getIngestionTable(self, table) -> str:
        pass

    @abstractmethod
    def getSparkParameters(self, table) -> dict:
        pass

    @abstractmethod
    def getAdditionalWhere(self, table) -> str:
        pass

    @abstractmethod
    def getNumPartitions(self, table) -> int:
        pass

    @abstractmethod
    def getSourceParameters(self, table) -> dict:
        pass
