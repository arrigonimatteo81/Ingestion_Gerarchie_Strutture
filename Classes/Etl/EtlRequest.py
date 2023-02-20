from Classes.Etl import Semaforo


class EtlRequest:
     def __init__(self, processId, semaforo: Semaforo):
        self.processId = processId
        self.semaforo = semaforo

     def __str__(self):
        return f"EtlRequest: processId = {self.processId}, {self.semaforo}"
