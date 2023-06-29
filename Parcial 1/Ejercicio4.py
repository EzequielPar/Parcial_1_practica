alumno = input("Ingrese su Apellido:")
materia = (str(input("Ingrese materia:")))
parcial1 = (int(input("Ingrese nota del primer parcial: ")))
parcial2 = (int(input("Ingrese nota del segundo parcial: ")))
parcial3 = (int(input("Ingrese nota del tercer parcial: ")))
promedio_final = (parcial1 + parcial2 + parcial3) / 3
if promedio_final >= 6:
    print("Felicidades!", alumno, "Has aprobado la materia", materia, "con un promedio final de:", promedio_final)
else:
     promedio_final <= 6
     print(alumno, "Usted es un burro y debe recursar la materia", materia, "por tener un promedio de:", promedio_final)
#En este programa se le pide al usuario que ingrese su apellido, luego la materia y sus notas de dicha materia. Luego se calcula el promedio de dichas notas y el progrma muestra si el alumno recursa o no


#4:Escribe un programa que calcule el promedio final de una materia, basado en 3 notas de parciales, indicando por pantalla si el alumno aprobó o debe recursar la materia (se aprueba con 6). 