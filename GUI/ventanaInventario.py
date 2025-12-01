import tkinter as tk
from tkinter import ttk
import sys
import os
# Agregar la carpeta raíz del proyecto al PYTHONPATH
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.append(ROOT)

from Classes.Libro import Libro
from Data.DataManagement import cargarInventarioGeneral
from Data.DataManagement import cargarInventarioOrdenado
from Data.ManejoListasMaestras import valorTotalAutor
from Data.ManejoListasMaestras import pesoPromedioAutor
from Data.ManejoListasMaestras import normalizar

#INVENTORY WINDOW
def abrirInventario(ventanaPrincipal):
    """Opens a window, in which you can choose if you want to see both inventories, borrowed books's history and the total price of an author's books and average author's book weight in the inventory"""
    def abrirTablaInventario(inventario: list[Libro],tipoInventario: str):
        """Opens a new window that contains the data of the books saved in the inventory that the user chooses"""
        ventanaTabla = tk.Toplevel(bg="#EAE4D5")
        ventanaTabla.title(tipoInventario)

        tabla = ttk.Treeview(ventanaTabla, columns=('ISBN','TITULO','AUTOR','PESO','PRECIO','EN INVENTARIO','PRESTADOS'),show= 'headings')#ttk.Treeview alows to place elements in a table
        tabla.heading('ISBN',text='ISBN')
        tabla.heading('TITULO',text='TÍTULO')
        tabla.heading('AUTOR',text='AUTOR')
        tabla.heading('PESO',text='PESO(Kg)')
        tabla.heading('PRECIO',text='PRECIO')
        tabla.heading('EN INVENTARIO',text='EN INVENTARIO')
        tabla.heading('PRESTADOS',text = 'PRESTADOS') #The text that will be shown on each heading
        tabla.pack()

        for libro in inventario:
            tabla.insert(parent='',index=tk.END,values=(libro.isbn, #tk.END agrega el elemento al final de la tabla
                                                    libro.titulo,
                                                    libro.autor,
                                                    str(libro.peso),
                                                    str(libro.precio),
                                                    str(libro.enInventario),
                                                    str(libro.prestados))) #Each one of the book parameters that will be shown in the table
        
    def buscarPesoYValor():
        """Reads the author name textbox, then searchs the average weight and total price of their books in the inventory."""
        InventarioOrdenado = cargarInventarioOrdenado()
        nombre = str(CampoTextoAutor.get())
        CampoValorTotal.config(state="normal")#This will allow to write the values in the textbox
        CampoPeso.config(state="normal")
        CampoPeso.delete(0, tk.END)
        CampoValorTotal.delete(0,tk.END) #Deletes the previous data in the textbox
        CampoValorTotal.insert(0,str(valorTotalAutor(nombre,InventarioOrdenado)))
        CampoPeso.insert(0,str(pesoPromedioAutor(nombre,InventarioOrdenado,normalizar)))
        CampoValorTotal.config(state="disabled")#Then will block them again
        CampoPeso.config(state="disabled")

    #INVENTORY WINDOW SETTINGS

    ventanaPrincipal.withdraw() #Hides the main window when the secondary window is opened
    ventanaInventario = tk.Toplevel(bg="#EAE4D5") #Toplevel creates a new secondary window and bg adds color
    ventanaInventario.protocol("WM_DELETE_WINDOW", lambda: ventanaPrincipal.destroy()) #Closes the main menu window once the user clicks the X button
    #Toplevel creates a new secondary window different from the main one (TK). There can only be one TK window.
    ventanaInventario.title("Gestión de Inventario")
    ventanaInventario.state('zoomed')
    ventanaInventario.resizable(True, True)
    ventanaInventario.rowconfigure(0,weight=1)
    ventanaInventario.rowconfigure(1,weight=1)
    ventanaInventario.rowconfigure(2,weight=1)
    ventanaInventario.columnconfigure(0,weight=1)

    #INVENTORY'S WINDOWS FRAMES
    frameTitulo = tk.Frame(ventanaInventario,bg="#EAE4D5")
    frameTitulo.grid(row=0,column=0)
    frameTitulo.columnconfigure(0,weight=1)
    frameTitulo.rowconfigure(0,weight=1)

    frameBotones = tk.Frame(ventanaInventario,bg="#EAE4D5")
    frameBotones.grid(row=1,column=0)
    frameBotones.columnconfigure(0,weight=1)
    frameBotones.columnconfigure(1,weight=1)
    frameBotones.columnconfigure(2,weight=1)
    frameBotones.rowconfigure(0,weight=1)

    frameEstadisticas = tk.Frame(ventanaInventario,bg="#EAE4D5")
    frameEstadisticas.grid(row=2,column=0)

    #INVENTORY TITLE

    titulo= tk.Label(frameTitulo, text="INVENTARIO", font=("Palatino Linotype", 20, "bold"), bg="#EAE4D5", fg="#213555")
    titulo.grid(row=0,column=0,sticky="nsew")

    #Secondary Buttons inside

    InventarioGeneral= tk.Button(frameBotones, text="Inventario general",command=lambda: abrirTablaInventario(cargarInventarioGeneral(),"Inventario general"), width=25, height=2, font=("Palatino Linotype", 14), bg="#B6B09F")
    InventarioGeneral.grid(row=0,column=0,sticky="nsew",padx=20)

    InventarioOrdenado= tk.Button(frameBotones, text="Inventario ordenado",command=lambda: abrirTablaInventario(cargarInventarioOrdenado(),"Inventario ordenado"), width=25, height=2, font=("Palatino Linotype", 14), bg="#B6B09F")
    InventarioOrdenado.grid(row=0,column=1,sticky="nsew",padx=20)

    historialPrestamos = tk.Button(frameBotones,text="Historal de préstamos",width=25, height=2, font=("Palatino Linotype",14),bg="#B6B09F")
    historialPrestamos.grid(row=0,column=2,sticky="nsew",padx=20)

    #AUTHOR'S BOOKS STATISTICS
    
    tituloEstadisticas= tk.Label(frameEstadisticas, text="ESTADISTICAS LIBROS AUTOR", font=("Palatino Linotype", 20, "bold"), bg="#EAE4D5", fg="#213555")
    tituloEstadisticas.grid(row=0,column=1,sticky="nsew")

    labelAutor = tk.Label(frameEstadisticas,text="Nombre autor: ", font=("Palatino Linotype", 14, "bold"), bg="#EAE4D5")
    labelAutor.grid(row=1,column=0)
    CampoTextoAutor= tk.Entry(frameEstadisticas,font=("Palatino Linotype", 14),width=30,bg="#FFFFFF",relief="groove",bd=2)
    CampoTextoAutor.grid(row=1,column=1)
    botonBuscar = tk.Button(frameEstadisticas,text="Buscar",command= lambda: buscarPesoYValor(),width=20, height=1, font=("Palatino Linotype", 14), bg="#B6B09F")
    botonBuscar.grid(row=1,column=2,sticky="nsew")

    labelPeso = tk.Label(frameEstadisticas,text="Peso promedio(kg): ", font=("Palatino Linotype", 14, "bold"), bg="#EAE4D5")
    labelPeso.grid(row=2, column=0,pady=10)
    CampoPeso= tk.Entry(frameEstadisticas,font=("Palatino Linotype", 14),width=30,bg="#FFFFFF",relief="groove",bd=2, state="disabled")
    CampoPeso.grid(row=2,column=1,pady=10)

    labelValorTotal= tk.Label(frameEstadisticas,text="Total de valor de libros: ", font=("Palatino Linotype", 14, "bold"), bg="#EAE4D5")
    labelValorTotal.grid(row=3, column=0,sticky="nsew",pady=10)
    CampoValorTotal= tk.Entry(frameEstadisticas,font=("Palatino Linotype", 14),width=30,bg="#FFFFFF",relief="groove",bd=2, state="disabled")
    CampoValorTotal.grid(row=3,column=1,pady=10)

    volver=tk.Button(frameEstadisticas, text="VOLVER AL MENÚ", command=lambda: [ventanaInventario.destroy(), ventanaPrincipal.deiconify()], bg="#213555",fg="white", font=("Palatino Linotype", 12), width=20).grid(row=4, column=0, padx=10, pady=20)
    #Returns to the main menu. .destroy() closes the window and .decoinify() shows the main window again
