numero = 1
total = 0 
par = 0
impar = 0

while numero <= 10:
    print(numero)
    total += numero

    sera_par = numero // 2 * 2 == numero

    if sera_par:
        print("es un numero par :D")
        par += numero
    else:
        print("es un numero impar :C")
        impar += numero

    numero += 1

print("La suma total de todos los numeros es: ", total)
print("La suma total de los numeros pares es: ", par)
print("La suma total de los numeros impares es: ", impar)

#Aca se nos muestra cuales son los numeros pares, impares y la suma total de todos ellos

#11: Escribe un programa que muestre los números del 1 al 10. Además, el programa debe mostrar:
#a. Si es número es par o impar.
#b. Cuanto es la suma total de todos los números mostrados.
#c. Cuanto es la suma total de todos los números pares mostrados.
#d. Cuanto es la suma total de todos los números impares mostrados.