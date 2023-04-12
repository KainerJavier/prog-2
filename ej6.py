empleados= int(input('Ingrese la cantidad total de empleados'))
i = 1
entre100Y300= 0
masDe300= 0
importeSueldos= 0
while i <= empleados:
    sueldo= int(input('Ingrese el sueldo del empleado'))
    if sueldo > 300:
        masDe300 += 1
    else:
        entre100Y300 += 1
    importeSueldos += sueldo
    i += 1

print('Empleados que cobran entre 100 y 300: ' + str(entre100Y300))
print('Empleados que cobran mas de 300: ' + str(masDe300))
print('El importe total de sueldos es: ' + str(importeSueldos))