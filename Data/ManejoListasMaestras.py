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
    guardarLibro() (INSERTION SORT):This method calls the Book attributes and creates a Book Object (if it doesn't exists) wich is going to be added
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

    modificarEstante():Searches a shelf in the shelf list, and then modifies its id

    agregarLibroEstante(): Add a book to a shelf without checking for duplicates, without modifying inventory or loans. 
    Check that the shelf exists and that there are books in inventory; 
    return True if it was added, False if not (shelf does not exist or there is nothing on the inventory)

    eliminarLibroEstante(): Removes a book from a specific shelf, also removing the shelf from 'libro.estantes.' Doesn't modify inventory or borrowed books. 
    Returns True if it was removed, False if not (shelf does not exist or book is not on it)

    --SHELF MODULE--
        1. Brute Force
            estanteriaDeficiente(): This algorithm finds and lists all possible combinations of four books that, when their weight in kg is added together, exceed a "risk" of 8kg
        2. Backtracking
            funcion ():This method acts as a wrapper function to prepare the enviroment for the backtracking initializating
            fundamental variables and lists

            backtracking():This method is the backtracking it finds the combination of books from the inventory that maximizes the total price
            without exceeding 8kg. It recursively explores all possible combinations, taking into account the available copies 
            'enInventario' of each book it doesn't count the borrowed books.
            At the end, it displays the optimal combinations and returns them

    
 --USER RELATED METHODS--
    guardarUsuarioFuncion(): This method calls the User attributes and creates a User Object wich is going to be added to the Users List after being created
    if it doesn't exists. If the user exists is not going to be added

    buscarUsuario(): This method searches for a User in the list of Users and returns the shelf object if it exists.
    If it does not exist, it returns False so the frontend can show the corresponding message

    eliminarUsuario(): Receives a user's ID and removes them from the user list.
    Maintains correct memory references when modifying the loaded list.
    Returns True if the user was successfully removed, False if the user does not exist.

    modificarUsuario(): Searches a user in the users list, and then modifies its id

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
            busquedaPorAutor():This method goes through the general inventory and searches (RECURSIVE METHOD) for the asked autor if the author is found is going
            to create a list with all the found books of the same author, if it isn't found returns a empty list or false for each case
        2. TITLE
            busquedaporTitulo():This method goes through the general inventory and searches (RECURSIVE METHOD) for the asked title if the title is found is going
            to create a list with all the found books of the same title, if it isn't found returns a empty list or false for each case

    -BINARY SEARCH
        busquedaBinISBN():This algorithm searches for the book's ISBN in the sorted inventory. 
        According to binary search, if the ISBN being searched for is equal to the ISBN in the middle of the sorted inventory, 
        it returns the position of that middle ISBN. 
        If the ISBN is less than the one being searched for, it moves through the inventory to the right,
        meaning the ascending part; if greater, it moves to the left, the descending part, and if it doesn't find anything, it returns -1, meaning the book was not found

--MERGE SORT--
    reporteGlobal(): This method is the MERGE SORT recursion part, this divides the general inventory list in two lists and it runs until the base case is met,
    it means when the list has only one element, and then it calls the 'mezclado' method that organizes the data

    mezclado(): This method is the MERGE SORT organization part, Sort in ascending order by the value (COP) of the books from the previously divided lists
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
"""(INSERTION SORT)"""
def guardarLibro(isbn: str, titulo: str, autor: str, peso: float, precio: int, cantidad: int, prestados: int, 
    estantes: List[str], listaEspera: deque | None = None): #no se pone self. atributo pq ese self solo existe dentro de la clase libro
    """This method calls the Book attributes and creates a Book Object wich is going to be added to the organized inventory and the general inventory
    after being created"""
    inventarioGeneral = cargarInventarioGeneral()
    inventarioOrdenado = cargarInventarioOrdenado()

    isbnNuevo =isbn.strip("-")
    

    for libro in inventarioGeneral: #Goes throught the general inventory
        if libro.isbn.strip("-")== isbnNuevo and cantidad>=0: #checks if the book is already in the inventory if it is, ask how many of the same book are gonna be added
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

    libroBuscado= buscarLibro(isbn) #Call the search function to get the book object

    if libroBuscado: #First, remove quantity from inventory if enough stock is available
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

        for libro in inventarioGeneral: #Update the book data in the general inventory
            if libro.isbn == libroBuscado.isbn: #finds matching book
                libro.enInventario = libroBuscado.enInventario #updates the inventory count
                libro.prestados = libroBuscado.prestados #update borrowed count
                break #exit loop once the book is found
        guardarInventarioGeneral(inventarioGeneral)

        for libro in inventarioOrdenado: #updates the data in arranged inventory
            if libro.isbn == libroBuscado.isbn:
                libro.enInventario = libroBuscado.enInventario
                libro.prestados = libroBuscado.prestados
        guardarInventarioOrdenado(inventarioOrdenado)
 
        if libroBuscado.enInventario + libroBuscado.prestados <= 0:#If total copies (inventory + borrowed) is zero, remove the book entirely

            for libro in inventarioGeneral: #Remove from general inventory
                if libro.isbn == libroBuscado.isbn:
                    libroInventarioGeneral = libro
                    break
            inventarioGeneral.remove(libroInventarioGeneral) #removes
            guardarInventarioGeneral(inventarioGeneral) #saves

            for libro in inventarioOrdenado: #remove for organized inventory
                if libro.isbn == libroBuscado.isbn:
                    libroInventarioOrdenado = libro
                    break
            inventarioOrdenado.remove(libroInventarioOrdenado)
            guardarInventarioOrdenado(inventarioOrdenado)



def modificarLibro(ISBNanterior: str,isbn: str, titulo: str, autor: str, peso: float, precio: int, enInventario: int, prestados: int,listaEspera = None):
    """This method updates the data of a book, by removing it from both inventories then re-adding it with the new atributes"""
    from Data.DataManagement import cargarInventarioGeneral
    from Data.DataManagement import cargarInventarioOrdenado

    inventarioGeneral=cargarInventarioGeneral() #Loads inventories
    inventarioOrdenado= cargarInventarioOrdenado()
    indice = busquedaBinISBN(inventarioOrdenado,ISBNanterior) #Call the search function to find the book by its old ISBN
    libroBuscado = inventarioOrdenado[indice] 
    
    if isbn:
        libroBuscado.isbn = isbn

    if titulo:
        libroBuscado.titulo = titulo

    if autor:
        libroBuscado.autor = autor
    
    if precio:
        libroBuscado.precio = precio

    if peso:
        libroBuscado.peso = peso

    if enInventario:
        libroBuscado.enInventario = enInventario

    if prestados:
        libroBuscado.prestados = prestados
        
    if listaEspera:
        libroBuscado.listaEspera = listaEspera

    for i in range(0,len(inventarioGeneral)): #Loop to find the index of the book in general inventory
        if inventarioGeneral[i].isbn.strip("-") == ISBNanterior.strip("-"):
            print(str(inventarioGeneral[i].precio))
            print(str(libroBuscado.precio))
            inventarioGeneral[i] = libroBuscado
            print(str(inventarioGeneral[i].precio)) #Replaces the book
            break
    guardarInventarioGeneral(inventarioGeneral) #Saves the general inventory
    indiceInventarioOrdenado = 0
    for i in range(0,len(inventarioOrdenado)): #Loop to find the index of the book in general inventory
        if inventarioOrdenado[i].isbn.strip("-") == ISBNanterior.strip("-"):
            indiceInventarioOrdenado = i #Saves the index
            break
    del inventarioOrdenado[indiceInventarioOrdenado] #Removes the book from the ordered inventory
    insertado=False #Flag Var to know if the book has been already added to the Organized Inventory

    for i in range(len(inventarioOrdenado)):#goes throught the organized inventory to fill it 
        libro= inventarioOrdenado[i] 
        if libroBuscado.isbn.strip("-") < libro.isbn.strip("-"):#This action is the one that allows the books to be organized
            inventarioOrdenado.insert(i, libroBuscado)#this inserts the book in the correct position
            insertado= True #the book has been inserted
            break

    if not insertado: #if the book doesnt match the comparision its gonna be add to the end of the list beacuse is greater than the others
        inventarioOrdenado.append(libroBuscado)
    guardarInventarioOrdenado(inventarioOrdenado)


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

    listaEstantes= cargarEstantes() #Loads the shelf list
    inventarioGeneral=cargarInventarioGeneral()
    inventarioOrdenado= cargarInventarioOrdenado()
    estanteBuscado = None

    idEstanteEliminar= id
    for estante in listaEstantes: #goes through the shelf list
        if estante.obtenerID() == idEstanteEliminar: #If one of the shelves id is the same as the one we are looking to eliminate
            estanteBuscado = estante #The shelf to be eliminated is the same as that shelf
            break #already found the shelf so no sense to continue going thought the list
    listaEstantes.remove(estanteBuscado) #removes the sehlf

    #Updates each Book Object by removing the shelf ID from its 'estantes' attribute
    for libro in inventarioGeneral: 
        libro.estantes = [estante for estante in libro.estantes if estante.obtenerID() != idEstanteEliminar]
         #Creates a new list that adds the shelf only if its ID is different from the one that was deleted
    
    guardarEstantes(listaEstantes) #Saves
    guardarInventarioGeneral(inventarioGeneral)
    guardarInventarioOrdenado(inventarioOrdenado)

    return True  #Returns True so the frontend can show a message that the shelf was successfully deleted

"""Shelf modification"""
def modificarEstante(viejoID: str, nuevoID: str):
    """Searches a shelf in the shelf list, and then modifies its id"""
    from Data.DataManagement import cargarEstantes
    from Data.DataManagement import guardarEstantes

    listaEstantes = cargarEstantes() #Loads the shelfList

    for estante in listaEstantes: #Loop through each shelf in the list to find the one with the old ID
        if estante.obtenerID() == viejoID: #Check if the current shelf has the old ID
            estante.modificarID(nuevoID) #Updates
            break
    guardarEstantes(listaEstantes) #saves

"""Add book to a shelf"""
def agregarLibroEstante(libro, idEstante, listaEstantes):
    """Add a book to a shelf without checking for duplicates, without modifying inventory or loans. 
    Check that the shelf exists and that there are books in inventory; 
    return True if it was added, False if not (shelf does not exist or there is nothing on the inventory)
    """
    from Data.DataManagement import cargarEstantes  # Importar para cargar la lista si no se pasa, pero se asume que se pasa
    from Data.DataManagement import guardarEstantes
    listaEstantes= cargarEstantes()
    #estanteDestino: It is the shelf object to which you want to add the book
    #librosEnEstante: It is a list within the Shelf object that contains all the books that are on that shelf

    if libro.enInventario<= 0: #Verifies that there is books on the inventory
        return False #If there are no books returns false so the frontend can show a message

    estanteDestino= None 
    for estante in listaEstantes: #Goes through the shelves list to look for the shelf
        if str(estante.obtenerID())== str(idEstante): #Converts the comparision to str just in case
            #If the shelf id is the same as the one we are going to add the book rewrites the destiny shelf and breaks the loop
            estanteDestino= estante
            break

    if estanteDestino is None: #if the shelf doesn't exist return false so the frontend can show a message
        return False
    
    estanteDestino.librosEnEstante.append(libro) #Adds the book to the shelf without verifying for duplicates
    libro.estantes.append(estanteDestino.obtenerID()) #Adds the shelf id to the book

    guardarEstantes(listaEstantes)
    modificarLibro(libro.isbn, libro.titulo, libro.autor, libro.peso, libro.precio, libro.enInventario, libro.prestados, 
    libro.listaEspera, libro.estantes)
    return True #The book has been succesfully added

"""Eliminate Book form a shelf"""
def eliminarLibroEstante(libro, estanteID, listaEstantes):
    """Removes a book from a specific shelf, also removing the shelf from 'libro.estantes.' Doesn't modify inventory or borrowed books. 
    Returns True if it was removed, False if not (shelf does not exist or book is not on it)
    """
    from Data.DataManagement import cargarEstantes
    from Data.DataManagement import guardarEstantes
    
    listaEstantes = cargarEstantes()

    estanteDestino = None
    for estante in listaEstantes: #Goes through the shelves list to look for the shelf
        if estante.obtenerID() == estanteID:
            estanteDestino = estante
            break

    if estanteDestino is None: #if the shelf doesn't exists
        return False

    if libro not in estanteDestino.librosEnEstante: #If the book isn't in the shelf
        return False
    
    estanteDestino.librosEnEstante.remove(libro) #Removes the book from the shelf

    if estanteID in libro.estantes: #Eliminates the book just once only if is duplicated
        libro.estantes.remove(estanteID)

    guardarEstantes(listaEstantes)
    modificarLibro(libro.isbn, libro.titulo, libro.autor, libro.peso, libro.precio, libro.enInventario, libro.prestados, 
    libro.listaEspera, libro.estantes)
    return True


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
                    if Libro1.peso + Libro2.peso + Libro3.peso + Libro4.peso > 8:
                        #Verifies that the four books weight is over 8kg
                        listaLibrosEstanteriaDeficiente.append([Libro1,Libro2,Libro3,Libro4])      
                                                 
    if len(listaLibrosEstanteriaDeficiente) == 0: #If the cycles are done and the final lenght of store list is zero it means that there are'nt enough books 
        return "No hay suficientes libros" #This messaje shows on the open window 'ventanaEstanterias'
    return listaLibrosEstanteriaDeficiente #Returns the final list

"""2. Backtracking"""
def funcion (inventarioOrdenado): #The opcions will came from the arranged inventory
    """This method acts as a wrapper function to prepare the enviroment for the backtracking initializating
    fundamental variables and lists"""
    maximo=8 #Max weight allowed for shelf
    combinacionesMaximizadas=[] #The final result of the backtracking
    mejorPrecioGlobal= [0] #This is created because we need a mutable int, so if we just put an int any change inside the function would not be reflected outside because integers in Python are immutable
    #This is necessary because we want to compare the price of the current combination with the best global price found so far, within all the recursive calls.

    def backtracking(combinacion, mejorCombinacion, indice):
        """This method is the backtracking it finds the combination of books from the inventory that maximizes the total price
        without exceeding 8kg. It recursively explores all possible combinations, taking into account the available copies 
        'enInventario' of each book it doesn't count the borrowed books.
        At the end, it displays the optimal combinations and returns them"""
        #'Combinacion' is a Temporary list that keeps track of the books we are currently trying
        #mejorCombinacione List that stores the best combination found so far

        precioCombinacion = sum(libro.precio for libro in combinacion) #sum of the price of all the books in the current combination
        sumaActual= sum(libro.peso for libro in combinacion) #sum of the weights of all the books in the current combination

        print("\nCombinación actual:", [libro.titulo for libro in combinacion], 
        "| Peso:", round(sumaActual,3), "| Precio:", precioCombinacion)

        if sumaActual > maximo:#If the total weight of the current combination exceeds the maximum, it doesn't make sense to keep adding books
            print("Se pasa del peso, backtrack")
            return
        
        if precioCombinacion> mejorPrecioGlobal[0]: #If the price from the actual combination is greater than the best one
            mejorCombinacion[:]=combinacion[:] #We copy all the elements from the list we need them to be the exact same list
            mejorPrecioGlobal[0] = precioCombinacion #Updates the best price founded
            combinacionesMaximizadas[:] = [combinacion.copy()] #We save the best combination found on the final result and rewrite over the previous element
        
        for i in range(indice, len(inventarioOrdenado)): #Goes throught the arranged list
            libro= inventarioOrdenado[i] #Brings the actual book

            if libro.enInventario>0: #if there is books 
                combinacion.append(libro) #Adds the book to the combination 
                libro.enInventario-=1 #we keep a copy of the book

                backtracking(combinacion, mejorCombinacion, i) #Recursive call

                libro.enInventario+=1 #When backtracking, we return the copy to the inventory and remove it from the combination
                combinacion.pop() #Backtrack
                print("Se hace Backtrack:", [libro.titulo for libro in combinacion])

    backtracking([],[],0) #Assures strarting with a empty combination and an empty initial combination

    print("\nCombinaciones máximas encontradas:")  #Prints all the combinations found
    for combinacion in combinacionesMaximizadas:
        print([libro.titulo for libro in combinacion]) #Prints the title because the isbn is feo


    if combinacionesMaximizadas:  #varifies that there is at leats one combination
        mejor_combinacion = combinacionesMaximizadas[-1]  # last combination saved= the best one
        print("\nMejor combinación encontrada:") #prints the best combination
        print([libro.titulo for libro in mejor_combinacion])

    if len(combinacionesMaximizadas) > 0: #returns the best combination if there are any
        return combinacionesMaximizadas[-1]  #returns the best combination to the frontend
        #[-1] is used because in the current implementation, combinacionesMaximizadas is being overwritten every time a better combination is found.
        #And the rewriting assures that the last combination in 'combinacionesMaximizadas' is already the best one
    return []  #Returns an empty list if there is no best combination

resultadoBacktracking=funcion(inventarioOrdenado)


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
            return usuario  #Returns the user object if found
        
    return False

"""User deletion"""
def eliminarUsuario(id: str):
    """Receives a user's ID and removes them from the user list.
    Maintains correct memory references when modifying the loaded list.
    """
    from Data.DataManagement import cargarUsuarios, guardarUsuarios

    listaUsuarios = cargarUsuarios()

    posicionUsuarioBuscado = None #Inicializates the var who is going to keep the position of the found user
    for i in range (0,len(listaUsuarios)): #Goes throught the user list
        if listaUsuarios[i].id == id: #If anyone of the id users is the same as the one the program is looking for
            posicionUsuarioBuscado = i  #Saves the position
            break  #The user has been found 
    del listaUsuarios[posicionUsuarioBuscado]
    guardarUsuarios(listaUsuarios) #Saves the user list once the one searched has been deleted

def modificarUsuario(viejoID: str, nuevoID: str,historialReservas = None):
    """Searches a user in the users list, and then modifies their data"""
    from Data.DataManagement import cargarUsuarios
    from Data.DataManagement import guardarUsuarios

    listaUsuarios = cargarUsuarios()  #Loads the users list
    for usuario in listaUsuarios:
        if usuario.id == viejoID:
            usuario.id = nuevoID  #Updates the user ID
            if historialReservas:
                usuario.historialPrestados = historialReservas #If there was a change made to the reservation history, updates it 
            
            break
    guardarUsuarios(listaUsuarios)  #Saves the modified list

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
"""Lineal Search"""
"""AUTHOR"""
    
def busquedaPorAutor(autor:str,librosAutor =[],  n=0):
    """This method goes through the general inventory and searches (RECURSIVE METHOD) for the asked autor if the author is found is going
    to create a list with all the found books of the same author, if it isn't found returns a empty list or false for each case"""
    inventarioGeneral= cargarInventarioGeneral() #Loads the inventory

    if librosAutor is None: #If 'librosAutor' is nothing, its going to be an empty list
        librosAutor=[]
 
    if n>= len(inventarioGeneral): #The index reached the end of the list
        if librosAutor: #If 'librosAutor' has something
            return librosAutor
        else:
            return False #'librosAutor' doesn't have anything
    
    if inventarioGeneral[n].autor== autor: #the author has been found
        librosAutor.append(inventarioGeneral[n]) #Adds it to the list of books with the same author

    return busquedaPorAutor(autor,librosAutor,n+1 ) #Recursive call

"""TITLE"""

def busquedaporTitulo(titulo:str, librosTitulo=[], n=0):
    """This method goes through the general inventory and searches (RECURSIVE METHOD) for the asked title if the title is found is going
    to create a list with all the found books of the same title, if it isn't found returns a empty list or false for each case"""
    inventarioGeneral= cargarInventarioGeneral() #Loads the inventory

    if librosTitulo is None: #If 'librosTitulo' is nothing, its going to be an empty list
        librosTitulo=[]

    if n>= len(inventarioGeneral):#The index reached the end of the list
        if librosTitulo:#If 'librosTitulo' has something
            return librosTitulo
        else:
            return False #'librosTitulo' doesn't have anything
    
    if inventarioGeneral[n].titulo== titulo: #the title has been found
        librosTitulo.append(inventarioGeneral[n]) #Adds it to the list of books with the same title

    return busquedaporTitulo(titulo,librosTitulo,n+1 ) #Recursive call

"""Binary Search"""
def busquedaBinISBN(inventarioOrdenado, isbnBuscado:str):
    """This algorithm searches for the book's ISBN in the sorted inventory. 
    According to binary search, if the ISBN being searched for is equal to the ISBN in the middle of the sorted inventory, 
    it returns the position of that middle ISBN. 
    If the ISBN is less than the one being searched for, it moves through the inventory to the right,
    meaning the ascending part; if greater, it moves to the left, the descending part, and if it doesn't find anything, it returns -1, meaning the book was not found."""
    inicio=0
    final=len(inventarioOrdenado)-1
    
    while inicio<= final: #mientras que se recorra correctamente el ciclo
        mitad=(inicio+final)//2 #Half MUST be an integer and it can't be done with the length of the list because that will never change. Each iteration must take the current range, not that of the whole list.
        isbnAct= inventarioOrdenado[mitad].isbn #The current ISBN will be whatever ISBN that is in the middle of the inventory

        if isbnAct== isbnBuscado: #If the current ISBN is the same as the one in the middle, then it returns it
            return mitad #returns THE POSITION, because in this case the data doesn't matter, but the point at which it changes does
        
        elif isbnAct< isbnBuscado:
            inicio=mitad+1 #split the list, look to the right, and of course start one position ahead of the middle one because it was already tested before

        else: 
            final= mitad-1 #split the list and search in the part with the smaller elements and -1 because it already tried the value that was in the middle
    
    return -1 #Not found

"""MERGE SORT"""

def reporteGlobal(inventarioGeneralLista):
    """This method is the MERGE SORT recursion part, this divides the general inventory list in two lists and it runs until the base case is met,
     it means when the list has only one element, and then it calls the 'mezclado' method that organizes the data """

    if len(inventarioGeneralLista) <= 1: #Base case when there is only one element on the list
        return inventarioGeneralLista #returns the one element list
    
    largo=len(inventarioGeneral)-1 
    medio=largo//2

    listaIZQ= inventarioGeneral[:medio] #List from the left of the general inventory
    listaDER=  inventarioGeneral[medio:] #list from the right

    listaIZQ=reporteGlobal(listaIZQ) #recursive call
    listaDER=reporteGlobal(listaDER)

    return mezclado(listaIZQ, listaDER)

def mezclado(listaIZQ, listaDER): 
    """This method is the MERGE SORT organization part, Sort in ascending order by the value (COP) of the books from the previously divided lists"""
    
    listaReporteGlobal=[] #List of result
    i=j=0

    while i < len(listaIZQ) and j < len(listaDER): #Goes throught the lists
         
        if listaIZQ[i].precio <= listaDER[j].precio: #This arranges in ascending order if the price form the 'listaIZQ' is cheaper it will add the price to the 'reporteGlobal'
            listaReporteGlobal.append(listaIZQ[i]) #adds the price
            i += 1 #adds one to the index
        
        else:
            listaReporteGlobal.append(listaDER[j]) #if the price on the right list has the lowest value, then it adds that one instead of the one on the left 
            j+=1 #adds one to the index

    listaReporteGlobal.extend(listaIZQ[i:]) #Adds the rest of the elements. add what remains from each list after comparing all possible elements
    listaReporteGlobal.extend(listaDER[j:])

    return listaReporteGlobal #Returns the result of the merge sort, the global report
    

    
