import tkinter as tk
from tkinter import ttk


#BOOKS'S CRUD WINDOW
def abrirLibros(ventanaPrincipal):
    """Opens the Book class CRUD"""

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

    AgregarLibro= tk.Button(frameBotones, text="Agregar", width=20, height=2,font=("Palatino Linotype", 14), bg="#B6B09F").grid(row=0, column=0, padx=10, pady=20,sticky="nsew")

    ModificarLibro= tk.Button(frameBotones, text="Modificar", width=20, height=2, font=("Palatino Linotype", 14), bg="#B6B09F").grid(row=0, column=1, padx=10, pady=20,sticky="nsew")

    BuscarLibro=tk.Button(frameBotones, text="Buscar", width=20, height=2, font=("Palatino Linotype", 14), bg="#B6B09F").grid(row=0, column=2, padx=10, pady=20,sticky="nsew")

    EliminarLibro= tk.Button(frameBotones, text="Eliminar", width=20, height=2, font=("Palatino Linotype", 14), bg="#B6B09F").grid(row=0, column=3, padx=10, pady=20,sticky="nsew")

    #RETURN BUTTON
    volver=tk.Button(frameBotones, text="VOLVER AL MENÚ", command=lambda: [ventanaLibros.destroy(), ventanaPrincipal.deiconify()], bg="#213555",fg="white", font=("Palatino Linotype", 12), width=20).grid(row=1, column=0, padx=10, pady=20)