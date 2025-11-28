import tkinter as tk
from tkinter import ttk
import sys
import os
import tkinter as tk
import sys
import os

# Agregar la carpeta raíz del proyecto al PYTHONPATH
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.append(ROOT)

# IMPORTS ABSOLUTOS (estos nunca fallan)
from Data import *
from Classes import *
from GUI import *
# Agregar la carpeta raíz del proyecto al PYTHONPATH
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.append(ROOT)

# IMPORTS ABSOLUTOS (estos nunca fallan)
from Data import *
from Classes import *
from GUI import *

#STAND WINDOW
def abrirEstanterias(ventanaPrincipal):
    """Opens a window, which contains the Stand class CRUD."""

    #STAND WINDOW SETTINGS

    ventanaPrincipal.withdraw() #Hides the main window when the secondary window is opened
    ventanaEstante = tk.Toplevel(bg="#EAE4D5") #Toplevel creates a new secondary window and bg adds color
    ventanaEstante.protocol("WM_DELETE_WINDOW", lambda: ventanaPrincipal.destroy()) #Closes the main menu window once the user clicks the X button
    
    ventanaEstante.title("Gestión de Estantes")
    ventanaEstante.state('zoomed')
    ventanaEstante.resizable(True, True)
    ventanaEstante.columnconfigure(0,weight=1)
    ventanaEstante.rowconfigure(0,weight=1)
    ventanaEstante.rowconfigure(1,weight=1)
    ventanaEstante.rowconfigure(2,weight=1)
    ventanaEstante.columnconfigure(0, weight=1)
    ventanaEstante.columnconfigure(1,weight=1)

    #STAND'S WINDOWS FRAMES
    frameTitulo = tk.Frame(ventanaEstante,bg="#EAE4D5")
    frameTitulo.grid(row=0,column=0)

    frameEstante = tk.Frame(ventanaEstante,bg= "#EAE4D5")
    frameEstante.grid(row=1,column=0,padx=10)

    frameLibros =tk.Frame(ventanaEstante, bg = "#EAE4D5")
    frameLibros.grid(row=2,column=0)

    #WINDOW'S TITLE

    titulo= tk.Label(frameTitulo, text="ESTANTE", font=("Palatino Linotype", 20, "bold"), bg="#EAE4D5", fg="#213555")
    titulo.grid(row=0,column=0,sticky="nsew")


    #STAND'S ID CRUD

    labelID = tk.Label(frameEstante,text="ID: ", font=("Palatino Linotype", 14, "bold"), bg="#EAE4D5")
    labelID.grid(row=0,column=0,pady=10)
    CampoTextoID= tk.Entry(frameEstante,font=("Palatino Linotype", 14),width=30,bg="#FFFFFF",relief="groove",bd=2)
    CampoTextoID.grid(row=0,column=1,pady=10)
    botonAgregar = tk.Button(frameEstante,text="Agregar",width=20, height=1, font=("Palatino Linotype", 14), bg="#B6B09F")
    botonAgregar.grid(row=1,column=0,sticky="nsew",padx=10,pady=20)
    botonModificar = tk.Button(frameEstante,text="Modificar",width=20, height=1, font=("Palatino Linotype", 14), bg="#B6B09F")
    botonModificar.grid(row=1,column=1,sticky="nsew",padx=10,pady=20)
    botonBuscar = tk.Button(frameEstante,text="Buscar",width=20, height=1, font=("Palatino Linotype", 14), bg="#B6B09F")
    botonBuscar.grid(row=2,column=0,sticky="nsew",padx=10,pady=20)
    botonEliminar = tk.Button(frameEstante,text="Buscar",width=20, height=1, font=("Palatino Linotype", 14), bg="#B6B09F")
    botonEliminar.grid(row=2,column=1,sticky="nsew",padx=10,pady=20)
    botonListaEstantes = tk.Button(frameEstante,text="Abrir lista de estantes",width=20, height=1, font=("Palatino Linotype", 14), bg="#B6B09F")
    botonListaEstantes.grid(row=3,column=0,sticky="nsew",padx=10,pady=20,columnspan=2)


    #STAND'S CONTAINED BOOKS CRUD
    CampoImpresionID= tk.Entry(frameLibros,font=("Palatino Linotype", 14),width=30,bg="#FFFFFF",relief="groove",bd=2)
    CampoImpresionID.grid(row=0,column=1,pady=10)

    labelISBN1 = tk.Label(frameLibros,text="ISBN: ", font=("Palatino Linotype", 14, "bold"), bg="#EAE4D5")
    labelISBN1.grid(row=1,column=0,pady=10)
    CampoTextoISBN1= tk.Entry(frameLibros,font=("Palatino Linotype", 14),width=30,bg="#FFFFFF",relief="groove",bd=2)
    CampoTextoISBN1.grid(row=1,column=1,pady=10)
    labelPresente1 = tk.Label(frameLibros,text="En estante: ", font=("Palatino Linotype", 14, "bold"), bg="#EAE4D5")
    labelPresente1.grid(row=1,column=2,pady=10)
    CampoTextoPresente1= tk.Entry(frameLibros,font=("Palatino Linotype", 14),width=30,bg="#FFFFFF",relief="groove",bd=2, state="disabled")
    CampoTextoPresente1.grid(row=1,column=3,pady=10)

    labelISBN2 = tk.Label(frameLibros,text="ISBN: ", font=("Palatino Linotype", 14, "bold"), bg="#EAE4D5")
    labelISBN2.grid(row=2,column=0,pady=10)
    CampoTextoISBN2= tk.Entry(frameLibros,font=("Palatino Linotype", 14),width=30,bg="#FFFFFF",relief="groove",bd=2)
    CampoTextoISBN2.grid(row=2,column=1,pady=10)
    labelPresente2 = tk.Label(frameLibros,text="En estante: ", font=("Palatino Linotype", 14, "bold"), bg="#EAE4D5")
    labelPresente2.grid(row=2,column=2,pady=10)
    CampoTextoPresente2 = tk.Entry(frameLibros,font=("Palatino Linotype", 14),width=30,bg="#FFFFFF",relief="groove",bd=2, state="disabled")
    CampoTextoPresente2.grid(row=2,column=3,pady=10)

    labelISBN3 = tk.Label(frameLibros,text="ISBN: ", font=("Palatino Linotype", 14, "bold"), bg="#EAE4D5")
    labelISBN3.grid(row=3,column=0,pady=10)
    CampoTextoISBN3= tk.Entry(frameLibros,font=("Palatino Linotype", 14),width=30,bg="#FFFFFF",relief="groove",bd=2)
    CampoTextoISBN3.grid(row=3,column=1,pady=10)
    labelPresente3 = tk.Label(frameLibros,text="En estante: ", font=("Palatino Linotype", 14, "bold"), bg="#EAE4D5")
    labelPresente3.grid(row=3,column=2,pady=10)
    CampoTextoPresente3 = tk.Entry(frameLibros,font=("Palatino Linotype", 14),width=30,bg="#FFFFFF",relief="groove",bd=2, state="disabled")
    CampoTextoPresente3.grid(row=3,column=3,pady=10)

    labelISBN4 = tk.Label(frameLibros,text="ISBN: ", font=("Palatino Linotype", 14, "bold"), bg="#EAE4D5")
    labelISBN4.grid(row=4,column=0,pady=10)
    CampoTextoISBN4= tk.Entry(frameLibros,font=("Palatino Linotype", 14),width=30,bg="#FFFFFF",relief="groove",bd=2)
    CampoTextoISBN4.grid(row=4,column=1,pady=10)
    labelPresente4 = tk.Label(frameLibros,text="En estante: ", font=("Palatino Linotype", 14, "bold"), bg="#EAE4D5")
    labelPresente4.grid(row=4,column=2,pady=10)
    CampoTextoPresente4 = tk.Entry(frameLibros,font=("Palatino Linotype", 14),width=30,bg="#FFFFFF",relief="groove",bd=2, state="disabled")
    CampoTextoPresente4.grid(row=4,column=3,pady=10)

    botonActualizar = tk.Button(frameLibros,text="Actualizar",width=20, height=1, font=("Palatino Linotype", 14), bg="#B6B09F")
    botonActualizar.grid(row=0,column=3,sticky="nsew",padx=10,pady=20)
    botonOrdenarOptimo = tk.Button(frameLibros,text="Ordenamiento óptimo",width=20, height=1, font=("Palatino Linotype", 14), bg="#B6B09F")
    botonOrdenarOptimo.grid(row=6,column=0,padx=10,pady=20, columnspan=2)
    botonOrdenarDeficiente = tk.Button(frameLibros,text="Ordenamiento deficiente",width=20, height=1, font=("Palatino Linotype", 14), bg="#B6B09F")
    botonOrdenarDeficiente.grid(row=6,column=3,padx=10,pady=20, columnspan=2)

    volver=tk.Button(ventanaEstante, text="VOLVER AL MENÚ", command=lambda: [ventanaEstante.destroy(), ventanaPrincipal.deiconify()], bg="#213555",fg="white", font=("Palatino Linotype", 12), width=20).grid(row=3, column=0, padx=10, pady=20)










