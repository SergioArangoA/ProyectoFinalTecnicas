import tkinter as tk
import sys
import os
from datetime import date, datetime


# Agregar la carpeta raíz del proyecto al PYTHONPATH
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.append(ROOT)

# IMPORTS ABSOLUTOS (estos nunca fallan)
from collections import deque
class Usuario:
    """A Usuario Instance represents a User from the library
        Attributes:

        id(str): Users ID
        HistorialPrestados(deque-Pile): History of borrowed books
        
        Methods: 
        usuarioADiccionario(): This method converts the user object in a dictionary

        """

    def __init__(self, id: str, historialPrestados: list ):
        self.id = id
        self.historialPrestados= list(historialPrestados)

    def usuarioADiccionario(self):
        diccionarioUsuario = {"id":self.id,"historialPrestados":list(self.historialPrestados)}
        return diccionarioUsuario
    
    def agregarReserva(self, isbn: str):
        """
        Attempt to borrow a book for the user.
        Handles inventory, waitlist, estantes, and history updates.
        """
        from Data.DataManagement import cargarInventarioOrdenado, cargarEstantes #Import necessary functions and classes
        from Classes.Libro import Libro
        from Data.ManejoListasMaestras import busquedaBinISBN, modificarLibro, modificarUsuario, eliminarLibroEstante

        
        inventario = cargarInventarioOrdenado() #Load ordered inventory and shelf list
        listaEstantes = cargarEstantes()

        indice = busquedaBinISBN(inventario, isbn) #Find book by ISBN
        libro: Libro = inventario[indice]


        primeroListaEspera = libro.listaEspera and len(libro.listaEspera) > 0 and libro.listaEspera[0] == self.id #Check if user is first in the waitlist (safe check for empty list)

        if libro.enInventario > len(libro.listaEspera) or primeroListaEspera: #Check if book can be borrowed (enough inventory or user is first in waitlist)
            #Remove book from all shelves before borrow

            for estanteID in libro.estantes[:]:  #Iterate over a copy to avoid modification issues
                eliminarLibroEstante(libro, estanteID, listaEstantes)

            libro.enInventario -= 1 #Update book inventory and borrowed count
            libro.prestados += 1

            self.historialPrestados.append({   #Saves the borrowing in user's history
                "fecha": date.today().strftime("%Y-%m-%d"),
                "ISBN": libro.isbn,
                "retornado": False
            })

            if primeroListaEspera: #Remove user from waitlist if they were first
                libro.listaEspera.popleft()
            ventana = tk.Toplevel(bg="#EAE4D5") #Notify that the book has been returned
            tk.Label(ventana,
            text="Prestar el libro por un valor de: " + str(libro.precio),
            font=("Palatino Linotype", 14), bg="#EAE4D5").pack()

        else:
            libro.listaEspera.append(self.id)  #Add user ID to waitlist if book cannot be borrowed

            ventana = tk.Toplevel(bg="#EAE4D5") #Notify that the user was added to the waitlist
            tk.Label(ventana,
            text="Se ha añadido al usuario a la lista de espera",
            font=("Palatino Linotype", 14), bg="#EAE4D5").pack()

        #Save changes to user and book in persistent storage
        modificarUsuario(self.id, self.id, self.historialPrestados)
        modificarLibro(libro.isbn , libro.isbn, libro.titulo, libro.autor, libro.peso, #first isbn: old isbn second: new isbn
            libro.precio, libro.enInventario, libro.prestados, libro.listaEspera)


    def retornarLibro(self, isbn: str):
        """Return a borrowed book, update inventory, and automatically lend to next user in waitlist.
        """
        from Classes.Libro import Libro
        from Data.ManejoListasMaestras import busquedaBinISBN, modificarLibro, modificarUsuario, buscarUsuario
        from Data.DataManagement import cargarInventarioOrdenado

        inventario = cargarInventarioOrdenado()

        indice = busquedaBinISBN(inventario, isbn)
        libro: Libro = inventario[indice]

        encontrado = False #Flag var

        for prestado in self.historialPrestados: #Find the borrowing record in user's history
            if prestado["ISBN"] == libro.isbn and not prestado["retornado"]:
                prestado["retornado"] = True  #Mark as returned
                encontrado = True
                break

        if not encontrado:
            ventana = tk.Toplevel(bg="#EAE4D5") #Notify user if book was not borrowed
            ventana.title("Anuncio")
            tk.Label(
                ventana,
                text="El libro no se le había prestado al usuario" + str(libro.precio),
                font=("Palatino Linotype", 14), bg="#EAE4D5"
            ).pack()
            return

        #Update book inventory and borrowed count
        libro.enInventario += 1
        libro.prestados -= 1

        ventana = tk.Toplevel(bg="#EAE4D5") #Notify that the book has been returned
        ventana.title("Anuncio")
        tk.Label(ventana,
            text="El libro ha sido retornado" + str(libro.precio),
            font=("Palatino Linotype", 14), bg="#EAE4D5").pack()

        if libro.listaEspera: #Automatically lend to the next user in waitlist if any
            siguienteUsuarioid = libro.listaEspera[0] #Get the ID of the next user in the waitlist (the first user in the queue)
            siguienteUsuario = buscarUsuario(siguienteUsuarioid) #Get the next user in line from the waitlist

            if siguienteUsuario:
                siguienteUsuario.agregarReserva(isbn)  #Let the next user borrow the book automatically

        # Save changes to user history and book inventory
        modificarUsuario(self.id, self.id, self.historialPrestados)
        modificarLibro(libro.isbn, libro.isbn, libro.titulo, libro.autor, libro.peso, libro.precio, libro.enInventario, 
        libro.prestados, libro.listaEspera)


