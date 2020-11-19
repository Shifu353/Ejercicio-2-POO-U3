class Helado (object):
    __gramos = None
    
    def __init__(self,gramo):
        self.__gramos = gramo
        self.__Sabor = []
    
    def getGramo (self):
        return self.__gramos

    def addSabor (self,sabor):
        self.__Sabor.append(sabor)
    def getSabor (self):
        return self.__Sabor
    
    def buscarSabor (self,numero):
        i = 0
        while i<len(self.__Sabor) and int(self.__Sabor[i].getNumero()) != numero:
            i+=1
        if i<len(self.__Sabor):
            print(self.__Sabor[i].getNombre())
            return self
        return -1
    def getLenlista(self):
        return len(self.__Sabor)
