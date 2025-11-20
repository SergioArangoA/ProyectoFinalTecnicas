from Classes.Libro import Libro
from typing import List                 
from collections import deque
from DataManagement import *
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

    inventarioGeneral.append(Libro(isbn, titulo, autor, peso, precio, enInventario, prestados, estantes, listaEspera))


    isbnNuevo =isbn.strip("-")
    insertado=False #Flag Var

    for i in range(len(inventarioOrdenado)):
        isbnExistente= inventarioOrdenado[i].isbn.strip("-")

        if isbnNuevo<isbnExistente:
            inventarioOrdenado.insert(i,Libro)

        if not insertado:
            inventarioOrdenado.append(Libro)
    guardarInventarioGeneral(inventarioGeneral)
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
            if contador==0:
                print("No hay libros relacionados con ese autor")
                return 0
            return pesoPromedio/contador

        LibroActual = inventarioOrdenado[n]

        if LibroActual.autor==autor:
            contador+=1
            pesoPromedio+=LibroActual.precio

        return calculoPesoPromedio(n+1, contador, pesoPromedio)
                                   
    return calculoPesoPromedio(n, contador, pesoPromedio)

