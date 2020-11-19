class Sabor (object):
    __numero = 0
    __nombre = ""
    __descripcion = ""

    def __init__ (self,num,nom,descripcion):
        self.__numero = num
        self.__nombre = nom
        self.__descripcion = descripcion
        
    def getNumero (self):
        return self.__numero
    def getNombre (self):
        return self.__nombre
    def getDescripcion (self):
        return self.__descripcion
    
    def __str__ (self):
        return("Nombre: ",self.__nombre),"\n"
