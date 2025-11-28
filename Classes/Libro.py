from collections import deque
from Usuario import Usuario
class Libro:
    """A Libro instance represents a book in the library.

        Atributes:
            isbn (str): ISBN code 
            titulo (str): Book's title
            autor (str): Author's name
            peso (float): Weight(Kg) 
            precio (int): Price(COP)
            enInventario (int): Amount of books inside the library
            prestados (int): Amount of books borrowed
            listaEspera(deque-Array)= Wait list
            estantes (str []): List of strings with the names of the stands in which the book can be found

        Methods:

        imprimirDatos(): This method prints the Book attributes

        llenarListaEspera(): This method Fulls the wait List with Users

        libroADict(): This method converts an object book into a dictionary so it can be saved in JSON
    """
    #ListaEspera es el nombre del parámetro. Puede ser de tipo deque o None (esa barra | se lee como “o”).
    #El valor por defecto es None. Es decir: si no pasas nada al crear el objeto, ListaEspera será None.
    
    def __init__(self, isbn: str, titulo: str, autor: str, peso: float, precio: int, enInventario: int, prestados: int, listaEspera: deque | None = None):
        #con __innit_ definimos los atributos con los que se creara una instancia de la clase. Se especifícan todos los atributos que se importaran
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.peso = peso
        self.precio = precio
        self.enInventario = enInventario
        self.prestados = prestados
        self.listaEspera= listaEspera if listaEspera is not None else deque()
        self.estantes: list[str]= []
        #self.atributo = atributo 
        
    def imprimirDatos(self):
        """This method prints the book attributes"""
        return[self.isbn,self.titulo,self.autor,self.peso,self.precio,self.enInventario,self.prestados,self.estantes] #NO ESTA LISTA DE ESPERA
    
    def llenarListaEspera (self, usuario: Usuario ):
            """This method fulls the wait list. If enInventario=0 adds a User to the wait list"""
            if self.enInventario==0:
                 self.listaEspera.append(usuario.id)
    def libroADict(self):
        """This method converts an object book into a dictionary so it can be saved in JSON"""
        #listaEspera is converted from a deque to a  list for the JSON

        return ({"ISBN":self.isbn,"titulo": self.titulo,"autor": self.autor, "peso": self.peso,"precio": self.precio,
                "enInventario": self.enInventario, "prestados": self.prestados, "listaEspera": list(self.listaEspera), 
                "estantes": self.estantes
            })