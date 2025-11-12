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
            estantes (str []): List of strings with the names of the stands in which the boook can be found
    """
    def __init__(self, isbn: str, titulo: str, autor: str, peso: float, precio: int, enInventario: int, prestados: int):
        #con __innit_ definimos los atributos con los que se creara una instancia de la clase. Se especifícan todos los atributos que se importaran
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.peso = peso
        self.precio = precio
        self.enInventario = enInventario
        self.prestados = prestados
        self.estantes = []
        #self.atributo = atributo 
        #Con self.atributo representamos el atributo del objeto, y con = atributo representamos que ese atributo será igual al que se importó en el constructor.
        
        
    def imprimirDatos(self):
        return[self.isbn,self.titulo,self.autor,self.peso,self.precio,self.enInventario,self.prestados,self.estantes]
    


    