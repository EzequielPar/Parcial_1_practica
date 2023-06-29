cantidad_de_alumnos = int(input("Ingrese la cantidad de alumnos: "))
calificaciones_suma = 0 
contador = 0

while contador < cantidad_de_alumnos:
    calificacion = (float(input("Ingrese la calificacion del alumno: ")))
    calificaciones_suma += calificacion
    contador += 1

promedio_general_curso = calificaciones_suma / cantidad_de_alumnos

print("El promedio de general de la clase es: ", promedio_general_curso)

#En este programa calculamos el promedio general de los alumnos


#10: Escribe un programa que calcule el promedio general de una clase