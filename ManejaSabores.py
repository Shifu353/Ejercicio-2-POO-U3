class ManejaSabores (object):
    __sabores = []

    def __init__ (self):
        self.__sabores = []
    
    def addSabor (self,sabor):
        if sabor != None:
            self.__sabores.append(sabor)
        else:
            print("Hubo un error al agregar el sabor")
    def MostrarSabores (self):
        print("{}            {}               {}".format("Numero","Nombre del Sabor","Descripcion"))
        for sabor in self.__sabores:
            print("{}         {}                {}".format(sabor.getNumero(),sabor.getNombre(),sabor.getDescripcion()))
    
    def BuscarSabor (self,nombresabor):
        if type(nombresabor) != int:
            i=0
            while i<len(self.__sabores) and self.__sabores[i].getNombre().lower() != nombresabor:
                i += 1
            if i<len(self.__sabores):
                return self.__sabores[i]
            return -1
        else:
            j = 0
            while j<len(self.__sabores) and int(self.__sabores[j].getNumero()) != nombresabor:
                j+=1
            if j<len(self.__sabores):
                return self.__sabores[j]
            return -1
    def getNumero (self):
        return len(self.__sabores)
