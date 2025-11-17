import tkinter as tk
from tkinter import ttk

#INVENTORY WINDOW
def abrirInventario(ventanaPrincipal):
    """Opens a window, in which you can choose if you want to see both inventories, borrowed books's history and the total price of an author's books and average author's book weight in the inventory"""

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

    InventarioGeneral= tk.Button(frameBotones, text="Inventario general", width=25, height=2, font=("Palatino Linotype", 14), bg="#B6B09F")
    InventarioGeneral.grid(row=0,column=0,sticky="nsew",padx=20)

    InventarioOrdenado= tk.Button(frameBotones, text="Inventario ordenado", width=25, height=2, font=("Palatino Linotype", 14), bg="#B6B09F")
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
    botonBuscar = tk.Button(frameEstadisticas,text="Buscar",width=20, height=1, font=("Palatino Linotype", 14), bg="#B6B09F")
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
#SECONDARY RESERVATION WINDOW


def abrirReservas(Ventana_principal):
    #Create new window
        root = tk.Tk()
        root.title("Estructura de ventana")
        root.geometry("600x400")

        # --- CONFIGURAR GRID PRINCIPAL ---
        root.rowconfigure(1, weight=1)   # La fila 1 (el contenido central) se expande
        root.columnconfigure(0, weight=1)

        # --- FRAME SUPERIOR ---
        frame_superior = ttk.Frame(root, padding=10, relief="ridge")
        frame_superior.grid(row=0, column=0, sticky="ew")

        ttk.Label(frame_superior, text="Barra superior / título", font=("Arial", 14, "bold")).pack()

        # --- FRAME CENTRAL ---
        frame_central = ttk.Frame(root, padding=10)
        frame_central.grid(row=1, column=0, sticky="nsew")

        # Configurar columnas del frame central
        frame_central.columnconfigure(0, weight=1)
        frame_central.columnconfigure(1, weight=3)

        # Subframe izquierdo
        frame_izquierdo = ttk.Frame(frame_central, padding=5, relief="groove")
        frame_izquierdo.grid(row=0, column=0, sticky="nsew")
        frame_izquierdo.pack()

        ttk.Label(frame_izquierdo, text="Panel izquierdo").pack(side="left", pady=5)
        ttk.Button(frame_izquierdo, text="Botón A").pack(side="left", pady=5)
        ttk.Button(frame_izquierdo, text="Botón B").pack(side="left", pady=5)

        # Subframe derecho
        frame_derecho = ttk.Frame(frame_central, padding=5, relief="groove")
        frame_derecho.grid(row=0, column=1, sticky="nsew")

        ttk.Label(frame_derecho, text="Zona principal de contenido").pack()
        ttk.Entry(frame_derecho).pack(pady=5)
        ttk.Text(frame_derecho, height=5, width=40).pack()

        # --- FRAME INFERIOR ---
        frame_inferior = ttk.Frame(root, padding=10, relief="ridge")
        frame_inferior.grid(row=2, column=0, sticky="ew")

        ttk.Button(frame_inferior, text="Aceptar").pack(side="left", padx=10)
        ttk.Button(frame_inferior, text="Cancelar").pack(side="right", padx=10)

        root.mainloop()

#STANDS'S CRUD WINDOW
def abrirEstanterias(ventanaPrincipal):
    """Opens the Book class CRUD"""

    #CRUD WINDOW SETTINGS
    ventanaPrincipal.withdraw() #Hides the principal window
    ventanaEstantes = tk.Toplevel(bg="#EAE4D5") #Creates a window with that background color
    ventanaEstantes.protocol("WM_DELETE_WINDOW", lambda: ventanaPrincipal.destroy()) #Also closes the main menu window once the user hits the close button
    ventanaEstantes.title("Gestión de Libros")
    ventanaEstantes.state('zoomed') #Se abre en pantalla completa
    ventanaEstantes.columnconfigure(0, weight=1) #Allows the column "0" to be resizable 
    ventanaEstantes.rowconfigure(2, weight=1) #Allows the row "2" to be resizable 

    #CRUD WINDOW FRAMES

    frameEstantesContenido = tk.Frame(ventanaEstantes,bg="#EAE4D5",bd=5)
    frameEstantesContenido.grid(row=1,column=0,sticky="nsew") #sticky = "nsew" allows the frame to be resizable
    frameEstantesContenido.columnconfigure(0,weight=1)
    frameEstantesContenido.columnconfigure(3,weight=1)

    frameEstantesIngresar = tk.Frame(frameEstantesContenido,bg="#EAE4D5",bd=5)
    frameEstantesIngresar.grid(row=1,column=0,sticky="nsew")
    frameEstantesIngresar.columnconfigure(1, weight=1)

    frameEstantesImprimir = tk.Frame(frameEstantesContenido,bg="#EAE4D5",bd=5)
    frameEstantesImprimir.grid(row=1,column=3,sticky="nsew")
    frameEstantesImprimir.columnconfigure(1, weight=1)

    frameBotones = tk.Frame(ventanaEstantes, bg="#EAE4D5",bd=5)
    frameBotones.grid(row=2,column=0,sticky="nsew")
    frameBotones.columnconfigure(0,weight=1)
    frameBotones.columnconfigure(1,weight=1)
    frameBotones.columnconfigure(2,weight=1)
    frameBotones.columnconfigure(3,weight=1)

    #CRUD WINDOW TITLE

    titulo= tk.Label(frameEstantesContenido, text="ESTANTES", font=("Palatino Linotype", 20, "bold"), bg="#EAE4D5", fg="#213555")
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
def abrirUsuarios(Ventana_principal):
    Ventana_principal.withdraw()
    ventana_usuarios = tk.Toplevel(bg="#EAE4D5")
    ventana_usuarios.title("Gestión de Usuarios")
    ventana_usuarios.geometry("500x800")

    titulo= tk.Label(ventana_usuarios, text="USUARIOS", font=("Palatino Linotype", 20, "bold"), bg="#EAE4D5", fg="#213555")
    titulo.pack(pady=20)

    #Secondary Buttons inside
    AgregarUsuario= tk.Button(ventana_usuarios, text="Agrega", width=25, height=2, font=("Palatino Linotype", 14), bg="#B6B09F")
    AgregarUsuario.pack(pady=10)

    ModificarUsuarios= tk.Button(ventana_usuarios, text="Modificar", width=25, height=2, font=("Palatino Linotype", 14), bg="#B6B09F")
    ModificarUsuarios.pack(pady=10)

    BuscarUsuario=tk.Button(ventana_usuarios, text="Buscar", width=25, height=2, font=("Palatino Linotype", 14), bg="#B6B09F")
    BuscarUsuario.pack(pady=10)

    EliminarUsuario= tk.Button(ventana_usuarios, text="Eliminar", width=25, height=2, font=("Palatino Linotype", 14), bg="#B6B09F")
    EliminarUsuario.pack(pady=10)
    #Volver Button
    volver=tk.Button(ventana_usuarios, text="VOLVER AL MENÚ", command=lambda: [ventana_usuarios.destroy(), Ventana_principal.deiconify()], bg="#213555",fg="white", font=("Palatino Linotype", 12)).pack(pady=20)




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