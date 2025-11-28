import tkinter as tk
import sys
import os
from Classes.Libro import Libro
# Agregar la carpeta raíz del proyecto al PYTHONPATH
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.append(ROOT)

# IMPORTS ABSOLUTOS (estos nunca fallan)
import json

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
    
def guardarEstantes(ListaEstantes):
    """Saves the list of shelves in a JSON"""
    with open ("Estantes.json", "w",encoding = "utf-8") as archivo:
        ListaCargadaEstantes= [estante.objetoDiccionario() for estante in ListaEstantes] #Desde la funcion que convierte objeto a diccionario, es decir los estantes de objeto estante en diccionario
        json.dump(ListaEstantes,archivo, ensure_ascii=False, indent = 4) #la llama y lee cada elemento en ese diccionario y crea una lista de diccionarios y la guarda en un JSON

def guardarHistorialPrestamos(PilaHistorialPrestamos):
    """Saves the borrowed books Pile in a JSON file"""
    with open("Historial Prestamos.json","w",encoding = "utf-8") as archivo:
        json.dump(PilaHistorialPrestamos,archivo, ensure_ascii=False, indent = 4)

def guardarListaEspera(listaEspera):
    """Saves the wait list as a list in a JSON"""
    with open("Lista de Espera.json","w",encoding = "utf-8") as archivo:
        json.dump(listaEspera,archivo, ensure_ascii=False, indent = 4)
