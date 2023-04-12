i = 1
notasMayores= 0
notasMenores= 0
while i > 0:
    nota= int(input('Ingrese la nota'))
    if nota >= 7:
        notasMayores += 1
    elif nota < 7 and nota > 0:
        notasMenores += 1
    else:
        break

print(str(notasMayores) + " alumnos tienen una nota mayor o igual a 7")
print(str(notasMenores) + " alumnos tienen notas menores a 7")
        
