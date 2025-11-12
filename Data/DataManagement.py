from Classes.Libro import Libro
from Classes.Estante import Estante
import json
def guardarInventarioGeneral(InventarioGeneral):
    """Saves the general inventory in a JSON"""
    with open ("InventarioGeneral.json", "w",encoding = "utf-8") as archivo:
        diccionarioLibros = [libro.__dict__ for libro in InventarioGeneral] #convirtiendo las instancias de libro en lista de diccionarios
        json.dump(diccionarioLibros,archivo, ensure_ascii=False, indent = 4) #guardando la lista de diccionarios

def guardarInventarioOrdenado(InventarioGeneral):
    """Saves the ordered inventory in a JSON"""
    with open ("InventarioGeneral.json", "w",encoding = "utf-8") as archivo:
        diccionarioLibros = [libro.__dict__ for libro in InventarioGeneral]
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
