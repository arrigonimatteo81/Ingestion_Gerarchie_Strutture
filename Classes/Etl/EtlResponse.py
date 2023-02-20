

class EtlResponse:

    def __init__(self, processId, status, error):
        self.processId=processId
        self.status = status
        self.error = error

    def __str__(self):
        return f"EtlResponse: processId = {self.processId}, status = {self.status}, error={self.error}"
