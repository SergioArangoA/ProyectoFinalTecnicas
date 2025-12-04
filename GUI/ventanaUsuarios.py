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
from Classes.Usuario import Usuario
from Data.ManejoListasMaestras import buscarUsuario, guardarUsuarioFuncion, busquedaBinISBN, eliminarUsuario
from Data.DataManagement import cargarInventarioOrdenado, cargarUsuarios


def abrirUsuarios(ventanaPrincipal):


    """Opens the User class CRUD"""
    usuario = None

    def borrarUsuario():
        """Deletes the searched user from the user list"""
        nonlocal usuario
        if usuario:
            eliminarUsuario(usuario.id)
            CampoImprimirUsuario.config(state="normal")
            CampoImprimirUsuario.delete(0,tk.END)
            CampoImprimirUsuario.config(state="disabled")
            usuario = None #Deletes the user from both the list and the window's memory. Also deletes the text shown on the print ID textbox
        
        else:
            ventanaError("Por favor busque un usuario antes de eliminarlo")


    def guardarUsuarios():
        """Reads the user's ID in the ID label and adds it to the users list"""
        id = CampoTextoIngresarUsuario.get()
        if id:
            succes = guardarUsuarioFuncion(id,[]) #Succes will be true if the user was added, if the user already existed, it will be false
            if not succes:
                ventanaError("El usuario que usted quiere agregar ya existe, no se pudo agregar.")
            else:
                        CampoImprimirUsuario.config(state="normal")
                        CampoImprimirUsuario.delete(0,tk.END)
                        CampoImprimirUsuario.insert(0,str(id))
                        CampoImprimirUsuario.config(state="disabled")

        else:
            ventanaError("Por favor ingrese el id del usuario que desea agregar")

    def imprimirUsuario():
        """Searchs for the user to print its data"""
        nonlocal usuario
        usuario = None
        
        id = CampoTextoIngresarUsuario.get()
        if id:
            usuario = buscarUsuario(id)
            if usuario:
                CampoImprimirUsuario.config(state="normal")
                CampoImprimirUsuario.delete(0,tk.END)
                CampoImprimirUsuario.insert(0,usuario.id)
                CampoImprimirUsuario.config(state="disabled")
            
            else:
                ventanaError("No se encontró el usuario que estaba buscando")

        
        else:
            ventanaError("Por favor ingrese el documento del usuario que desea buscar")

    def abrirHistorialReservas():
        """Opens the reservation history of the searched user"""
        if usuario:
            ventanaTabla = tk.Toplevel(bg="#EAE4D5")
            ventanaTabla.title("Historial de reservas")
            tabla = ttk.Treeview(ventanaTabla, columns=('FECHA','ISBN','RETORNADO'),show= 'headings')#ttk.Treeview alows to place elements in a table
            tabla.heading('FECHA',text='FECHA')
            tabla.heading('ISBN',text='ISBN')
            tabla.heading('RETORNADO',text='RETORNADO')  #The text that will be shown on each heading
            tabla.pack()
            for reserva in usuario.historialPrestados:
                retornado = "No"
                if reserva["retornado"] == True:
                    retornado = "Si"
                tabla.insert(parent='',index=tk.END,values=(reserva["fecha"],reserva["ISBN"],retornado))            
        else:
            ventanaError("Por favor busque un usuario antes de abrir su historial de reservas")
    
    def reservarLibro():
        """Adds the book to the user's reservation history"""
        nonlocal usuario #nonlocal so that the object from outside the method can be accesed
        if CampoTextoIngresarISBN.get():
            libro = busquedaBinISBN(cargarInventarioOrdenado(),CampoTextoIngresarISBN.get())
            if libro != -1:
                usuario.agregarReserva(CampoTextoIngresarISBN.get())
            
            else:
                print("El libro no fue encontrado, no se pudo hacer la reserva")
        
        else:
            ventanaError("Por favor escriba el ISBN del libro que desea reservarle al usuario")
    
    def imprimirUsuarios():
        """Loads the user list from the JSON and then shows a list of IDs of al the users registered in the system"""
        ventanaTabla = tk.Toplevel(bg="#EAE4D5")
        ventanaTabla.title("Lista de usuarios")
        listaUsuarios = cargarUsuarios()

        tabla = ttk.Treeview(ventanaTabla, columns=('ID'),show= 'headings')#ttk.Treeview alows to place elements in a table
        tabla.heading('ID',text='ID') #The text that will be shown on the heading
        tabla.pack()

        for usuario in listaUsuarios:
            tabla.insert(parent='',index=tk.END,values=(usuario.id)) #tk.END agrega el elemento al final de la tabla
    

        
    
    def ventanaError(mensaje: str):
        """A pop up window that will print the message sent"""
        ventana = tk.Toplevel(bg= "#EAE4D5")
        ventana.title("ERROR")
        labelError = tk.Label(ventana, text=mensaje,font=("Palatino Linotype", 14, "normal"), bg="#EAE4D5")
        labelError.pack()
        


    #WINDOW SETTINGS
    ventanaPrincipal.withdraw()
    ventanaUsuario = tk.Toplevel(bg="#EAE4D5")
    ventanaUsuario.title("Gestión de Usuarios")
    ventanaUsuario.protocol("WM_DELETE_WINDOW", lambda: ventanaPrincipal.destroy()) #Closes the main menu window once the user clicks the X button
    #Toplevel creates a new secondary window different from the main one (TK). There can only be one TK window.
    ventanaUsuario.state('zoomed')
    ventanaUsuario.resizable(True, True)
    ventanaUsuario.rowconfigure(0,weight=1)
    ventanaUsuario.rowconfigure(1,weight=1)
    ventanaUsuario.rowconfigure(2,weight=1)
    ventanaUsuario.rowconfigure(3,weight=1)
    ventanaUsuario.rowconfigure(4,weight=1)
    ventanaUsuario.columnconfigure(0,weight=1)

    #WINDOW FRAMES

    frameTituloUsuario = tk.Frame(ventanaUsuario,bg="#EAE4D5")
    frameTituloUsuario.grid(row=0,column=0)

    frameUsuario = tk.Frame(ventanaUsuario,bg="#EAE4D5")
    frameUsuario.grid(row=1,column=0,sticky="nsew")
    frameUsuario.columnconfigure(0,weight=1)
    frameUsuario.rowconfigure(1,weight=1)

    frameIngresarUsuario = tk.Frame(frameUsuario,bg="#EAE4D5")
    frameIngresarUsuario.grid(row=1,column=0)
    
    frameBotonesUsuario = tk.Frame(frameUsuario,bg="#EAE4D5")
    frameBotonesUsuario.grid(row=3,column=0,columnspan=3,pady=50)

    frameTituloLibro = tk.Frame(ventanaUsuario,bg="#EAE4D5")
    frameTituloLibro.grid(row=2,column=0)

    frameLibro = tk.Frame(ventanaUsuario,bg="#EAE4D5")
    frameLibro.grid(row=3,column=0)
    frameLibro.rowconfigure(0,weight=1)
    frameLibro.rowconfigure(1,weight=1)
    frameLibro.rowconfigure(2,weight=1)


    frameBotonesLibro = tk.Frame(frameLibro,bg="#EAE4D5")
    frameBotonesLibro.grid(row=1,column=1)

    #USER CRUD

    tituloUsuario= tk.Label(frameTituloUsuario, text="USUARIO", font=("Palatino Linotype", 20, "bold"), bg="#EAE4D5", fg="#213555")
    tituloUsuario.grid(row=0,column=0,sticky="nsew")

    labelIngresarUsuario = tk.Label(frameIngresarUsuario, text="Documento: ", font=("Palatino Linotype", 14, "bold"), bg="#EAE4D5")
    labelIngresarUsuario.grid(row=0,column=0)
    CampoTextoIngresarUsuario= tk.Entry(frameIngresarUsuario,font=("Palatino Linotype", 14),width=30,bg="#FFFFFF",relief="groove",bd=2)
    CampoTextoIngresarUsuario.grid(row=0,column=1)
    CampoImprimirUsuario= tk.Entry(frameIngresarUsuario,font=("Palatino Linotype", 14),width=30,bg="#FFFFFF",relief="groove",bd=2, state="disabled")
    CampoImprimirUsuario.grid(row=0,column=2,padx=20)

    AgregarUsuario= tk.Button(frameBotonesUsuario,command=lambda: guardarUsuarios(), text="Agregar", width=20, height=2,font=("Palatino Linotype", 14), bg="#B6B09F").grid(row=0, column=0, padx=10, pady=20,sticky="nsew")

    ModificarUsuario= tk.Button(frameBotonesUsuario, text="Modificar", width=20, height=2, font=("Palatino Linotype", 14), bg="#B6B09F").grid(row=0, column=1, padx=10, pady=20,sticky="nsew")

    BuscarUsuario=tk.Button(frameBotonesUsuario,command=lambda: imprimirUsuario(), text="Buscar", width=20, height=2, font=("Palatino Linotype", 14), bg="#B6B09F").grid(row=0, column=2, padx=10, pady=20,sticky="nsew")

    EliminarUsuario = tk.Button(frameBotonesUsuario,command=lambda:borrarUsuario(), text="Eliminar", width=20, height=2, font=("Palatino Linotype", 14), bg="#B6B09F").grid(row=0, column=3, padx=10, pady=20,sticky="nsew")

    abrirListaUsuario = tk.Button(frameBotonesUsuario,command=lambda: imprimirUsuarios(), text="Abrir lista de usuarios", width=20, height=2, font=("Palatino Linotype", 14), bg="#B6B09F").grid(row=1, column=1,columnspan=2, padx=10, pady=20,sticky="nsew")
    #BOOK RESERVATION CRUD

    tituloLibro= tk.Label(frameTituloLibro, text="LIBRO", font=("Palatino Linotype", 20, "bold"), bg="#EAE4D5", fg="#213555")
    tituloLibro.grid(row=0,column=1)

    labelIngresarISBN = tk.Label(frameLibro, text="ISBN: ", font=("Palatino Linotype", 14, "bold"), bg="#EAE4D5")
    labelIngresarISBN.grid(row=0,column=0)
    CampoTextoIngresarISBN= tk.Entry(frameLibro,font=("Palatino Linotype", 14),width=30,bg="#FFFFFF",relief="groove",bd=2)
    CampoTextoIngresarISBN.grid(row=0,column=1,sticky="nsew")

    botonReservarLibro = tk.Button(frameBotonesLibro,command=lambda: reservarLibro(), text="Prestar", width=20, height=2,font=("Palatino Linotype", 14), bg="#B6B09F").grid(row=0, column=0, padx=10, pady=20,sticky="nsew")

    retornarLibro = tk.Button(frameBotonesLibro, text="Retornar", width=20, height=2, font=("Palatino Linotype", 14), bg="#B6B09F").grid(row=0, column=1, padx=10, pady=20,sticky="nsew")

    historialReservas = tk.Button(frameBotonesLibro,command=lambda: abrirHistorialReservas(), text="Historial de reservas", width=20, height=2, font=("Palatino Linotype", 14), bg="#B6B09F").grid(row=1, column=0, columnspan=2, padx=10, pady=20,sticky="nsew")

    volver=tk.Button(frameBotonesLibro, text="VOLVER AL MENÚ", command=lambda: [ventanaUsuario.destroy(), ventanaPrincipal.deiconify()], bg="#213555",fg="white", font=("Palatino Linotype", 12), width=20).grid(row=2, column=0, columnspan=2, pady=50)
