def opciones(primeraopcion):
    opcion = ["solicitar moneda","cantidad a recibir","codigo"]
    return primeraopcion in opcion

lasopciones=[]
i=0

while i <=3:
    print("que opcion desea realizar: ")
    moneda=input("solicitar moneda, cantidad a recibir, codigo: ")
    while not opciones(moneda):
        print("opcion invalida.")
        lasopciones =input("ingrese correctamente la opcion a realizar: ")




