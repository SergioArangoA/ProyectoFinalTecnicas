import tkinter as tk
import sys
import os
from datetime import date, datetime

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
        diccionarioUsuario = {"id":self.id,"historialPrestados":list(self.historialPrestados)}
        return diccionarioUsuario
    
    def agregarReserva(self,libro):
        """Adds the reservation to the user's reservation history"""
        from Classes.Libro import Libro
        if libro.enInventario > 0 or libro.listaEspera[0] == self: #The book can be borrowed only if the user is at the top of the waitlist
            libro.enInventario -= 1
            libro.prestados += 1
            self.historialPrestados.append({"fecha":date.today().strftime("%Y-%m-%d"),"ISBN":libro.isbn,"retornado":False})
        
        else:
            libro.listaEspera.append(self)
    
    def retornarLibro(self,libro):
        """Returns the book to the inventory"""
        from Classes.Libro import Libro
        for prestado in self.historialPrestados:
            if prestado["ISBN"] == libro.isbn:
                prestado["retornado"] = True



