from Classes.Etl import Semaforo


class EtlRequest:
     def __init__(self, processId, maxDataVa, semaforo: Semaforo):
        self.processId = processId
        self.maxDataVa = maxDataVa
        self.semaforo = semaforo

     def __str__(self):
        return f"EtlRequest: processId = {self.processId}, maxDataVa = {self.maxDataVa}, {self.semaforo}"
