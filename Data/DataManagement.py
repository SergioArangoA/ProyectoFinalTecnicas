import tkinter as tk
import sys
import os
# Agregar la carpeta raíz del proyecto al PYTHONPATH
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.append(ROOT)

# IMPORTS ABSOLUTOS (estos nunca fallan)
import json
from Classes.Libro import Libro
from Classes.Estante import Estante
from Classes.Usuario import Usuario

#HAY QUE CREAR LAS VARIABLES DE COLOR DUDOSO
def guardarInventarioGeneral(InventarioGeneral: list[Libro]):
    """Saves the general inventory in a JSON"""
    with open ("InventarioGeneral.json", "w",encoding = "utf-8") as archivo:
        diccionarioLibros = [libro.libroADict() for libro in InventarioGeneral] #convirtiendo las instancias de libro en lista de diccionarios
        json.dump(diccionarioLibros,archivo, ensure_ascii=False, indent = 4) #guardando la lista de diccionarios

def guardarInventarioOrdenado(InventarioGeneral: list[Libro]):
    """Saves the ordered inventory in a JSON"""
    with open ("InventarioOrdenado.json", "w",encoding = "utf-8") as archivo:
        diccionarioLibros = [libro.libroADict() for libro in InventarioGeneral]
        json.dump(diccionarioLibros, archivo, ensure_ascii=False, indent=4)

def cargarInventarioGeneral():
    """This method loads the general inventory JSON, and returns a list
    of instances of the class Libro. if the JSON cannot be openned, it will print
    in console a warning and return an empty list"""
    try:
        with open("InventarioGeneral.json","r",encoding="utf-8") as archivo:
            InventarioCargado = json.load(archivo)
            print("Inventario general cargado exitosamente")
            InventarioGeneral =[Libro(**libro)for libro in InventarioCargado] #Cada diccionario en la lista de diccionarios es convertido en una instancia de libro
            return InventarioGeneral 
    except (FileNotFoundError, json.JSONDecodeError):
        print("No encontró un inventario general, creando un vacío.")
        return []

def cargarInventarioOrdenado():
    """This method loads the ordered inventory JSON, and returns a list
    of instances of the class Libro. if the JSON cannot be openned, it will print
    in console a warning and return an empty list"""
    try:
        with open("InventarioOrdenado.json","r",encoding="utf-8") as archivo:
            InventarioCargado = json.load(archivo)
            print("Inventario ordenado cargado exitosamente")
            InventarioOrdenado =[Libro(**libro)for libro in InventarioCargado]
            return InventarioOrdenado
    except (FileNotFoundError, json.JSONDecodeError):
        generalInventory = []
        print("No encontró un inventario general, creando una lista vacía.")
        return []
    
def guardarEstantes(ListaEstantes: list[Estante]):
    """Saves the list of shelves in a JSON"""
    with open ("Estantes.json", "w",encoding = "utf-8") as archivo:
        ListaCargadaEstantes= [estante.objetoDiccionario() for estante in ListaEstantes] #Desde la funcion que convierte objeto a diccionario, es decir los estantes de objeto estante en diccionario
        json.dump(ListaCargadaEstantes,archivo, ensure_ascii=False, indent = 4) #la llama y lee cada elemento en ese diccionario y crea una lista de diccionarios y la guarda en un JSON

def cargarEstantes():
    """Loads the list of shelves saved in the JSON"""
    listaEstantes = []
    try:
        with open ("Estantes.json","r",encoding="utf-8") as archivo:
            ListaCargadaEstantes = json.load(archivo)
            listaEstantes = [Estante(**estante)for estante in ListaCargadaEstantes] #Each dictionary loaded in the JSON is turned into a Estante instance
    
    except (FileNotFoundError, json.JSONDecodeError):
        print("No se encontró lista de estantes guardada, creando una lista vacía")
    
    return listaEstantes

def guardarUsuarios(listaUsuarios:list[Usuario]):
    """Saves the user list in a JSON file"""
    with open("Usuarios.json","w",encoding="utf-8") as archivo:
        listaDiccionarioUsuarios = []
        for usuario in listaUsuarios:
            listaDiccionarioUsuarios.append(usuario.usuarioADiccionario)
        json.dump(listaDiccionarioUsuarios)

def cargarUsuarios():
    listaUsuarios = []
    try:
        with open ("Usuarios.json","r",encoding="utf-8") as archivo:
            listaCargadaUsuarios = json.load(archivo)
            listaUsuarios = [Estante(**usuario)for usuario in  listaCargadaUsuarios] #Each dictionary loaded in the JSON is turned into a Usuario instance
    
    except (FileNotFoundError, json.JSONDecodeError):
        print("No se encontró lista de usuarios guardada, creando una lista vacía")
    return listaUsuarios



def guardarHistorialPrestamos(PilaHistorialPrestamos):
    """Saves the borrowed books Pile in a JSON file"""
    with open("Historial Prestamos.json","w",encoding = "utf-8") as archivo:
        json.dump(PilaHistorialPrestamos,archivo, ensure_ascii=False, indent = 4)

def guardarListaEspera(listaEspera):
    """Saves the wait list as a list in a JSON"""
    with open("listaEspera.json","w",encoding = "utf-8") as archivo:
        json.dump(listaEspera,archivo, ensure_ascii=False, indent = 4)
