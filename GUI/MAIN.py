import tkinter as tk
import sys
import os

# Agregar la carpeta raíz del proyecto al PYTHONPATH
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.append(ROOT)

from GUI import *
# IMPORTS ABSOLUTOS (estos nunca fallan)
#Imports functions for the secondary windows from the file botonesSecundarios.py
"""Importa las funciones de las ventanas secundarias desde el archivo botonesSecundarios.py"""

"""Crear la ventana principal"""
#Create Main window
Ventana_principal = tk.Tk()
Ventana_principal.configure(bg="#EAE4D5") #Sets the background color of the main window

#Customize Main window
Ventana_principal.title("Inicio")          #Window Title
Ventana_principal.geometry("500x800")       #Window Size (ancho x alto)
Ventana_principal.resizable(True, True)     #Allows Resize Main Window (ancho y alto)

#Window Title Label
titulo = tk.Label(Ventana_principal, text="MENÚ PRINCIPAL", font=("Palatino Linotype", 30, "bold"), fg="#213555", bg="#EAE4D5")
"""Un Label es un texto que se muestra en la ventana, pero no se puede editar ni interactuar con él (no es un campo de texto)
dice que va a estar en la ventana principal, que texto va a mostrar, fuente color etc"""

titulo.pack(pady= 35) #The pack method places the title in the window and pady gives it a vertical margin of 20 pixels
"""El pack mete el titulo a la ventana y el pady le da un margen vertical de 20 pixeles"""

## MAIN CRUD BUTTONS: CREATE, DISPLAY, CONNECT TO SECONDARY WINDOWS
ButtonInventario= tk.Button(Ventana_principal, text="Inventario", font=("Palatino Linotype", 20), width=25, height=1, bg="#B6B09F")
ButtonInventario.pack(pady=20)
ButtonInventario.config(command=lambda: abrirInventario(Ventana_principal))#Calls the abrirInventario function from the botonesSecundarios.py file, linking the button to the window
## Lambda is created as a function that calls the abrirInventario function from5 the botonesSecundarios.py file, passes the main window as an argument, and links the button to the window
"""Lambda se crea como funcion que Llama a la funcion abrirInventario del archivo botonesSecundarios.py, y pasa ventana principal como
argumento y enlazaza boton con ventana"""

ButtonEstanterias= tk.Button(Ventana_principal, text="Estanterias", font=("Palatino Linotype", 20), width=25, height=1, bg="#B6B09F")
ButtonEstanterias.pack(pady=20)
ButtonEstanterias.config(command=lambda: abrirEstanterias(Ventana_principal)) #Calls the abrirEstanterias function from the botonesSecundarios.py file, linking the button to the window

ButtonUsuario= tk.Button(Ventana_principal, text="Usuario", font=("Palatino Linotype", 20), width=25, height=1, bg="#B6B09F")
ButtonUsuario.pack(pady=20)
ButtonUsuario.config(command=lambda:abrirUsuarios(Ventana_principal)) 

ButtonLibros= tk.Button(Ventana_principal, text="Libros", font=("Palatino Linotype", 20), width=25, height=1, bg="#B6B09F")
ButtonLibros.pack(pady=20)
ButtonLibros.config(command=lambda: abrirLibros(Ventana_principal)) 
"""Label y Button son tipos de objetos (clases) que crea tkinter para construir la interfaz."""

#Show Main window
Ventana_principal.mainloop() # Keeps the window open until the user decides to close it. It makes the window appear and stay open.
"""Mantiene la ventana abierta hasta que el usuario decida cerrarla Hace que la ventana se muestre y se quede abierta."""
