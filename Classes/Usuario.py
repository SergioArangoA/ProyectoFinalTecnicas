import tkinter as tk
import sys
import os

# Agregar la carpeta raíz del proyecto al PYTHONPATH
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.append(ROOT)

# IMPORTS ABSOLUTOS (estos nunca fallan)
from Data import *
from collections import deque
class Usuario:
    """A Usuario Instance represents a User from the library
        Attributes:

        id(str): Users ID
        HistorialPrestados(deque-Pile): History of borrowed books"""

    def __init__(self, id: str, historialPrestados: deque ):
        self.id = id
        self.historialPrestados= historialPrestados

"""User List filling"""

def guardarUsuarioFuncion (id:str, historialPrestados:deque): 
    """This method calls the User attributes and creates a User Object wich is going to be added to the Users List after being created
    if it doesn't exists. If the user exists is not going to be added"""
    listaUsuarios= #########Falta json con la lista
    idNuevo= id
    
    for usuario in listaUsuarios: #Goes throught the list of Users
        if Usuario.id== idNuevo: #checks if the user is already in the list if it is, a message will show 
            return False #Returns false so the frontend can show the message that the User already exist and has not been added 

    nuevoUsuario= Usuario(id, historialPrestados) #If the User doesn't exist creates a new User instance with the atributes
    listaUsuarios.append(nuevoUsuario)#Adds the new object to the list

    guardarUsuario(listaUsuarios)#Saves the list in the JSON

    return True #User added