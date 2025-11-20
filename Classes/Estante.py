
class Estante:
    """A Estante instance represents a bookStand in the library.
    
    Atributes:
    id(private str): Stand's id
    books(Books list [size 4])

    Methods:
    estanteDeficiente(): Checks the inventory, and looks for all the possible combinations of 
    4 books that aren't already in a stand and exceeds the 8kg weight limit.

    ObtenerID(): Returns the Id attribute

    SacarID (): Allows modifying the ID

    estanteOptimo(): Finds all the combinations of books that can be placed in the stand without
    exceeding the 8kg weight limit. It'll also search for the one that will have the highest
    combined value in COP. It will also print in console the proccess.

    objetoDiccionario(): This Method transform the object to a dictionary

    diccionarioObjeto(): Transforms dictionary to object

    """
    def __init__(self, id: str, bookList: list):
        self.__id = id #__id, quiere decir que la variable es privada. Es decir, que no
        #puedes acceder a ella directamente. Esto lo hago, para que al cambiar el nombre
        #del stand, se puedan actualizar de inmediato en los libros del stand el nuevo
        #nombre del stand, así evitaremos errores más adelante
        self.bookList = bookList

    def obtenerID(self):
        """This method returns the Id attribute"""
        return self.__id 
    
    def modificarID(self, nuevaID ):
        """This method allows to modifying the Id"""
        self.__id= nuevaID

    def objetoDiccionario(self):
        """Transforms the object to a dictionary"""
        return({"id": self.obtenerID(), "bookList": self.bookList})
    
    def diccionarioObjeto(diccionario):
        """Transforms dictionary to object"""
        return()
    
    ###HACER OTRO ATRIBUTO QUE SEA UNA LISTA DE BOOLEANOS QUE DIGA SI EL LIBRO EN ESA POSICION ESTA EN EL ESTANTE SI ES TRUE ESE LIBRO ESTA EN 
    #EL ESTANTE SI ES FALSE ESTA PRESTADO
        