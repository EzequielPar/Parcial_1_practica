cantidad_personas = int(input("Ingrese cantidad de personas: "))
edades = 0
cantidad = 0

while cantidad_personas > cantidad:
    edad = int(input("Ingrese edad: "))
    edades = edad / cantidad_personas
    cantidad += 1

print("Las personas ingresadas son: ", cantidad_personas)
print("El promedio de edades es de: ", edades)
print("Cantidad de persona: ", cantidad)

#El usuario ingresa la cantidad de personas que desee, les añade sus edades y al final del programa se muestra todas las personas y calcula promedio de edad.


#12: Escribe un programa que permita ingresar las edades de las personas, hasta que el usuario decida no hacerlo más, y muestre, al final, un promedio de las edades ingresadas y el total de personas ingresadas