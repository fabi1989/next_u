import os


clear = lambda: os.system('cls')

monedas = [
    'BTC',
    'BCC',
    'ETH',
    'XRP',
    'LTC',
    'ETC',
]


def recibir_cantidad():
    print('Recibir Cantidad!')
    print('-----------------')
    print('Tipos de moneda:')

    for moneda in monedas:
        print('1. ', moneda)
        
    tipo_de_moneda = input('Ingrese su tipo de moneda: ')
    print(tipo_de_moneda)

    cantidad_a_recibir =int(input("Cantidad a recibir es de: "))


def transferir_monto():
    print('Transferir Cantidad!')
    print('--------------------')
    print('Tipos de moneda: ')

    for moneda in monedas:
        print('1. ', moneda)
    
    tipo_de_moneda = input('Ingrese tipo de moneda: ')
    print(tipo_de_moneda)

    cantidad_a_enviar =int(input("Cantidad a enviar es de: "))

def mostrar_balance_una_moneda():
    print('Solicitar la moneda a mostrar')
    print('-----------------------------')
    print('Tipos de Monedas:')

    for moneda in monedas:
        print('1. ',moneda)

    tipo_de_moneda = input('Ingrese tipo de moneda: ')
    print(tipo_de_moneda)

def menu(mensaje = ''):
    clear()

    if (mensaje):
        print(mensaje)

    print('MENU PRINCIPAL!')
    print('---------------')
    print("1. Recibir Cantidad")
    print("2. Transferir Monto")
    print("3. Mostrar Balance una Moneda")
    print("4. Mostrar Balance General")
    print("5. Mostrar Historico de Transacciones")
    print("6. Salir")
    print('---------------')

    opcion = int(input('Ingrese su opcion: '))

    if opcion == 1:
        clear()
        recibir_cantidad()
    elif opcion == 2:
        clear()
        transferir_monto()
    elif opcion == 3:
        clear()
        mostrar_balance_una_moneda()
    elif opcion == 6:
        print("Gracias por nada!")
    else:
        menu("Esa opcion no existe, vuelva a ingresar su opcion.")


menu()
