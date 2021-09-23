edades = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

mapa_edades = {}

for edad in edades:
    if edad in mapa_edades:
        mapa_edades[edad] += 1
    else:
        mapa_edades[edad] = 1

for valor in sorted(mapa_edades):
    print(f'{valor}: {"*"*mapa_edades[valor]}')
