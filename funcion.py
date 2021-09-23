valid_alpha_user = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890-_."

while True:
    user = input("ingrese el nombre de usuario")
    if (len(user) > 4):
        a = set(valid_alpha_user)
        b = set(user)
        if len(b-a) > 0:
            print("usuario invalido.")
            continue
        else:
            print("usuario valido.")
            break
    else:
        print("usuario invalido.")
