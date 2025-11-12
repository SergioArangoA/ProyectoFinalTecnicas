
class Estante:
    """A Estante instance represents a bookStand in the library.
    
    Atributes:
    id(private str): Stand's id
    books(Books list [size 4])

    Methods:
    riskyStand(): Checks the inventory, and looks for all the possible combinations of 
    4 books that aren't already in a stand and exceeds the 8kg weight limit.

    optimalStand(): Finds all the combinations of books that can be placed in the stand without
    exceeding the 8kg weight limit. It'll also search for the one that will have the highest
    combined value in COP. It will also print in console the proccess.

    """
    def __init__(self, id: str):
        self.__id = id #__id, quiere decir que la variable es privada. Es decir, que no
        #puedes acceder a ella directamente. Esto lo hago, para que al cambiar el nombre
        #del stand, se puedan actualizar de inmediato en los libros del stand el nuevo
        #nombre del stand, así evitaremos errores más adelante
        self.bookList = [4]

