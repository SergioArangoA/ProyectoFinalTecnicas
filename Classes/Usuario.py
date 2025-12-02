import tkinter as tk
import sys
import os

# Agregar la carpeta raíz del proyecto al PYTHONPATH
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.append(ROOT)

# IMPORTS ABSOLUTOS (estos nunca fallan)
from collections import deque
class Usuario:
    """A Usuario Instance represents a User from the library
        Attributes:

        id(str): Users ID
        HistorialPrestados(deque-Pile): History of borrowed books
        
        Methods: 
        usuarioADiccionario(): This method converts the user object in a dictionary

        """

    def __init__(self, id: str, historialPrestados: list ):
        self.id = id
        self.historialPrestados= deque(historialPrestados)

def usuarioADiccionario(self):
    """This method converts the user object in a dictionary"""
    diccionarioUsuario = {"id":self.id,"historialPrestados":list(self.historialPrestados)}
    return diccionarioUsuario