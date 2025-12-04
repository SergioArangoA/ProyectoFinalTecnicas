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
    
    def agregarReserva(self,isbn: str):
        """Adds the reservation to the user's reservation history"""
        from Data.DataManagement import cargarInventarioOrdenado
        from Classes.Libro import Libro
        from Data.ManejoListasMaestras import busquedaBinISBN, modificarLibro, modificarUsuario
        inventario = cargarInventarioOrdenado()
        indice = busquedaBinISBN(inventario,isbn)
        libro: Libro = inventario[indice]
        primeroListaEspera = False
        if libro.listaEspera:
            if libro.listaEspera[0].id == self.id:
                primeroListaEspera = True
            
        
        if libro.enInventario > len(libro.listaEspera) or (libro.enInventario > 0 and primeroListaEspera): #The book can be borrowed only if there are enough books or if the user is at the top of the waitlist
            if libro.enInventario > len(libro.listaEspera)  or libro.listaEspera[0].id == self.id:
                libro.enInventario -= 1
                libro.prestados += 1
                self.historialPrestados.append({"fecha":date.today().strftime("%Y-%m-%d"),"ISBN":libro.isbn,"retornado":False})
                ventana = tk.Toplevel(bg= "#EAE4D5")
                ventana.title("Anuncio")
                labelAnuncio = tk.Label(ventana, text="El libro se le puede prestar al usuario, valor a pagar: " + str(libro.precio),font=("Palatino Linotype", 14, "normal"), bg="#EAE4D5")
                labelAnuncio.pack()
            if libro.enInventario < len(libro.listaEspera):
                ventana = tk.Toplevel(bg= "#EAE4D5")
                ventana.title("Anuncio")
                labelAnuncio = tk.Label(ventana, text="Antes de poder prestar el libro se debe vaciar la lista de espera. El libro no se pudo prestar " + str(libro.precio),font=("Palatino Linotype", 14, "normal"), bg="#EAE4D5")
                
            if primeroListaEspera:
                libro.listaEspera.popleft() #Removes the user from the waitlist if they're at the top
        
        else:
            libro.listaEspera.append(self)
            ventana = tk.Toplevel(bg= "#EAE4D5")
            ventana.title("Anuncio")
            labelAnuncio = tk.Label(ventana, text="Se ha agregado al usuario a la lista de espera" + str(libro.precio),font=("Palatino Linotype", 14, "normal"), bg="#EAE4D5")
            labelAnuncio.pack()
        print("enInventario a guardar:", libro.enInventario)
        print("prestados a guardar:", libro.prestados)
        modificarUsuario(self.id,self.id,self.historialPrestados) #At last, saves the changes made
        modificarLibro(libro.isbn,libro.isbn,libro.titulo,libro.autor,libro.peso,libro.precio,libro.enInventario,libro.prestados,libro.listaEspera)
    
    def retornarLibro(self,isbn: str):
        """Returns the book to the inventory"""
        from Classes.Libro import Libro
        from Data.ManejoListasMaestras import busquedaBinISBN,modificarLibro,modificarUsuario
        from Data.DataManagement import cargarInventarioOrdenado
        inventario = cargarInventarioOrdenado()
        indice = busquedaBinISBN(inventario,isbn)
        libro: Libro = inventario[indice]
        encontrado = False
        for prestado in self.historialPrestados:
            if prestado["ISBN"] == libro.isbn and prestado["retornado"] == False:
                prestado["retornado"] = True
                encontrado = True
        if not encontrado: #Tells the user that the book hadn't been borrowed to that user
            ventana = tk.Toplevel(bg= "#EAE4D5")
            ventana.title("Anuncio")
            labelAnuncio = tk.Label(ventana, text="El libro no se le había prestado al usuario" + str(libro.precio),font=("Palatino Linotype", 14, "normal"), bg="#EAE4D5")
            labelAnuncio.pack()
        if encontrado:
            libro.enInventario += 1
            libro.prestados -= 1
            ventana = tk.Toplevel(bg= "#EAE4D5") #Makes the related modifications to the book
            ventana.title("Anuncio")
            labelAnuncio = tk.Label(ventana, text="El libro ha sido retornado" + str(libro.precio),font=("Palatino Linotype", 14, "normal"), bg="#EAE4D5")
            labelAnuncio.pack()
            if len(libro.listaEspera) > 0:
                ventana = tk.Toplevel(bg= "#EAE4D5")
                ventana.title("Anuncio")
                labelAnuncio = tk.Label(ventana, text="El próximo usuario en la lista de espera es: " + libro.listaEspera[0].id + str(libro.precio),font=("Palatino Linotype", 14, "normal"), bg="#EAE4D5")
                labelAnuncio.pack()

        modificarUsuario(self.id,self.id,self.historialPrestados)
        modificarLibro(libro.isbn, libro.isbn,libro.titulo,libro.autor,libro.peso,libro.precio,libro.enInventario,libro.prestados,libro.listaEspera)
        



