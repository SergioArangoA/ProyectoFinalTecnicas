from collections import deque
class Usuario:
    """A Usuario Instance represents a User from the library
        Attributes:

        id(str): Users ID
        HistorialPrestados(deque-Pile): History of borrowed books"""

    def __init__(self, id: str, historialPrestados: deque, ):
        self.id = id
        self.historialPrestados= historialPrestados