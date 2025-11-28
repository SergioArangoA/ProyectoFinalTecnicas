from Data.ManejoListasMaestras import inventarioOrdenado
class Estante:
    """An Estante instance represents a book shelf in the library.
    
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

    estanteriaDeficiente():This algorithm finds and lists all possible combinations of four books that, when their weight in kg is added together,
    exceed a "risk" of 8kg"""
    
    def __init__(self, id: str, librosEnEstante: list):
        self.__id = id #__id, quiere decir que la variable es privada. Es decir, que no
        #puedes acceder a ella directamente. Esto lo hago, para que al cambiar el nombre
        #del stand, se puedan actualizar de inmediato en los libros del stand el nuevo
        #nombre del stand, así evitaremos errores más adelante
        self.librosEnEstante = librosEnEstante
        self.libroEnEstante: list[bool]= [] #Ask if the book in that position is on the shelf: if true that book is on the shelf, if false it's loaned out/borrowed
        
    def obtenerID(self):
        """This method returns the Id attribute"""
        return self.__id 
    
    def modificarID(self, nuevaID ):
        """This method allows to modifying the Id"""
        self.__id= nuevaID

    def objetoDiccionario(self):
        """Transforms the object to a dictionary"""
        return({"id": self.obtenerID(), "librosEnEstante": self.librosEnEstante})
    
    @classmethod #The method belongs to the class, not to an existing object.
    def diccionarioObjeto(clsEstante, diccionarioEstante):
        """Transforms dictionary to object"""
        return clsEstante(diccionarioEstante["id"], diccionarioEstante["librosEnEstante"], diccionarioEstante["libroEnEstante"])
    
"""Shelf Module"""

"""1. Brute force"""

def estanteriaDeficiente(inventarioOrdenado):
    """This algorithm finds and lists all possible combinations of four books that, when their weight in kg is added together, exceed a "risk" of 8kg"""
    listaLibrosEstanteriaDeficiente=[]
    #This list stores all the 4 books combinations that exceeds the 8kg risk
    
    for Libro1 in inventarioOrdenado: #A For for each book in the shelf (4)
        for Libro2 in inventarioOrdenado:
            for Libro3 in inventarioOrdenado:
                for Libro4 in inventarioOrdenado:
                    if Libro1.enInventario>0 and Libro2.enInventario>0 and Libro3.enInventario>0 and Libro4.enInventario>0:
                        #Verifies that the four books are available in the inventory
                        
                        if Libro1.peso+Libro2.peso+Libro3.peso+Libro4>8:
                            #If sum of the weights is above eight the books are added as a list in 'listaLibrosEstanteriaDeficiente'

                            listaLibrosEstanteriaDeficiente.append([Libro1,Libro2,Libro3,Libro4])      
                                                 
    if len(listaLibrosEstanteriaDeficiente) == 0: #If the cycles are done and the final lenght of store list is zero it means that there are'nt enough books 
        return "No hay suficientes libros" #This messaje shows on the open window 'ventanaEstanterias'
    return listaLibrosEstanteriaDeficiente #Returns the final list



  
        