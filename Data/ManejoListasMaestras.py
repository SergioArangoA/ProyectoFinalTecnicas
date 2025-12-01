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
from Data.DataManagement import cargarInventarioGeneral
from Data.DataManagement import cargarInventarioOrdenado
from Classes.Libro import Libro


"""Master Lists of Objects
The two lists of organized Inventory and General Inventory are defined and filled, also makes the recursive stack, pile calls and other
main functions for the program

Methods:
guardarLibro():This method calls the Book attributes and creates a Book Object (if it doesn't exists) wich is going to be added
to the organized inventory and the general inventory after being created, if the book exists

valorTotalAutor(): This function acts as a wrapper for the internal recursive function 'valorTotalMetodo()',
initializing the necessary parameters and starting the exploration from the first item in the inventory

valorTotalMetodo():This method is the recursive technique, calculates the total value of all books written by a specific author

pesoPromedioAutor(): This function acts as a wrapper for the internal recursive function 'calculoPesoPromedio()',
initializing the necessary parameters, variables and starting the exploration from the first item in the inventory

calculoPesoPromedio():This method is the recursive technique, calculates the average weight of a collection of books from a specific author

funcionLlamar(): Bridge function for the frontend. Internally calls pesoPromedioAutor by sending 'normalizar', 
Its like a wrapper for the wrapper function
"""
inventarioOrdenado=cargarInventarioOrdenado
inventarioGeneral=cargarInventarioGeneral
def normalizar(cadena):
    """This method helps later to compare strings without Upper case, comma, hyphen and dot"""
    cadena= cadena.lower()            #Convert to lower case
    cadena= cadena.replace(" ", "")   #Remove Space
    cadena= cadena.replace("-", "")   #Remove Hyphen 
    cadena= cadena.replace(".", "")   #Remove dot
    return cadena

"""List Filling"""
#CANTIDAD VIENE DEL FRONTEND PREGUNTA CUANTOS LIBROS VA A AGREGAR Y SE LOS AGREGA AL ATRIBUTO DEL LIBRO 'EN INVENTARIO'
def guardarLibro(isbn: str, titulo: str, autor: str, peso: float, precio: int, cantidad: int, prestados: int, 
    estantes: List[str], listaEspera: deque | None = None): #no se pone self. atributo pq ese self solo existe dentro de la clase libro
    """This method calls the Book attributes and creates a Book Object wich is going to be added to the organized inventory and the general inventory
    after being created"""
    inventarioGeneral = cargarInventarioGeneral()
    inventarioOrdenado = cargarInventarioOrdenado()

    isbnNuevo =isbn.strip("-")
    

    for libro in inventarioGeneral: #Goes throught the general inventory
        if libro.isbn.strip("-")== isbnNuevo and cantidad>0: #checks if the book is already in the inventory if it is, ask how many of the same book are gonna be added
            libro.enInventario+= cantidad #If the book exists it just going to update the amount of books
            guardarInventarioGeneral(inventarioGeneral)
            guardarInventarioOrdenado(inventarioOrdenado)
            return True #Returns true so the frontend can show the message that the book already exist and has been updated 
        
        elif  cantidad<0:
            return False #Returns False so the frontend can show a message that the amount entered is not valid
        
    #If the book doesn't exists, creates a new instance, Creates a Book object with all the attributes and adds it to the general inventory
    nuevoLibro= Libro(isbn, titulo, autor, peso, precio, cantidad, prestados, estantes, listaEspera)
    inventarioGeneral.append(nuevoLibro)


    nuevoLibro.enInventario= cantidad #Initialize the correct amount of books that the user entered

    insertado=False #Flag Var to know if the book has been already added to the Organized Inventory

    for i in range(len(inventarioOrdenado)):#goes throught the organized inventory to fill it 
        libro= inventarioOrdenado[i] 
        if isbnNuevo< libro.isbn.strip("-"):#This action is the one that allows the books to be organized
            inventarioOrdenado.insert(i, nuevoLibro)#this inserts the book in the correct position
            insertado= True #the book has been inserted
            break

    if not insertado: #if the book doesnt match the comparision its gonna be add to the end of the list beacuse is greater than the others
        inventarioOrdenado.append(nuevoLibro)

    guardarInventarioGeneral(inventarioGeneral) #Saves the list
    guardarInventarioOrdenado(inventarioOrdenado)

"""Stack and Tail Recursion"""

"""Stack"""
    #LA VARIABLE AUTOR VIENE DEL FRONTEND Y ES LA QUE DICE QUE AUTOR SE VA A BUSCAR

def valorTotalAutor(autor: str, inventarioOrdenado):
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

def pesoPromedioAutor(autor: str, inventarioOrdenado, normalizar):
    """ This function acts as a wrapper for the internal recursive function 'calculoPesoPromedio()',
initializing the necessary parameters, variables and starting the exploration from the first item in the inventory"""

    n=0
    pesoPromedio=0
    contador=0
    def calculoPesoPromedio(n:int, contador:int, pesoPromedio: float, normalizar):
        """This method is the recursive technique, calculates the average weight of a collection of books from a specific author"""

        if n==len(inventarioOrdenado):
        #Base case, returns the final average sum of the books weights
            if contador== 0:
            #If the is counter is zero and the list has reach the end it means that there are no books of that author, returns zero and prints the message
                print("No hay libros relacionados con ese autor")
                return 0
            return pesoPromedio/contador

        LibroActual = inventarioOrdenado[n] 
        #This extracts from the object (in this case named as 'LibroActual') the actual book 

        if normalizar(LibroActual.autor)==normalizar(autor):
        #It compares the Actual Book Author (.autor) and the author that the user is looking for. If its found adds to the counter one and adds
        # to the weight sum. Returns the recursive call adding to the index 'n' one continuing the recursion
            contador+= 1
            pesoPromedio+= LibroActual.peso

            print("Indice(n)= "+ str(n)+"\n"+ "Contador= "+ str(contador)+"\n"+ "Suma Actual Peso promedio= "+ str(pesoPromedio))
        return calculoPesoPromedio(n+1, contador, pesoPromedio, normalizar)
                                   
    return calculoPesoPromedio(n, contador, pesoPromedio, normalizar)

def funcionLlamar(autor, inventarioOrdenado):
    """Bridge function for the frontend. Internally calls pesoPromedioAutor by sending normalizar, Its like a wrapper for the wrapper function"""
    return pesoPromedioAutor(autor, inventarioOrdenado, normalizar) 

#peso = pesoPromedioAutor(autor, inventarioOrdenado, normalizar)
#print("\n")
#print("Peso Promedio = " + str(peso))
    #This allows that the response from 'calculoPesoPromedio' is working on the general code and can be called, else it won't work
    #because the wrapper function is not returning anything
