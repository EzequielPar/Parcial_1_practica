
horas = (int(input("Ingrese la cantidad de horas trabajadas")))
if horas > 120:
    valorhora = 1500
elif horas >= 80:
    valorhora = 1300
else:
    valorhora = 1100
sueldo = horas * valorhora
print("Su sueldo de este mes es:$", sueldo)
#Aqui pedimos al usuario que ingrese sus horas trabajadas y luego calculamos cual es su sueldo en el mes.

#5:Escribe un programa que calcule el sueldo de un empleado basándose en la cantidad de horas y muestre por pantalla el resultado, considerando lo siguiente:
#a. Si trabajo más de 120hs por mes, la hora tiene un valor de $1500.
#b. Si trabajo entre 80 y 120hs por mes, la hora tiene un valor de $1300.
#c. Si trabajo menos de 80 horas por mes, la hora tiene un valor de $1100.