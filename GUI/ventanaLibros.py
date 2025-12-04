import tkinter as tk
from tkinter import ttk
import sys
import os
# Agregar la carpeta raíz del proyecto al PYTHONPATH
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.append(ROOT)

# IMPORTS ABSOLUTOS (estos nunca fallan)
from Data.ManejoListasMaestras import guardarLibro, busquedaBinISBN, busquedaPorAutor, busquedaporTitulo, eliminarlibro, modificarLibro
from Data.DataManagement import cargarInventarioOrdenado
from Classes.Libro import Libro



#BOOKS'S CRUD WINDOW
def abrirLibros(ventanaPrincipal):
    """Opens the Book class CRUD"""

    libroBuscado = None

    #METHODS
    def agregarLibro():
        """Reads the data in the textboxes to add a book. Also opens a new window that will ask the user the amount of books they want to add"""
        isbn = CampoTextoISBN.get()
        titulo= None
        autor = None
        peso = None
        precio = None
        if busquedaBinISBN(cargarInventarioOrdenado(),isbn) == -1: #First looks for a book, if it can't be found, reads the other textboxes data to add it
            titulo = CampoTextoTitulo.get()
            autor = CampoTextoAutor.get()
            peso = float(CampoTextoPeso.get())
            precio = int(CampoTextoPrecio.get())
            if peso < 0 or precio < 0:
                peso = None
                precio = None 
        cantidad = ventanaCantidadLibros(True) #Opens a new window that will ask the amount they want to add
        if (isbn and titulo and autor and peso and precio and cantidad) or busquedaBinISBN(cargarInventarioOrdenado(),isbn) != -1:
            #If the user filled every box, proceeds to do the verifications before finally adding the book
            while cantidad < 0:
                ventanaError("La cantidad no puede ser un número negativo")
                cantidad = ventanaCantidadLibros(True)
            if cantidad > 0:
                guardarLibro(isbn,titulo,autor,peso,precio,cantidad,0,[],None)
                imprimirLibro()
            else:
                ventanaError("No se agregó ningún libro porque la cantidad ingresada fue 0")
        else:
            #If the user didn't fill all the boxes, shows him an error
            ventanaError("Asegúrese de llenar todos los campos antes de agregar el libro")
    
    def borrarLibros():
        """Reads the isbn in the print isbn box, and then proceeds to ask the user for an amount of said book to delete and lastly deletes said amount"""
        isbn = CampoImprimirISBN.get() #Checks that the user has searched for a book before doing anything else

        if not isbn:
            ventanaError("Por favor primero busque un libro antes de eliminarlo") #If there wasn't a previously searched book, shows the user an error

        if isbn:
            cantidad = ventanaCantidadLibros(False)
            while cantidad < 0: 
                ventanaError("Por favor ingrese una cantidad mayor o igual a cero") #The amount of books added must be positive
                cantidad = ventanaCantidadLibros(False) #Will keep showing the amount tab until a valid amount is inputted
            
            eliminarlibro(isbn, cantidad)
            if cantidad == 0: #Tell the user that the amount was 0
                ventanaError("No se eliminó ningún libro porque la cantidad ingresada fue cero")
            inventario = cargarInventarioOrdenado()
            indice = busquedaBinISBN(cargarInventarioOrdenado(),isbn)
            libro = inventario[indice] #Then searches the book after the amount was changed
            if libro: #If the book is found
                texto = CampoTextoISBN.get() #Saves the text in the input box
                CampoTextoISBN.delete(0,tk.END)
                CampoTextoISBN.insert(0,isbn) #Inserts the old isbn to search for the book
                imprimirLibro() #Prints the book data
                CampoTextoISBN.delete(0,tk.END)
                CampoTextoISBN.insert(0,texto) #then returns the old text to the input box so the user doesn't notice any changes
            else:  #If the book isn't found, it means that it was removed from the invetory
                ventana = tk.Toplevel(bg= "#EAE4D5")
                label = tk.Label(ventana, text="El libro ha sido eliminado del inventario",font=("Palatino Linotype", 14, "normal"), bg="#EAE4D5")
                label.pack()

    def modificarDatosLibro():
        if CampoImprimirISBN.get():
            ISBNanterior = CampoImprimirISBN.get()
            isbn = None
            titulo = None
            autor = None
            peso = None
            precio = None
            if CampoTextoISBN.get():
                isbn = CampoTextoISBN.get()
            if CampoTextoTitulo.get():
                titulo = CampoTextoTitulo.get()
            if CampoTextoAutor.get():
                autor = CampoTextoAutor.get()
            if CampoTextoPeso.get():
                peso = CampoTextoPeso.get()
                if peso < 0:
                    peso = None
            if CampoTextoPrecio.get():
                precio = CampoTextoPrecio.get()
                if precio < 0:
                    precio = None
            modificarLibro(ISBNanterior,isbn,titulo,autor,peso,precio,None,None)
            if isbn:
                imprimirLibro()
            else:
                CampoTextoISBN.insert(0,ISBNanterior)
                imprimirLibro()
                CampoTextoISBN.delete(0,tk.END)

        
        else:
            ventanaError("Por favor busque un libro antes de realizar modificaciones")



    def ventanaError(mensaje: str):
        """A pop up window that will print the message sent"""
        ventana = tk.Toplevel(bg= "#EAE4D5")
        ventana.title("ERROR")
        labelError = tk.Label(ventana, text=mensaje,font=("Palatino Linotype", 14, "normal"), bg="#EAE4D5")
        labelError.pack()
    
    def ventanaCantidadLibros(agregar: bool):
        """A window that will ask the amount of books that the user will either want to add or remove. Will return the amount inserted by the user"""
        ventana = tk.Toplevel()
        ventana.title("Cantidad de libros")
        ventana.geometry("350x150")
        ventana.grab_set()  #Makes the user only able to interact with this window until it closes
        tk.Label(ventana, text="").pack(pady=10)
        mensaje = ""
        if agregar:
            mensaje = "Cantidad a agregar: "
        
        else:
            mensaje = "Cantidad a eliminar: "

        tk.Label(ventana, text=mensaje).pack(pady=10)
        campo = tk.Entry(ventana)
        campo.pack()
        resultado = {"valor":0} # The amount must be saved in a dictionary because they are mutable

        def confirmar():
            try:
                resultado["valor"] = int(campo.get())
                ventana.destroy()
            except ValueError:
                ventanaError("Por favor ingrese un valor válido")
                ventana.destroy()

        tk.Button(ventana, text="OK", command=confirmar).pack(pady=10)
        ventana.wait_window() #The program stops running until the window is closed
        return resultado["valor"]
    
    def imprimirLibro():
        """Searchs the book and prints its data once it's found. The book is first searched by ISBN, then by title, then by author. If no book is found once the three searches are done, it shows an error message"""
        libro = None
        CampoImprimirISBN.config(state="normal")
        CampoImprimirTitulo.config(state="normal")
        CampoImprimirAutor.config(state="normal")
        CampoImprimirPeso.config(state="normal")
        CampoImprimirPrecio.config(state="normal")
        CampoImprimirEnInventario.config(state="normal")
        CampoImprimirPrestados.config(state="normal")
        CampoImprimirEnEstantes.config(state="normal") #First makes all the print textboxes rewritable

        CampoImprimirISBN.delete(0,tk.END)
        CampoImprimirTitulo.delete(0,tk.END)
        CampoImprimirAutor.delete(0,tk.END)
        CampoImprimirPeso.delete(0,tk.END)
        CampoImprimirPrecio.delete(0,tk.END)
        CampoImprimirEnInventario.delete(0,tk.END)
        CampoImprimirPrestados.delete(0,tk.END)
        CampoImprimirEnEstantes.delete(0,tk.END) #Then deletes the previous text found in the textbox

        #Then proceeds to search, first by ISBN, then by title, lastly by author
        encontrado = False
        if CampoTextoISBN.get() or CampoTextoTitulo.get() or CampoTextoAutor.get():
            #First checks that the user has at least filled one of the search requirements
            if CampoTextoISBN.get():
                inventario = cargarInventarioOrdenado()
                indice = busquedaBinISBN(cargarInventarioOrdenado(),CampoTextoISBN.get())
                if indice != -1:
                    libro = inventario[indice] #Searchs the book by ISBN
                    encontrado = True
            
            if not libro and CampoTextoTitulo.get(): #If the book hasn't been found and it can be searched by title, searches it again by title
                listaLibros = busquedaporTitulo(CampoTextoTitulo.get())
                if listaLibros:
                    abrirTablaBuscados(listaLibros, "Libros con el título " + CampoTextoTitulo.get())
                    encontrado = True
            
            if not libro and CampoTextoAutor.get(): #If the book hasn't been found and it can be searche by author, searches it again
                listaLibros = busquedaPorAutor(CampoTextoAutor.get())
                if listaLibros:
                    abrirTablaBuscados(listaLibros, "Libros de " + CampoTextoAutor.get())
                    encontrado = True
            
            if libro:
                        
                CampoImprimirISBN.insert(0,libro.isbn)
                CampoImprimirTitulo.insert(0,libro.titulo)
                CampoImprimirAutor.insert(0,libro.autor)
                CampoImprimirPeso.insert(0,libro.peso)
                CampoImprimirPrecio.insert(0,libro.precio)
                CampoImprimirEnInventario.insert(0,libro.enInventario)
                CampoImprimirPrestados.insert(0,libro.prestados)
                CampoImprimirEnEstantes.insert(0,libro.estantes) #Prints the book data
            
            
            if not encontrado:
                ventanaError("No se encontró el libro que usted buscaba") #If the book still isn't found, tells the user that it couldn't be found
        
        else:
            ventanaError("Por favor asegúrese de haber llenado al menos uno de los campos: ISBN, Titulo o Autor para poder realizar la búsqueda") 
            #If the user didn't input any of the necesary fields for the search, tells him to do so
        
        CampoImprimirISBN.config(state="disabled")
        CampoImprimirTitulo.config(state="disabled")
        CampoImprimirAutor.config(state="disabled")
        CampoImprimirPeso.config(state="disabled")
        CampoImprimirPrecio.config(state="disabled")
        CampoImprimirEnInventario.config(state="disabled")
        CampoImprimirPrestados.config(state="disabled")
        CampoImprimirEnEstantes.config(state="disabled") #Lastly, disables the print textboxes once again
    
    def abrirTablaBuscados(listaLibros: list[Libro],tipoBusqueda: str):
        """Opens a new window that contains the list of the books found with the search parameters"""
        ventanaTabla = tk.Toplevel(bg="#EAE4D5")
        ventanaTabla.title(tipoBusqueda)

        tabla = ttk.Treeview(ventanaTabla, columns=('ISBN','TITULO','AUTOR','PESO','PRECIO','EN INVENTARIO','PRESTADOS'),show= 'headings')#ttk.Treeview alows to place elements in a table
        tabla.heading('ISBN',text='ISBN')
        tabla.heading('TITULO',text='TÍTULO')
        tabla.heading('AUTOR',text='AUTOR')
        tabla.heading('PESO',text='PESO(Kg)')
        tabla.heading('PRECIO',text='PRECIO')
        tabla.heading('EN INVENTARIO',text='EN INVENTARIO')
        tabla.heading('PRESTADOS',text = 'PRESTADOS') #The text that will be shown on each heading
        tabla.pack()

        for libro in listaLibros:
            for i in tabla.get_children():
                tabla.delete(i) #Borra los elementos de la tabla antes de insertar algo
            tabla.insert(parent='',index=tk.END,values=(libro.isbn, #tk.END agrega el elemento al final de la tabla
                                                    libro.titulo,
                                                    libro.autor,
                                                    str(libro.peso),
                                                    str(libro.precio),
                                                    str(libro.enInventario),
                                                    str(libro.prestados))) #Each one of the book parameters that will be shown in the table
        
                





    #WINDOW

    #CRUD WINDOW SETTINGS
    ventanaPrincipal.withdraw() #Hides the principal window
    ventanaLibros = tk.Toplevel(bg="#EAE4D5") #Creates a window with that background color
    ventanaLibros.protocol("WM_DELETE_WINDOW", lambda: ventanaPrincipal.destroy()) #Also closes the main menu window once the user hits the close button
    ventanaLibros.title("Gestión de Libros")
    ventanaLibros.state('zoomed') #Se abre en pantalla completa
    ventanaLibros.columnconfigure(0, weight=1) #Allows the column "0" to be resizable 
    ventanaLibros.rowconfigure(2, weight=1) #Allows the row "2" to be resizable 

    #CRUD WINDOW FRAMES

    frameLibrosContenido = tk.Frame(ventanaLibros,bg="#EAE4D5",bd=5)
    frameLibrosContenido.grid(row=1,column=0,sticky="nsew") #sticky = "nsew" allows the frame to be resizable
    frameLibrosContenido.columnconfigure(0,weight=1)
    frameLibrosContenido.columnconfigure(3,weight=1)

    frameLibrosIngresar = tk.Frame(frameLibrosContenido,bg="#EAE4D5",bd=5)
    frameLibrosIngresar.grid(row=1,column=0,sticky="nsew")
    frameLibrosIngresar.columnconfigure(1, weight=1)

    frameLibrosImprimir = tk.Frame(frameLibrosContenido,bg="#EAE4D5",bd=5)
    frameLibrosImprimir.grid(row=1,column=3,sticky="nsew")
    frameLibrosImprimir.columnconfigure(1, weight=1)

    frameBotones = tk.Frame(ventanaLibros, bg="#EAE4D5",bd=5)
    frameBotones.grid(row=2,column=0,sticky="nsew")
    frameBotones.columnconfigure(0,weight=1)
    frameBotones.columnconfigure(1,weight=1)
    frameBotones.columnconfigure(2,weight=1)
    frameBotones.columnconfigure(3,weight=1)

    #CRUD WINDOW TITLE

    titulo= tk.Label(frameLibrosContenido, text="LIBROS", font=("Palatino Linotype", 20, "bold"), bg="#EAE4D5", fg="#213555")
    titulo.grid(row=0,column=2)
    
    #BOOK'S ISBN LABELS AND TEXTBOXES
    #tk.Entry is a textbox, if the state is disabled, means the user can't write on it
    #relief="flat" makes the entry field flat without 3D borders, bd=2 sets the border width to 2 pixels

    labelIngresarISBN = tk.Label(frameLibrosIngresar, text="ISBN: ", font=("Palatino Linotype", 14, "bold"), bg="#EAE4D5")
    labelIngresarISBN.grid(row=0,column=0)
    CampoTextoISBN= tk.Entry(frameLibrosIngresar,font=("Palatino Linotype", 14),width=30,bg="#FFFFFF",relief="groove",bd=2)
    CampoTextoISBN.grid(row=0,column=1,sticky="nsew")
    CampoImprimirISBN= tk.Entry(frameLibrosImprimir,font=("Palatino Linotype", 14),width=30,bg="#FFFFFF",relief="groove",bd=2, state="disabled")
    CampoImprimirISBN.grid(row=0,column=1,sticky="nsew")

    #BOOK'S TITLE LABELS AND TEXTBOXES

    labelIngresarTitulo= tk.Label(frameLibrosIngresar, text="Título: ",font=("Palatino Linotype", 14, "bold"), bg="#EAE4D5")
    labelIngresarTitulo.grid(row=1,column=0,pady=10)
    CampoTextoTitulo= tk.Entry(frameLibrosIngresar,font=("Palatino Linotype", 14),width=30,bg="#FFFFFF",relief="groove",bd=2)
    CampoTextoTitulo.grid(row=1,column=1,pady=10,sticky="nsew")
    CampoImprimirTitulo= tk.Entry(frameLibrosImprimir,font=("Palatino Linotype", 14),width=30,bg="#FFFFFF",relief="groove",bd=2, state="disabled")
    CampoImprimirTitulo.grid(row=1,column=1,pady=10,sticky="nsew")

    #BOOK'S AUTHOR LABELS AND TEXTBOXES

    labelIngresarAutor =tk.Label(frameLibrosIngresar, text="Autor: ",font=("Palatino Linotype", 14, "bold"), bg="#EAE4D5")
    labelIngresarAutor.grid(row=2,column=0,pady=10)
    CampoTextoAutor= tk.Entry(frameLibrosIngresar,font=("Palatino Linotype", 14),width=30,bg="#FFFFFF",relief="groove",bd=2)
    CampoTextoAutor.grid(row=2,column=1,pady=10,sticky="nsew")
    CampoImprimirAutor= tk.Entry(frameLibrosImprimir,font=("Palatino Linotype", 14),width=30,bg="#FFFFFF",relief="groove",bd=2, state="disabled")
    CampoImprimirAutor.grid(row=2,column=1,pady=10,sticky="nsew")

    #BOOK'S WEIGHT LABELS AND TEXTBOXES

    labelIngresarPeso =tk.Label(frameLibrosIngresar, text="Peso(kg): ",font=("Palatino Linotype", 14, "bold"), bg="#EAE4D5")
    labelIngresarPeso.grid(row=3,column=0,pady=10)
    CampoTextoPeso= tk.Entry(frameLibrosIngresar,font=("Palatino Linotype", 14),width=30,bg="#FFFFFF",relief="groove",bd=2)
    CampoTextoPeso.grid(row=3,column=1,pady=10,sticky="nsew")
    CampoImprimirPeso= tk.Entry(frameLibrosImprimir,font=("Palatino Linotype", 14),width=30,bg="#FFFFFF",relief="groove",bd=2, state="disabled")
    CampoImprimirPeso.grid(row=3,column=1,pady=10,sticky="nsew")

    #BOOK'S PRICE LABELS AND TEXTBOXES

    labelIngresarPrecio =tk.Label(frameLibrosIngresar, text="Precio: ",font=("Palatino Linotype", 14, "bold"), bg="#EAE4D5")
    labelIngresarPrecio.grid(row=4,column=0,pady=10)
    CampoTextoPrecio= tk.Entry(frameLibrosIngresar,font=("Palatino Linotype", 14),width=30,bg="#FFFFFF",relief="groove",bd=2)
    CampoTextoPrecio.grid(row=4,column=1,pady=10,sticky="nsew")
    CampoImprimirPrecio= tk.Entry(frameLibrosImprimir,font=("Palatino Linotype", 14),width=30,bg="#FFFFFF",relief="groove",bd=2, state="disabled")
    CampoImprimirPrecio.grid(row=4,column=1,pady=10,sticky="nsew")

    #BOOK'S INVENTORY AMOUNT LABELS AND TEXTBOXES

    labelVaciaEnInventario =tk.Label(frameLibrosIngresar, text="",font=("Palatino Linotype", 14, "bold"), bg="#EAE4D5")
    labelVaciaEnInventario.grid(row=5,column=0,pady=10)
    labelEnInventario =tk.Label(frameLibrosImprimir, text="En inventario: ",font=("Palatino Linotype", 14, "bold"), bg="#EAE4D5")
    labelEnInventario.grid(row=5,column=0,pady=10)
    CampoImprimirEnInventario= tk.Entry(frameLibrosImprimir,font=("Palatino Linotype", 14),width=30,bg="#FFFFFF",relief="groove",bd=2, state="disabled")
    CampoImprimirEnInventario.grid(row=5,column=1,pady=10,sticky="nsew")

    #BOOK'S BORROWED AMOUNT LABELS AND TEXTBOXES
    
    labelVacioPrestados=tk.Label(frameLibrosIngresar, text="",font=("Palatino Linotype", 14, "bold"), bg="#EAE4D5")
    labelVacioPrestados.grid(row=6,column=0,pady=10)
    labelPrestados =tk.Label(frameLibrosImprimir, text="Prestados: ",font=("Palatino Linotype", 14, "bold"), bg="#EAE4D5")
    labelPrestados.grid(row=6,column=0,pady=10)
    CampoImprimirPrestados= tk.Entry(frameLibrosImprimir,font=("Palatino Linotype", 14),width=30,bg="#FFFFFF",relief="groove",bd=2, state="disabled")
    CampoImprimirPrestados.grid(row=6,column=1,pady=10,sticky="nsew")

    #BOOK'S STANDS LOCATIONS LABELS AND TEXTBOXES

    labelVacioEnEstantes =tk.Label(frameLibrosIngresar, text="",font=("Palatino Linotype", 14, "bold"), bg="#EAE4D5")
    labelVacioEnEstantes.grid(row=7,column=0,pady=10)
    labelEnEstantes =tk.Label(frameLibrosImprimir, text="En estantes: ",font=("Palatino Linotype", 14, "bold"), bg="#EAE4D5")
    labelEnEstantes.grid(row=7,column=0,pady=10)
    CampoImprimirEnEstantes= tk.Entry(frameLibrosImprimir,font=("Palatino Linotype", 14),width=30,bg="#FFFFFF",relief="groove",bd=2, state="disabled")
    CampoImprimirEnEstantes.grid(row=7,column=1,pady=10,sticky="nsew")    
    
    #CRUD BUTTONS

    AgregarLibro= tk.Button(frameBotones,command=agregarLibro, text="Agregar", width=20, height=2,font=("Palatino Linotype", 14), bg="#B6B09F").grid(row=0, column=0, padx=10, pady=20,sticky="nsew")

    ModificarLibro= tk.Button(frameBotones,command = lambda: modificarDatosLibro(), text="Modificar", width=20, height=2, font=("Palatino Linotype", 14), bg="#B6B09F").grid(row=0, column=1, padx=10, pady=20,sticky="nsew")

    BuscarLibro=tk.Button(frameBotones, text="Buscar", width=20, command=lambda: imprimirLibro(), height=2, font=("Palatino Linotype", 14), bg="#B6B09F").grid(row=0, column=2, padx=10, pady=20,sticky="nsew")

    EliminarLibro= tk.Button(frameBotones,command=lambda: borrarLibros(), text="Eliminar", width=20, height=2, font=("Palatino Linotype", 14), bg="#B6B09F").grid(row=0, column=3, padx=10, pady=20,sticky="nsew")

    #RETURN BUTTON
    volver=tk.Button(frameBotones, text="VOLVER AL MENÚ", command=lambda: [ventanaLibros.destroy(), ventanaPrincipal.deiconify()], bg="#213555",fg="white", font=("Palatino Linotype", 12), width=20).grid(row=1, column=0, padx=10, pady=20)


