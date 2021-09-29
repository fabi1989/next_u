import os


clear = lambda: os.system('cls')

monedas = [
    'BTC',
    'DCC',
]


def recibir_cantidad():
    print('RECIBIR CANTIDAD!')
    print('----------')
    print('Tipos de moneda:')

    for moneda in monedas:
        print('1. ', moneda)

    tipo_de_moneda = input('Ingrese su tipo de moneda: ')
    print(tipo_de_moneda)


def transferir_monto():
    print('Transfiriendo monto')


def menu(mensaje = ''):
    clear()

    if (mensaje):
        print(mensaje)

    print('MENU PRINCIPAL!')
    print('----------')
    print("1. Recibir Cantidad")
    print("2. Transferir Monto")
    print("6. Salir")
    print('----------')

    opcion = input('Ingrese su opcion: ')

    if opcion == '1':
        clear()
        recibir_cantidad()
    elif opcion == '2':
        clear()
        transferir_monto()
    elif opcion == '6':
        print("Gracias por nada!")
    else:
        menu("Esa opcion no existe, vuelva a ingresar su opcion.")


menu()
