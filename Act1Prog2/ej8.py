piezas= int(input('Ingrese la cantidad de piezas a procesar: '))
i= 1
piezasAptas= 0
while i <= piezas:
    longitud= float(input('Ingrese la longitud de la pieza: '))
    if longitud >= 1.20 and longitud <= 1.50:
        piezasAptas +=1
    i += 1

print('Las piezas aptas son: ' + str(piezasAptas))
