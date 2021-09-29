def opciones(primeraopcion):
    opcion = ["solicitar moneda","cantidad a recibir","codigo"]
    return primeraopcion in opcion

lasopciones=[]
i=0

while i <=3:
    print("que opcion desea realizar: ")
    opcion=input("recibir cantidad, transferir monto, mostrar balance de una moneda, mostrar balance general, mostrar historico de transacciones, salir de programa: ")
    while not opciones(opcion):
        print("opcion invalida.")
        lasopciones =input("ingrese correctamente la opcion a realizar: ")




