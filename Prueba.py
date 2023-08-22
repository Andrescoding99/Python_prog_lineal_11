"""1) Lea un numero hasta que el usuario decida detenerse
2) Calcular el promedio de todos los numeros"""

#Asignacion de controladores

contro = True

#Asignacion de variables

num = 0
res = ""
tot = 0 #Total final

#Asignacion de acumuladores

acuN = 0

#Asignacion de contadores

contaN = 0

while contro:
    print("---------------------------------------------------------------------")
    print("Lectura de numeros")

    num = float(input("Digite el numero deseado: "))
    print("Su numero es: {}".format(num))
    contaN = contaN + 1
    acuN = acuN + num

    print("\nOpcion 1 No: n \nOpcion 2 Si: s")
    res = input("¿Desea continuar?: ")

    
    while res != "s" and res != "n":
        print("Ha ingresado una opcion invalida, vuelva a digitar su opcion")
        res = input("¿Desea continuar?: ")

    if res == "s":
        print("De vuelta a digitar")
        contro = True
    elif res == "n":
        print("Fin del programa")
        contro = False


print("La suma de todos los numeros fue {}".format(acuN))
print("El numero de rondas totales fue {}".format(contaN))

tot = acuN / contaN

print("El promedio final es {}".format(tot))
