class ManejaHelados (object):
    def __init__ (self):
        self.__lista = []
    
    def AgregarHelado (self,Helado):
        self.__lista.append(Helado)

    def Item2Mostrar (self,numero):
        numeros={}
        for i in range (1,numero+1):
            numeros[i]=0
        for helado in self.__lista:
            sabores=helado.getSabor()
            for sabor in sabores:
                numero=sabor.getNumero()
                numeros[numero]+=1
        dicOrdenado=sorted(numeros.items(),key=lambda x:x[1],reverse=True)
        lista5populares=[]
        if(len(dicOrdenado)>5):
            lista5populares=dicOrdenado[0:5]
        else:
            lista5populares=dicOrdenado
        return lista5populares
    
    def saboresvendidos (self):
        for sabor in self.__lista:
            nombre = sabor.getSabor()
            for nom in nombre:
                print(nom.getNombre())

    def EstimarGramos (self, numeroesabor):
        estimar = []
        for helado in self.__lista:
            busca = helado.buscarSabor(numeroesabor)
            if busca != -1:
                estimar.append(busca)
            else:
                print("Error..")
        i=0
        gramo = 0
        while i<len(estimar):
            gramo+=int(estimar[i].getGramo())/int(estimar[i].getLenlista())
            i+=1
        print("La cantidad de gramos es de: ",gramo)

    def BuscarSaboresxGramos (self,tipo):
        listaNombres = []
        for helado in self.__lista:
            if tipo == int(helado.getGramo()):
                sabores = helado.getSabor()
                for sabor in sabores:
                    nombre = sabor.getNombre()
                    if(not(nombre in listaNombres)):
                        listaNombres.append(nombre)
        return listaNombres
    
    def LenSabor (self):
        for i in self.__lista:
            print(i.getLenlista())
