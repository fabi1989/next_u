x = int(input("ingrese primero numero: "))
y = int(input("ingrese segundo numero: "))
z = int(input("ingrese tercer numero: "))
print("el maximo entre", x, ",", y, "y", z, "es", max(x, y, z), )


def max(a, b,):
    """ esta funcion calcula el maximo entre dos numeros"""

    if a >= b:
        maximo = a
    else:
        maximo = b
        return maximo
