from typing import List                 
from collections import deque
import tkinter as tk
import sys
import os

# Agregar la carpeta raíz del proyecto al PYTHONPATH
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.append(ROOT)

# IMPORTS ABSOLUTOS (estos nunca fallan)
from Data.DataManagement import guardarInventarioGeneral
from Data.DataManagement import guardarInventarioOrdenado
from Classes.Libro import Libro


"""Master Lists of Objects
The two lists of organized Inventory and General Inventory are defined and filled, also makes the recursive stack and pile calls

Methods:
guardarLibro():Calls the Book attributes and creates a Book Object wich is going to be added to the organized inventory in
ascending order and the general inventory after being created

valorTotalAutor(): This function acts as a wrapper for the internal recursive function 'valorTotalMetodo()',
initializing the necessary parameters and starting the exploration from the first item in the inventory

valorTotalMetodo():This method is the recursive technique, calculates the total value of all books written by a specific author

pesoPromedioAutor(): This function acts as a wrapper for the internal recursive function 'calculoPesoPromedio()',
initializing the necessary parameters, variables and starting the exploration from the first item in the inventory

calculoPesoPromedio():This method is the recursive technique, calculates the average weight of a collection of books from a specific author
"""
inventarioGeneral=[]
inventarioOrdenado=[] 

"""List Filling"""

def guardarLibro (isbn: str, titulo: str, autor: str, peso: float, precio: int, enInventario: int, prestados: int, 
    estantes: List[str], listaEspera: deque | None = None): #no se pone self. atributo pq ese self solo existe dentro de la clase libro
    """This method calls the Book attributes and creates a Book Object wich is going to be added to the organized inventory and the general inventory
    after being created"""
    nuevoLibro = Libro(isbn, titulo, autor, peso, precio, enInventario, prestados, estantes, listaEspera)
    inventarioGeneral.append(nuevoLibro)
    #Creates a Book object with all the attributes and adds it to the general inventory

    isbnNuevo =isbn.strip("-")
    insertado=False #Flag Var to know if the book has been already added to the Organized Inventory

    for i in range(len(inventarioOrdenado)): #Goes throught the organized inventory
        isbnExistente= inventarioOrdenado[i].isbn.strip("-") #Extracts de ISBN of the actual Book without hyphens

        if isbnNuevo<isbnExistente: #Compares the ISBN and if the new is less than the older its going to insert the new book on that position
            inventarioOrdenado.insert(i,nuevoLibro)
            insertado = True

        if not insertado: #if the book doesnt match the comparision its gonna be add to the end of the list beacuse is greater than the others
            inventarioOrdenado.append(nuevoLibro)

    guardarInventarioGeneral(inventarioGeneral) #Saves the list
    guardarInventarioOrdenado(inventarioOrdenado)
"""Stack and Tail Recursion"""

"""Stack"""
    #LA VARIABLE AUTOR VIENE DEL FRONTEND Y ES LA QUE DICE QUE AUTOR SE VA A BUSCAR

def valorTotalAutor(listaLibros: List[Libro], autor: str, inventarioOrdenado):
    """This function acts as a wrapper for the internal recursive function, initializing the necessary parameters and starting the exploration from the first item in the inventory"""
    
    def valorTotalMetodo(n):
        """This method is the recursive technique, calculates the total value of all books written by a specific author"""

        if n == len(inventarioOrdenado): 
        #Base case, returns 0 because there are no more book prices to sum, its the end of the Inventory
            return 0

        libroActual = inventarioOrdenado[n]
        #Extracts the Actual Book from the Inventory

        if libroActual.autor == autor:
        #libroActual.autor extracts the author from the object in the Inventory also this if makes the recursive call and sum the valorTotal of the books
            return libroActual.precio + valorTotalMetodo(n + 1)

        return valorTotalMetodo(n + 1)
        #Allows the recursion to continue

    return valorTotalMetodo(0) 
    #Start the recursion from the first book, index 0

"""Tail"""
""""2. Recursión de Cola: Implementar una función recursiva que calcule el Peso Promedio de la colección de un autor, demostrando la lógica de la recursión de cola por consola.
"""

def pesoPromedioAutor(autor: str, inventarioOrdenado):
    """ This function acts as a wrapper for the internal recursive function 'calculoPesoPromedio()',
initializing the necessary parameters, variables and starting the exploration from the first item in the inventory"""
    n=0
    pesoPromedio=0
    contador=0
    def calculoPesoPromedio(n:int, contador:int, pesoPromedio: float):
        """This method is the recursive technique, calculates the average weight of a collection of books from a specific author"""

        if n==len(inventarioOrdenado):
        #Base case, returns the final average sum of the books weights
            if contador==0:
            #If the is counter is zero and the list has reach the end it means that there are no books of that author, returns zero and prints the message
                print("No hay libros relacionados con ese autor")
                return 0
            return pesoPromedio/contador

        LibroActual = inventarioOrdenado[n] 
        #This extracts from the object (in this case named as 'LibroActual') the actual book 

        if LibroActual.autor==autor:
        #It compares the Actual Book Author (.autor) and the author that the user is looking for. If its found adds to the counter one and adds
        # to the weight sum. Returns the recursive call adding to the index 'n' one continuing the recursion
            contador+=1
            pesoPromedio+=LibroActual.peso

        return calculoPesoPromedio(n+1, contador, pesoPromedio)
                                   
    return calculoPesoPromedio(n, contador, pesoPromedio)
    #This allows that the response from 'calculoPesoPromedio' is working on the general code and can be called, else it won't work
    #because the wrapper function is not returning anything

