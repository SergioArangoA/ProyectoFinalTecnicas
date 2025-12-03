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
        HistorialPrestados(deque-Pile): History of borrowed books"""

    def __init__(self, id: str, historialPrestados: list ):
        self.id = id
        self.historialPrestados= deque(historialPrestados)

    """User List filling"""
    @classmethod
    def guardarUsuarioFuncion (cls, id:str, historialPrestados:deque): 
        from Data.DataManagement import cargarUsuarios #The imports are made here to avoid making circular imports when initializing the program
        from Data.DataManagement import guardarUsuarios
        """This method calls the User attributes and creates a User Object wich is going to be added to the Users List after being created
        if it doesn't exists. If the user exists is not going to be added"""
        listaUsuarios = cargarUsuarios()
        idNuevo= id
        
        for usuario in listaUsuarios: #Goes throught the list of Users
            if usuario.id == idNuevo: #checks if the user is already in the list if it is, a message will show 
                return False #Returns false so the frontend can show the message that the User already exist and has not been added 

        nuevoUsuario= Usuario(id, historialPrestados) #If the User doesn't exist creates a new User instance with the atributes
        listaUsuarios.append(nuevoUsuario)#Adds the new object to the list

        guardarUsuarios(listaUsuarios)#Saves the list in the JSON

        return True #User added
    
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



