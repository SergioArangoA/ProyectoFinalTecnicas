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
normalizar():This method helps later to compare strings without Upper case, comma, hyphen and dot

--BOOK RELATED METHODS--
    guardarLibro():This method calls the Book attributes and creates a Book Object (if it doesn't exists) wich is going to be added
    to the organized inventory and the general inventory after being created, if the book exists

    buscarLibro(): This method searches for the book in the inventory and returns the book
    object if it exists. If it does not exist, it returns False so the frontend can
    show the corresponding message

    eliminarLibro(): This method receives the information form the searching function, it means the book exists
    and can be found. Removes the object from the both Master Lists and returns True so the frontend 
    can show a succes message

--SHELF RELATED METHODS--
    guardarEstanteFuncion (): This method calls the shelf attributes and creates a shelf Object wich is going
    to be added to the list of shelves if it doesn't exist after being created. If it exist it would simply don't be added

    estanteriaDeficiente():This algorithm finds and lists all possible combinations of four books that, when their weight in kg is added together,
    exceed a "risk" of 8kg
    
    buscarEstante(): This method searches for a shelf in the list of shelves and returns the shelf
    object if it exists. If it does not exist, it returns False so the frontend can show the corresponding message

    eliminarEstante (): This method receives the information form the searching function, it means the book exists
    and can be found. Removes the object from the both Master Lists and returns True so the frontend 
    can show a succes message

    estanteriaDeficiente(): This algorithm finds and lists all possible combinations of four books that, when their weight in kg is added together, exceed a "risk" of 8kg

 --USER RELATED METHODS--
    guardarUsuarioFuncion(): This method calls the User attributes and creates a User Object wich is going to be added to the Users List after being created
    if it doesn't exists. If the user exists is not going to be added

    buscarUsuario(): This method searches for a User in the list of Users and returns the shelf object if it exists.
    If it does not exist, it returns False so the frontend can show the corresponding message

--RECURSION--
-STACK

valorTotalAutor(): This function acts as a wrapper for the internal recursive function 'valorTotalMetodo()',
initializing the necessary parameters and starting the exploration from the first item in the inventory

valorTotalMetodo():This method is the recursive technique, calculates the total value of all books written by a specific author

-QUEUE
pesoPromedioAutor(): This function acts as a wrapper for the internal recursive function 'calculoPesoPromedio()',
initializing the necessary parameters, variables and starting the exploration from the first item in the inventory

calculoPesoPromedio():This method is the recursive technique, calculates the average weight of a collection of books from a specific author

--SEARCHES--
-LINEAL SEARCH 
    1. AUTHOR
    busquedaPorAutor():This method goes through the general inventory and searches for the asked autor if the author is found is going
    to create a list with all the found books of the same author, if it isn't found returns a empty list or false for each case
    2. TITLE


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

"""BOOKLIST RELATED METHODS"""
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

"""Book searching"""
def buscarLibro(isbn: str):
    """This method searches for the book in the inventory and returns the book
    object if it exists. If it does not exist, it returns False so the frontend can show the corresponding message"""
    from Data.DataManagement import cargarInventarioGeneral

    listalibros = cargarInventarioGeneral()
    isbnBuscado = isbn

    for libro in listalibros:  #Goes through the inventory looking for the book
        if libro.isbn == isbnBuscado:  #Checks if it exists
            return libro  #Returns the shelf object if found
    return False ##Returns false so the frontend can show a message that the book doesn't exist

"""Book deletion"""
def eliminarlibro(isbn: str, cantidad:int):
    """This method receives the information form the searching function, it means the book exists
    and can be found. Removes the object from the both Master Lists and returns True so the frontend can show a succes message"""
    
    from Data.DataManagement import cargarInventarioGeneral
    from Data.DataManagement import cargarInventarioOrdenado

    inventarioGeneral=cargarInventarioGeneral() #Loads inventories
    inventarioOrdenado= cargarInventarioOrdenado()

    libroInventarioGeneral = None
    libroInventarioOrdenado = None

    libroBuscado= buscarLibro(isbn) #Calls the searching method
    print(libroBuscado.enInventario)

    if libroBuscado:
        if libroBuscado.enInventario >= cantidad: #If the quantity to be eliminated fits on the quantity available it will eliminate that quantity
            libroBuscado.enInventario-= cantidad #Eliminates the quantity
            cantidad=0 #The book quantity already been eliminated, there's nothing left, the quantity to be eliminated is zero

        
        
        else: #There are not enough books in the inventory to eliminated
            cantidad-= libroBuscado.enInventario #It substracts the quantity that can be substracted
            libroBuscado.enInventario= 0 #The inventory its zero because all the books has been eliminated

        if cantidad>0:#Still books to eliminate
            if libroBuscado.prestados>= cantidad: #There is no books on the inventory but there are borrowed 
                libroBuscado.prestados-= cantidad #Substracts the quantity from borrowed books
                cantidad=0
            else:
                libroBuscado.prestados=0 #There is no borrowed books
                cantidad=0 #No books will be eliminated
        for libro in inventarioGeneral:
            if libro.isbn == libroBuscado.isbn:
                libroInventarioGeneral = libro
        inventarioGeneral.remove(libroInventarioGeneral)
        guardarInventarioGeneral(inventarioGeneral)

        for libro in inventarioOrdenado:
            if libro.isbn == libroBuscado.isbn:
                libroInventarioOrdenado = libro
        inventarioOrdenado.remove(libroInventarioOrdenado)
        guardarInventarioOrdenado(inventarioOrdenado)
        #This section updates the inventories
        if libroBuscado.enInventario + libroBuscado.prestados > 0:
            guardarLibro(libroBuscado.isbn,libroBuscado.titulo,libroBuscado.autor,libroBuscado.peso,libroBuscado.precio,libroBuscado.enInventario,libroBuscado.prestados,libroBuscado.estantes,libroBuscado.listaEspera)

"""SHELVES RELATED METHODS"""

"""Shelf storage"""
def guardarEstanteFuncion (id:str, librosEnEstante:list): 
    """This method calls the shelf attributes and creates a shelf Object wich is going to be added to the list of shelves if it doesn't exist
    after being created. If it exist it would simply don't be added"""
    from Data.DataManagement import cargarEstantes #The imports are made here to avoid circular imports when initializing the program
    from Data.DataManagement import guardarEstantes
    from Classes.Estante import Estante
    listaEstantes= cargarEstantes()
    idNuevo= id
    
    for estante in listaEstantes: #Goes throught the list of shelves
        if estante.obtenerID()== idNuevo: #checks if the shelf is already in the list if it is, a message will show 
            return False #Returns false so the frontend can show the message that the shelf already exist and has not been added 

    nuevoEstante= Estante(idNuevo, librosEnEstante) #If the shelf doesn't exist creates a new shelf instance with the atributes
    listaEstantes.append(nuevoEstante)#Adds the new object to the list

    guardarEstantes(listaEstantes)#Saves the list in the JSON

    return True #Shelf added

"""Shelf searching"""
def buscarEstante(id: str):
    """This method searches for a shelf in the list of shelves and returns the shelf
    object if it exists. If it does not exist, it returns False so the frontend can
    show the corresponding message"""
    from Data.DataManagement import cargarEstantes

    listaEstantes = cargarEstantes()
    idBuscado = id

    for estante in listaEstantes:  #Goes through the list of shelves looking for the shelf
        if estante.obtenerID() == idBuscado:  #Checks if it exists
            return estante  #Returns the shelf object if found

    return False #Returns false so the frontend can show a message that the shelf does not exist

"""Shelf deletion"""
def eliminarEstante (id: str):
    """This method receives the information form the searching function, it means the book exists
    and can be found. Removes the object from the both Master Lists and returns True so the frontend 
    can show a succes message """
    from Data.DataManagement import cargarEstantes, guardarEstantes
    from Data.DataManagement import cargarInventarioGeneral, guardarInventarioGeneral
    from Data.DataManagement import cargarInventarioOrdenado, guardarInventarioOrdenado

    listaEstantes= cargarEstantes()
    inventarioGeneral=cargarInventarioGeneral()
    inventarioOrdenado= cargarInventarioOrdenado()

    idEstanteEliminar= id
    estanteBuscado= buscarEstante(idEstanteEliminar) 
    if estanteBuscado:
        listaEstantes.remove(estanteBuscado)

    #Updates each Book Object by removing the shelf ID from its 'estantes' attribute
    for libro in inventarioGeneral: #For each book in the general inventory
        if idEstanteEliminar in libro.estantes: #Checks if the shelf ID to be deleted exists in the current book's 'estantes' attribute.
        #'libro.estantes' is a list of IDs representing the shelves where this book is stored.
            libro.estantes.remove(idEstanteEliminar) #Removes the shelf
    
    for libro in cargarInventarioOrdenado: #For each book in the organized inventory
        if idEstanteEliminar in libro.estantes:
            libro.estantes.remove(idEstanteEliminar)
    
    guardarEstantes(listaEstantes) #Saves
    guardarInventarioGeneral(inventarioGeneral)
    guardarInventarioOrdenado(inventarioOrdenado)

    return True  #Returns True so the frontend can show a message that the shelf was successfully deleted

"""Shelf Module"""

"""1. Brute force"""
def estanteriaDeficiente(inventarioOrdenado):
    """This algorithm finds and lists all possible combinations of four books that, when their weight in kg is added together, exceed a "risk" of 8kg"""
    listaLibrosEstanteriaDeficiente=[]
    #This list stores all the 4 books combinations that exceeds the 8kg risk
    
    for Libro1 in inventarioOrdenado: #A For for each book in the shelf (4)
        for Libro2 in inventarioOrdenado:
            for Libro3 in inventarioOrdenado:
                for Libro4 in inventarioOrdenado:
                    if Libro1.enInventario>0 and Libro2.enInventario>0 and Libro3.enInventario>0 and Libro4.enInventario>0:
                        #Verifies that the four books are available in the inventory
                        
                        if Libro1.peso+Libro2.peso+Libro3.peso+Libro4>8:
                            #If sum of the weights is above eight the books are added as a list in 'listaLibrosEstanteriaDeficiente'

                            listaLibrosEstanteriaDeficiente.append([Libro1,Libro2,Libro3,Libro4])      
                                                 
    if len(listaLibrosEstanteriaDeficiente) == 0: #If the cycles are done and the final lenght of store list is zero it means that there are'nt enough books 
        return "No hay suficientes libros" #This messaje shows on the open window 'ventanaEstanterias'
    return listaLibrosEstanteriaDeficiente #Returns the final list

"""USER RELATED METHODS"""
"""User List filling"""

def guardarUsuarioFuncion (id:str, historialPrestados:deque): 
    """This method calls the User attributes and creates a User Object wich is going to be added to the Users List after being created
    if it doesn't exists. If the user exists is not going to be added"""
    from Data.DataManagement import cargarUsuarios
    from Data.DataManagement import guardarUsuarios
    from Classes.Usuario import Usuario

    listaUsuarios = cargarUsuarios()
    idNuevo= id
    
    for usuario in listaUsuarios: #Goes throught the list of Users
        if usuario.id == idNuevo: #checks if the user is already in the list if it is, a message will show 
            return False #Returns false so the frontend can show the message that the User already exist and has not been added 

    nuevoUsuario= Usuario(id, historialPrestados) #If the User doesn't exist creates a new User instance with the atributes
    listaUsuarios.append(nuevoUsuario)#Adds the new object to the list

    guardarUsuarios(listaUsuarios)#Saves the list in the JSON

    return True #User added

"""User searching"""
def buscarUsuario(id: str):
    """This method searches for a User in the list of Users and returns the shelf object if it exists.
    If it does not exist, it returns False so the frontend can show the corresponding message"""
    from Data.DataManagement import cargarUsuarios

    listaUsuarios = cargarUsuarios()
    idBuscado = id

    for usuario in listaUsuarios:  #Goes through the list of Users looking for the right User
        if usuario.id == idBuscado:  #Checks if it exists
            return usuario  #Returns the shelf object if found
        
    return False #Returns false so the frontend can show a message that the shelf does not exist

def eliminarUsuario(id: str):
    """
    Recibe el ID de un usuario y lo elimina de la lista de usuarios.
    Mantiene las instancias de memoria correctas al modificar la lista cargada.
    Devuelve True si se eliminó correctamente, False si el usuario no existe.
    """
    from Data.DataManagement import cargarUsuarios, guardarUsuarios

    listaUsuarios = cargarUsuarios()

    usuarioBuscado = None #Inicializates the var who is going to keep the found user
    for usuario in listaUsuarios: #Goes throught the user list
        if usuario.id == id: #If anyone of the id users is the same as the one the program is looking for
            usuarioBuscado = usuario  #Saves the searched 
            break  #The user has been found 

    if usuarioBuscado: #verifies is the user has been found
        listaUsuarios.remove(usuarioBuscado)  #Eliminates from the list the same instance from the found user assuring the delete of the right object
        guardarUsuarios(listaUsuarios)  #List save
        return True  #The user has been succesfully eliminated
    else:
        return False  #The user is not in the list

"""Stack and Queue Recursion"""

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

"""Queue"""

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

"""SEARCHES"""
"Lineal Search"
"AUTHOR"
    
def busquedaPorAutor(autor:str,librosAutor =[],  n=0):
    """This method goes through the general inventory and searches for the asked autor if the author is found is going
    to create a list with all the found books of the same author, if it isn't found returns a empty list or false for each case"""
    inventarioGeneral= cargarInventarioGeneral()

    if librosAutor is None: 
        librosAutor=[]

    if n>= len(inventarioGeneral):
        if librosAutor:
            return librosAutor
        else:
            return False
    
    if inventarioGeneral[n].autor== autor:
        librosAutor.append(inventarioGeneral[n])

    return busquedaPorAutor(autor,librosAutor,n+1 )

def busquedaporTitulo(titulo:str, librosTitulo=[], n=0):
    """This method goes through the general inventory and searches for the asked title if the title is found is going
    to create a list with all the found books of the same title, if it isn't found returns a empty list or false for each case"""
    inventarioGeneral= cargarInventarioGeneral()

    if librosTitulo is None: 
        librosTitulo=[]

    if n>= len(inventarioGeneral):
        if librosTitulo:
            return librosTitulo
        else:
            return False
    
    if inventarioGeneral[n].titulo== titulo:
        librosTitulo.append(inventarioGeneral[n])

    return busquedaporTitulo(titulo,librosTitulo,n+1 )
