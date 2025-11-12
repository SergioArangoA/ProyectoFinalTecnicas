import tkinter as tk
from tkinter import ttk

"""VENTANA INVENTARIO SECUNDARIA"""
#SECONDARY INVENTORY WINDOW
def abrirInventario(Ventana_principal):
    #Create new window
        Ventana_principal.withdraw() #Hides the main window when the secondary window is opened
        ventana_inventario = tk.Toplevel(bg="#EAE4D5") #Toplevel creates a new secondary window and bg adds color
        """Toplevel crea una nueva ventana secundaria diferente a tk.TK solo puede haber 1 solo TK"""
        ventana_inventario.title("Gestión de Inventario")
        ventana_inventario.geometry("500x820")

        titulo= tk.Label(ventana_inventario, text="INVENTARIO", font=("Palatino Linotype", 20, "bold"), bg="#EAE4D5", fg="#213555")
        titulo.pack(pady=20)
    
        #Secondary Buttons inside

        InventarioGeneral= tk.Button(ventana_inventario, text="Inventario General", width=25, height=2, font=("Palatino Linotype", 14), bg="#B6B09F")
        InventarioGeneral.pack(pady=10)

        InventarioOrdenado= tk.Button(ventana_inventario, text="Inventario Ordenado", width=25, height=2, font=("Palatino Linotype", 14), bg="#B6B09F")
        InventarioOrdenado.pack(pady=10)

        """BOTÓN VOLVER: Cierra la ventana secundaria y vuelve a mostrar el menú principal"""
        #Volver Button: Closes the secondary window and shows the main menu again

        volver=tk.Button(ventana_inventario, text="VOLVER AL MENÚ", command=lambda: [ventana_inventario.destroy(), Ventana_principal.deiconify()], bg="#213555",fg="white", font=("Palatino Linotype", 12)).pack(pady=20)
        #.destroy() method closes the secondary window, 
        #.deiconify() method shows the main window agai
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

        
        '''
        Ventana_principal.withdraw()
        ventana_reservas = tk.Toplevel(bg="#EAE4D5")
        ventana_reservas.title("Gestión de Reservas")
        ventana_reservas.geometry("500x800")

        CampoTextoReserva = tk.Entry(ventana_reservas,font=("Palatino Linotype", 14),width=30,bg="#EAE4D5",relief="flat",bd=2)
        CampoTextoReserva.pack(pady=20)

        titulo= tk.Label(ventana_reservas, text="RESERVAS", font=("Palatino Linotype", 20, "bold"), bg="#EAE4D5", fg="#213555")
        titulo.pack(pady=20)
    
        #Secondary Buttons inside
        FrameBotones = tk.Frame(ventana_reservas, bg="#E2D9C8")
        FrameBotones.pack(pady=20)

        CrearReserva=tk.Button(ventana_reservas, text="Crear", width=25, height=2, font=("Palatino Linotype", 14), bg="#B6B09F")
        CrearReserva.pack(pady=10)

        Historial= tk.Button(ventana_reservas, text="Historial", width=25, height=2, font=("Palatino Linotype", 14), bg="#B6B09F") 
        Historial.pack(pady=10)

        ListaDeEspera= tk.Button(ventana_reservas, text="Lista de Espera", width=25, height=2, font=("Palatino Linotype", 14), bg="#B6B09F")
        ListaDeEspera.pack(pady=10)

        BuscarReserva= tk.Button(ventana_reservas, text="Buscar", width=25, height=2, font=("Palatino Linotype", 14), bg="#B6B09F")
        BuscarReserva.pack(pady=10)

        ModificarReserva= tk.Button(ventana_reservas, text="Modificar", width=25, height=2, font=("Palatino Linotype", 14), bg="#B6B09F")
        ModificarReserva.pack(pady=10)

        EliminarReserva= tk.Button(ventana_reservas, text="Eliminar", width=25, height=2, font=("Palatino Linotype", 14), bg="#B6B09F")
        EliminarReserva.pack(pady=10)
        #Volver Button
        volver=tk.Button(ventana_reservas, text="VOLVER AL MENÚ", command=lambda: [ventana_reservas.destroy(),Ventana_principal.deiconify()],bg="#213555",fg="white", font=("Palatino Linotype", 12)).pack(pady=20)

        canvas = tk.Canvas(FrameBotones)
        canvas.pack(side="left", fill="both", expand=True)
        
        scrollbar = ttk.Scrollbar(FrameBotones, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")
        '''

#SECONDARY SHELVES WINDOW
def abrirEstanterias(Ventana_principal):
    #Crete new window
        Ventana_principal.withdraw()
        ventana_estanterias = tk.Toplevel(bg="#EAE4D5")
        ventana_estanterias.title("Gestión de Estanterias")
        ventana_estanterias.geometry("500x800")

        titulo= tk.Label(ventana_estanterias, text="ESTANTERIAS", font=("Palatino Linotype", 20, "bold"), bg="#EAE4D5", fg="#213555")
        titulo.pack(pady=20)
    
        #Secondary Buttons inside
        CrearEstanteria= tk.Button(ventana_estanterias, text="Agregar", width=25, height=2, font=("Palatino Linotype", 14), bg="#B6B09F")
        CrearEstanteria.pack(pady=10)

        VerEstanterias= tk.Button(ventana_estanterias, text="Lista Estanterias", width=25, height=2, font=("Palatino Linotype", 14), bg="#B6B09F")
        VerEstanterias.pack(pady=10)

        ModificarEstanteria= tk.Button(ventana_estanterias, text="Modificar", width=25, height=2, font=("Palatino Linotype", 14), bg="#B6B09F")
        ModificarEstanteria.pack(pady=10)

        BuscarEstanteria=tk.Button(ventana_estanterias, text="Buscar", width=25, height=2, font=("Palatino Linotype", 14), bg="#B6B09F")
        BuscarEstanteria.pack(pady=10)

        EliminarEstanteria= tk.Button(ventana_estanterias, text="Eliminar", width=25, height=2, font=("Palatino Linotype", 14), bg="#B6B09F")
        EliminarEstanteria.pack(pady=10)
        #Volver Button
        volver=tk.Button(ventana_estanterias, text="VOLVER AL MENÚ", command=lambda: [ventana_estanterias.destroy(), Ventana_principal.deiconify()], bg="#213555",fg="white", font=("Palatino Linotype", 12)).pack(pady=20)
#SECONDARY USERS WINDOW
def abrirUsuarios(Ventana_principal):
    #Create new window
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
#SECONDARY BOOKS WINDOW
def abrirLibros(Ventana_principal):
    #Create new window
        Ventana_principal.withdraw()
        ventana_libros = tk.Toplevel(bg="#EAE4D5")
        ventana_libros.title("Gestión de Libros")
        ventana_libros.geometry("500x800")

        titulo= tk.Label(ventana_libros, text="LIBROS", font=("Palatino Linotype", 20, "bold"), bg="#EAE4D5", fg="#213555")
        titulo.pack(pady=20)

        #Text Entry Field
        CampoTextoISBN= tk.Entry(ventana_libros,font=("Palatino Linotype", 14),width=30,bg="#FFFFFF",relief="groove",bd=2)
        CampoTextoISBN.pack(pady=10)
        #relif="flat" makes the entry field flat without 3D borders, bd=2 sets the border width to 2 pixels
        """Entry indica que es un campo de texto donde el usuario puede escribir informacion"""

        CampoTextoAutor= tk.Entry(ventana_libros,font=("Palatino Linotype", 14),width=30,bg="#FFFFFF",relief="groove",bd=2)
        CampoTextoAutor.pack(pady=10)

        CampoTextoTitulo= tk.Entry(ventana_libros,font=("Palatino Linotype", 14),width=30,bg="#FFFFFF",relief="groove",bd=2)
        CampoTextoTitulo.pack(pady=10)
    
        #Secondary Buttons inside

        FrameBotones= tk.Frame(ventana_libros, bg="#E2D9C8") #Creates a frame to group buttons together
        FrameBotones.pack(side="bottom", pady=(0,10), expand=False)

        AgregarLibro= tk.Button(FrameBotones, text="Agregar", width=20, height=2,font=("Palatino Linotype", 14), bg="#B6B09F").grid(row=0, column=0, padx=10, pady=20)

        ModificarLibro= tk.Button(FrameBotones, ventana_libros, text="Modificar", width=20, height=2, font=("Palatino Linotype", 14), bg="#B6B09F").grid(row=0, column=1, padx=10, pady=20)

        BuscarLibro=tk.Button(FrameBotones, ventana_libros, text="Buscar", width=20, height=2, font=("Palatino Linotype", 14), bg="#B6B09F").grid(row=0, column=2, padx=10, pady=20)

        EliminarLibro= tk.Button(FrameBotones,ventana_libros, text="Eliminar", width=20, height=2, font=("Palatino Linotype", 14), bg="#B6B09F").grid(row=0, column=3, padx=10, pady=20)

        #Volver Button
        volver=tk.Button(ventana_libros, text="VOLVER AL MENÚ", command=lambda: [ventana_libros.destroy(), Ventana_principal.deiconify()], bg="#213555",fg="white", font=("Palatino Linotype", 12), width=20)
        volver.pack(side="bottom", pady=20)

        canvas = tk.Canvas(FrameBotones)
        canvas.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(FrameBotones, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")