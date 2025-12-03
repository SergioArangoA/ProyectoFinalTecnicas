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
from Data.DataManagement import guardarEstantes
from Data.DataManagement import cargarEstantes
from Classes.Estante import Estante
from GUI import *
# Agregar la carpeta raíz del proyecto al PYTHONPATH
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.append(ROOT)

# IMPORTS ABSOLUTOS (estos nunca fallan)
from Data import *
from Classes.Estante import Estante
from Data.ManejoListasMaestras import guardarEstanteFuncion
from GUI import *

#STAND WINDOW
def abrirEstanterias(ventanaPrincipal):
    """Opens a window, which contains the Stand class CRUD."""

    def abrirTablaLibros():
        """Opens a new window that contains the data of the books saved in the stand's inventory"""
        listaLibros = list[Libro]
        ventanaTabla = tk.Toplevel(bg="#EAE4D5")
        ventanaTabla.title("Libros en estante UwU")

        tabla = ttk.Treeview(ventanaTabla, columns=('ISBN','TITULO','AUTOR','PESO','PRECIO'),show= 'headings')#ttk.Treeview alows to place elements in a table
        tabla.heading('ISBN',text='ISBN')
        tabla.heading('TITULO',text='TÍTULO')
        tabla.heading('AUTOR',text='AUTOR')
        tabla.heading('PESO',text='PESO(Kg)')
        tabla.heading('PRECIO',text='PRECIO')
        tabla.pack()

        for libro in listaLibros:
            tabla.insert(parent='',index=tk.END,values=(libro.isbn, #tk.END agrega el elemento al final de la tabla
                                                    libro.titulo,
                                                    libro.autor,
                                                    str(libro.peso),
                                                    str(libro.precio)))
    def guardarEstanterias():
        """A method that read's the id in the stand's id textbox, then creates a stand with said id"""
        id = CampoTextoID.get()
        if id:
            agregado = guardarEstanteFuncion(id,[])
            if not agregado:
               ventanaError("No se agregó el estante porque ya existía uno con la misma id")
            else:
               campoImpresionID.config(state="normal")
               campoImpresionID.delete(0,tk.END)
               campoImpresionID.insert(0,str(id))
               campoImpresionID.config(state="disabled")
        else:
            ventanaError("Por favor ingrese un id para poder agregar el estante")

    def ventanaError(mensaje: str):
        """A pop up window that will print the message sent"""
        ventana = tk.Toplevel(bg= "#EAE4D5")
        ventana.title("ERROR")
        labelError = tk.Label(ventana, text=mensaje,font=("Palatino Linotype", 14, "normal"), bg="#EAE4D5")
        labelError.pack()

    def abrirListaEstantes():
        """Opens a new window that contains a table with the list of stands and their characteristics"""
        ventanaTabla = tk.Toplevel(bg="#EAE4D5")
        ventanaTabla.title("Lista de estantes")
        listaEstantes = cargarEstantes() #Loads the stand list

        tabla = ttk.Treeview(ventanaTabla, columns=('ID','CANTIDAD DE LIBROS','PESO','VALOR ACUMULADO'),show= 'headings')#ttk.Treeview alows to place elements in a table
        tabla.heading('ID',text='ID')
        tabla.heading('CANTIDAD DE LIBROS',text='CANTIDAD DE LIBROS')
        tabla.heading('PESO',text='PESO')
        tabla.heading('VALOR ACUMULADO',text='VALOR ACUMULADO') #the text that will be shown on each heading
        tabla.pack()

        for estante in listaEstantes:
            tabla.insert(parent='',index=tk.END,values=(estante.obtenerID(), #tk.END adds the element at the end of the table
                                                    estante.cantidadLibros(),
                                                    estante.calcularPesoAcumulado(),
                                                    str(estante.calcularValorAcumulado()))) #Each one of the parameters that will be shown in the table
        
    



    #STAND WINDOW SETTINGS

    ventanaPrincipal.withdraw() #Hides the main window when the secondary window is opened
    ventanaEstante = tk.Toplevel(bg="#EAE4D5") #Toplevel creates a new secondary window and bg adds color
    ventanaEstante.protocol("WM_DELETE_WINDOW", lambda: ventanaPrincipal.destroy()) #Closes the main menu window once the user clicks the X button
    
    ventanaEstante.title("Gestión de Estantes")
    ventanaEstante.state('zoomed')
    ventanaEstante.resizable(True, True)
    ventanaEstante.columnconfigure(0,weight=1)
    ventanaEstante.columnconfigure(1,weight=0)
    ventanaEstante.columnconfigure(2,weight=1)
    ventanaEstante.rowconfigure(0,weight=1)
    ventanaEstante.rowconfigure(1,weight=1)
    ventanaEstante.rowconfigure(2,weight=1)
    ventanaEstante.rowconfigure(3,weight=1)
    ventanaEstante.columnconfigure(0, weight=1)
    ventanaEstante.columnconfigure(1,weight=1)

    #STAND'S WINDOWS FRAMES
    frameTitulo = tk.Frame(ventanaEstante,bg="#EAE4D5")
    frameTitulo.grid(row=0,column=1)
    frameTitulo.columnconfigure(0,weight=1)

    frameEstante = tk.Frame(ventanaEstante,bg= "#EAE4D5")
    frameEstante.grid(row=1,column=1,padx=10)
    frameEstante.columnconfigure(0,weight=1)
    frameEstante.columnconfigure(1,weight=1)

    frameIDEstante = tk.Frame(frameEstante,bg= "#EAE4D5")
    frameIDEstante.grid(row=0,column=0,columnspan=2)

    frameLibros =tk.Frame(ventanaEstante, bg = "#EAE4D5")
    frameLibros.grid(row=3,column=1)
    frameLibros.columnconfigure(0, weight=1)
    frameLibros.columnconfigure(1,weight=1)
  
    frameInfoEstanteActual = tk.Frame(frameLibros,bg= "#EAE4D5")
    frameInfoEstanteActual.grid(row=0,column=0,columnspan=2)

    #WINDOW'S TITLE

    titulo= tk.Label(frameTitulo, text="ESTANTE", font=("Palatino Linotype", 20, "bold"), bg="#EAE4D5", fg="#213555")
    titulo.grid(row=0,column=0,sticky="nsew")


    #STAND'S ID CRUD

    labelID = tk.Label(frameIDEstante,text="ID: ", font=("Palatino Linotype", 14, "bold"), bg="#EAE4D5")
    labelID.grid(row=0,column=0,pady=10,sticky="e")
    CampoTextoID= tk.Entry(frameIDEstante,font=("Palatino Linotype", 14),width=30,bg="#FFFFFF",relief="groove",bd=2)
    CampoTextoID.grid(row=0,column=1,pady=10,sticky="w")
    botonAgregar = tk.Button(frameEstante,text="Agregar",command=lambda: guardarEstanterias(),width=20, height=1, font=("Palatino Linotype", 14), bg="#B6B09F")
    botonAgregar.grid(row=1,column=0,padx=10,pady=20,sticky="e")
    botonModificar = tk.Button(frameEstante,text="Modificar",width=20, height=1, font=("Palatino Linotype", 14), bg="#B6B09F")
    botonModificar.grid(row=1,column=1,padx=10,pady=20,sticky="w")
    botonBuscar = tk.Button(frameEstante,text="Buscar",width=20, height=1, font=("Palatino Linotype", 14), bg="#B6B09F")
    botonBuscar.grid(row=2,column=0,padx=10,pady=20,sticky="e")
    botonEliminar = tk.Button(frameEstante,text="Eliminar",width=20, height=1, font=("Palatino Linotype", 14), bg="#B6B09F")
    botonEliminar.grid(row=2,column=1,padx=10,pady=20,sticky="w")
    botonListaEstantes = tk.Button(frameEstante,text="Abrir lista de estantes",command=lambda:abrirListaEstantes(),width=20, height=1, font=("Palatino Linotype", 14), bg="#B6B09F")
    botonListaEstantes.grid(row=3,column=0,padx=10,pady=20,columnspan=2)


    #STAND'S CONTAINED BOOKS CRUD
    labelEstanteActual = tk.Label(frameInfoEstanteActual,text="Estante actual: ", font=("Palatino Linotype", 14, "bold"), bg="#EAE4D5")
    labelEstanteActual.grid(row=0,column=0,sticky="e")
    campoImpresionID = tk.Entry(frameInfoEstanteActual,font=("Palatino Linotype", 14),width=30,bg="#FFFFFF",relief="groove",bd=2,state="disabled")
    campoImpresionID.grid(row=0,column=1,pady=10,sticky="w")
    
    labelCantidadLibros = tk.Label(frameInfoEstanteActual,text="Cantidad de libros: ", font=("Palatino Linotype", 14, "bold"), bg="#EAE4D5")
    labelCantidadLibros.grid(row=1,column=0,pady=10,sticky="e")
    CampoTextoISBN= tk.Entry(frameInfoEstanteActual,font=("Palatino Linotype", 14),width=30,bg="#FFFFFF",relief="groove",bd=2)
    CampoTextoISBN.grid(row=1,column=1,pady=10,sticky="w")

    labelPeso = tk.Label(frameInfoEstanteActual,text="Peso acumulado:", font=("Palatino Linotype", 14, "bold"), bg="#EAE4D5")
    labelPeso.grid(row=2,column=0,pady=10,sticky="e")
    CampoTextoPeso= tk.Entry(frameInfoEstanteActual,font=("Palatino Linotype", 14),width=30,bg="#FFFFFF",relief="groove",bd=2,state="disabled")
    CampoTextoPeso.grid(row=2,column=1,pady=10,sticky="w")

    botonAbrirListaLibros = tk.Button(frameInfoEstanteActual,text="Lista de libros",command=lambda: abrirTablaLibros(), width=20, height=1, font=("Palatino Linotype", 14), bg="#B6B09F")
    botonAbrirListaLibros.grid(row=3,column=0,columnspan=2,sticky="nsew")

    labelISBN = tk.Label(frameInfoEstanteActual,text="ISBN: ", font=("Palatino Linotype", 14, "bold"), bg="#EAE4D5")
    labelISBN.grid(row=4,column=0,pady=10,sticky="e")
    CampoTextoISBN= tk.Entry(frameInfoEstanteActual,font=("Palatino Linotype", 14),width=30,bg="#FFFFFF",relief="groove",bd=2)
    CampoTextoISBN.grid(row=4,column=1,pady=10,sticky="w")

    botonAgregarLibro = tk.Button(frameLibros,text="Agregar libro",width=20, height=1, font=("Palatino Linotype", 14), bg="#B6B09F")
    botonAgregarLibro.grid(row=2,column=0,pady=10,sticky="e",padx=10)
    botonEliminarLibro = tk.Button(frameLibros,text="Remover libro",width=20, height=1, font=("Palatino Linotype", 14), bg="#B6B09F")
    botonEliminarLibro.grid(row=2,column=1,pady=10,sticky="w",padx=10)

    botonOrdenarOptimo = tk.Button(frameLibros,text="Ordenamiento óptimo",width=20, height=1, font=("Palatino Linotype", 14), bg="#B6B09F")
    botonOrdenarOptimo.grid(row=3,column=0,pady=20,sticky="e",padx=10)
    botonOrdenarDeficiente = tk.Button(frameLibros,text="Ordenamiento deficiente",width=20, height=1, font=("Palatino Linotype", 14), bg="#B6B09F")
    botonOrdenarDeficiente.grid(row=3,column=1,pady=20,sticky="w",padx=10)

    volver=tk.Button(ventanaEstante, text="VOLVER AL MENÚ", command=lambda: [ventanaEstante.destroy(), ventanaPrincipal.deiconify()], bg="#213555",fg="white", font=("Palatino Linotype", 12), width=20).grid(row=4, column=1, padx=10, pady=20,sticky="w")