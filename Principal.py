if __name__ == "__main__":
    from ClaseHelado import Helado
    from ClaseSabor import Sabor
    from ManejaHelados import ManejaHelados
    from ManejaSabores import ManejaSabores
    import csv,os
    archivo = open("sabores.csv")
    leer = csv.reader(archivo, delimiter=";")
    Mansabor = ManejaSabores()
    manejaHelado = ManejaHelados()
    for sabor in leer:
        Mansabor.addSabor(Sabor(int(sabor[0]),sabor[1],sabor[2]))
    archivo.close()
    def op1():
        os.system("cls")
        print("Nota los gramos del helado que se venden son de 100gr 150gr 250gr 500gr 1000gr.")
        try:
            gramos = int(input("Ingrese gramos del helado a vender: "))
            while gramos!=100 and gramos!=150 and gramos!=250 and gramos!=500 and gramos!=1000:
                print("El tipo del helado no es correcto, vuelva a ingresarlo..")
                gramos = int(input("Ingrese gramos del helado a vender: "))
            helado = Helado(gramos)
            print("Sabores que presenta la heladeria.")
            Mansabor.MostrarSabores()
            print("Nota solo puede ingresar 4 sabores, si desea menos sabores solo finalice con fin")
            sabores = input("Ingrese nombre del sabor: ")
            i=1
            while sabores.lower()!="fin":
                buscar = Mansabor.BuscarSabor(sabores)
                if buscar != -1:
                    helado.addSabor(buscar)   
                if i != 4:
                    i+=1
                    sabores = input("Ingrese nombre del sabor: ")
                else:
                    sabores="fin"
            manejaHelado.AgregarHelado(helado)
        except ValueError:
            print("Tipo de dato erroneo, vuelva a intentarlo")
        input("Toque una tecla para continuar..")
        os.system("cls")
    def op2 ():
        os.system("cls")
        numero = Mansabor.getNumero()
        sabores = manejaHelado.Item2Mostrar(numero)
        print("Mejores 5 Helados Vendidos")
        i=1
        for sabor in sabores:
            nombre = Mansabor.BuscarSabor(sabor[0])
            print(i,nombre.getNombre(),"cantidad: ",sabor[1])
            i+=1
        input("Toque una tecla para continuar..")
        os.system("cls")
    def op3():
        os.system("cls")
        try:
            numeroSabor = int(input("Ingrese un numero de sabor: "))
            buscarNumSabor = Mansabor.BuscarSabor(numeroSabor)
            if buscarNumSabor != -1:
                manejaHelado.EstimarGramos(buscarNumSabor.getNumero())
            else:
                print("No se encontro el numero del sabor")
        except ValueError:
            print("Tipo de dato incorrecto vuelva a intentarlo..")
        input("Toque una tecla para continuar..")
        os.system("cls")
    def op4():
        os.system("cls")
        try:
            gramo = int(input("Ingrese tipo de helado: "))
            while gramo != 100 and gramo != 150 and gramo != 250 and gramo!=500 and gramo!=1000:
                print("El tipo de gramo no es el correcto, vuelva a ingresarlo")
                gramo = int(input("Ingrese tipo de helado: "))
            obtenerlistadeSabores = manejaHelado.BuscarSaboresxGramos(gramo)
            if len(obtenerlistadeSabores) == 0:
                print("No se vendio ningun helado con ese gramo") 
            else:
                for nombre in obtenerlistadeSabores:
                    print(nombre)
        except ValueError:
            print("Tipo de dato incorrecto vuelva a intentarlo..")
        input("Toque una tecla para continuar..")
        os.system("cls")
    def op5 ():
        print("Cerrando....")
    def op99():
        manejaHelado.LenSabor()
    opcion = None
    diccionario = {1:op1,2:op2,3:op3,4:op4,5:op5,99:op99}
    while opcion != 5:
        print("|------------------------------------------------------------|")
        print("| Ingrese 1 para registrar una venta de helado               |")
        print("| Ingrese 2 para ver el nombre de los 5 sabores mas pedidos  |")
        print("| Ingrese 3 para estimar los gramos vendidos                 |")
        print("| Ingrese 4 para mostrar los sabores vendidos un tamaño dado |")
        print("| Ingrese 5 para cerrar programa                             |")
        print("|------------------------------------------------------------|")
        opcion = int(input("Ingrese Opcion: "))
        op = diccionario.get(opcion,lambda: print("Opcion Incorrecta"))
        op()
