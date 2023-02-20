from Utils.DbUtils.interfaces.IDbSource import IDbSource


class DbSourceSqlServer(IDbSource):

    def __init__(self, config):
        self.config = config

    def returnCount(self, query_count):
        pass
