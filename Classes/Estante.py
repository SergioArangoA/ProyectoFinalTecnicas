import tkinter as tk
import sys
import os

# Agregar la carpeta raíz del proyecto al PYTHONPATH
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.append(ROOT)

from Classes import Libro
class Estante:
    """An Estante instance represents a book shelf in the library.
    
    Atributes:
    id(private str): Stand's id
    books(Books list [size 4])

    Methods:
    estanteDeficiente(): Checks the inventory, and looks for all the possible combinations of 
    4 books that aren't already in a stand and exceeds the 8kg weight limit.

    ObtenerID(): Returns the Id attribute

    SacarID (): Allows modifying the ID

    estanteOptimo(): Finds all the combinations of books that can be placed in the stand without
    exceeding the 8kg weight limit. It'll also search for the one that will have the highest
    combined value in COP. It will also print in console the proccess.

    objetoDiccionario(): This Method transform the object shelf to a dictionary

    diccionarioObjeto(): Transforms dictionary to object shelf
    """
    
    def __init__(self, id: str, librosEnEstante: list["Libro"]):
        self.__id = id #__id, quiere decir que la variable es privada. Es decir, que no
        #puedes acceder a ella directamente. Esto lo hago, para que al cambiar el nombre
        #del stand, se puedan actualizar de inmediato en los libros del stand el nuevo
        #nombre del stand, así evitaremos errores más adelante
        self.librosEnEstante = librosEnEstante
        self.libroEnEstante: list[bool]= [] #Ask if the book in that position is on the shelf: if true that book is on the shelf, if false it's loaned out/borrowed
        
    def obtenerID(self):
        """This method returns the Id attribute"""
        return self.__id 
    
    def modificarID(self, nuevaID ):
        """This method allows to modifying the Id"""
        self.__id= nuevaID

    def objetoDiccionario(self):
        """Transforms the object shelf to a dictionary"""
        return({"id": self.obtenerID(), "librosEnEstante": self.librosEnEstante})
    
    @classmethod #The method belongs to the class, not to an existing object.
    def diccionarioObjeto(clsEstante, diccionarioEstante):
        """Transforms dictionary to object shelf"""
        return clsEstante(diccionarioEstante["id"], diccionarioEstante["librosEnEstante"])
    
    def obtenerPesoAcumulado(self):
        """Adds the total weight of all the books in the stand"""
        total = 0
        for libro in self.librosEnEstante:
            total += libro.peso
        return total
    
    def obtenerCantidadDeLibros(self):
        """Returns the amount of books inside the stand"""
        return len(self.librosEnEstante)
    

    
