i = 1
while i < 11:
    num= int(input('Ingrese un numero'))
    if (num % 2) == 0:
        print("{0} es par".format(num))
    else:
        print("{0} es impar".format(num))
    i += 1