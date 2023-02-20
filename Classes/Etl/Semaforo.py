class Semaforo:

    def __init__(self, id, abi, oCarico):
        self.id = id
        self.abi = abi
        self.oCarico = oCarico

    def __str__(self):
        return f"Semaforo: id = {self.id}, abi = {self.abi},oCarico={self.oCarico}"
