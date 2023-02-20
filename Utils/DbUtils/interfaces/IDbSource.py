from abc import ABC, abstractmethod


class IDbSource(ABC):

    @abstractmethod
    def returnCount(self, query_count) -> int:
        pass
