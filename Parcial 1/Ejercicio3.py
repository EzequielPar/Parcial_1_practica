dolar = (float(input("Ingrese la cantidad de dolares que desee convertir")))    #El usuario ingresa la cantidad que desee convertir. Ej: 7.99
tipo_convertir = input("Ingrese el tipo de cambio (blue/oficial): ")     #Ingresa el tipo de cambio
if tipo_convertir.lower() == "blue":
    cotizacion_endolares = 492.0
elif tipo_convertir.lower() == "oficial":
    cotizacion_endolares = 260.0
else:
    print("Tipo de cambio no valido. Intentelo nuevamente.")
    exit()
#Aqui podemos ver que utilize la funcion ".lower()", que su funcion es de convertir las cadenas de texto en minusculas, para que asi el programa lo pueda entender y ejecutar
#Bueno, pedimos que ingrese el tipo de cambio ya sea "blue" o "oficial". Si no es ingresado ninguna de esas 2 variantes, el programa indicara la finalizacion del programa utilizando "exit()" de otra manera daria error.
pesos = dolar * cotizacion_endolares
print(dolar, "Dolares equivalen a:", pesos, "pesos usando el tipo de cambio", tipo_convertir, ".")
#Y aqui daria el resultado, esto se hizo cuando el tipo de cambio estaba 492 y 260. Nose cuanto estara hoy 29/06 xd

#3:Escribe un programa que calcule la equivalencia a pesos de los dólares ingresados por pantalla. El programa debe preguntar el tipo de cambio a convertir (es decir, cuánto cotiza el dólar).