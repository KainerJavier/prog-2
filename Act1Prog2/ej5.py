datos= int(input('Ingrese la cantidad de datos que ingresará'))
alturas= 0
i = 1
while i <= datos:
    altura= int(input('Ingrese la altura'))
    alturas += altura
    i += 1

promedioAlturas= alturas//datos
print('El promedio de alturas es= ' + str(promedioAlturas) + ' cm')
