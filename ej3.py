i = 1
preguntas= int(input('Ingrese la cantidad de preguntas realizadas'))
respuestas= int(input('Ingrese la cantidad de respuestas correctas'))
porcentaje= (respuestas*100)/preguntas

if porcentaje >= 90:
    print('Nivel máximo')
elif porcentaje >= 75:
    print('Nivel medio')
elif porcentaje >= 50:
    print('Nivel regular')
else:
    print('Fuera de nivel')