cantidad_personas = int(input("Ingrese la cantidad de personas que usted desee: "))

contador = 0 

while contador < cantidad_personas:
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    edad = int(input("Ingrese edad: "))

    print("Nombre: ", nombre)
    print("Apellido: ", apellido)
    print("Edad: ", edad)

    contador += 1

print("Fin del Programa compadre.")


#Aqui lo mismo del programa anterior pero en esta vez el usuario decide cuantas personas agregar


#9:Escribe un programa que solicite y muestre por pantalla nombre, apellido y edad de una cantidad de personas ingresada por el usuario.