horas = (int(input("Ingrese la cantidad de horas trabajadas")))
if horas > 120:
    valorhora = 1500
    bonificacion = 0.18
elif horas >= 80:
    valorhora = 1300
    bonificacion = 0.15
else:
    valorhora = 1100
    bonificacion = 0.13
sueldo_bruto = horas * valorhora
bonificacion_monto = sueldo_bruto * bonificacion
sueldo_neto = sueldo_bruto + bonificacion_monto
print("Su sueldo de este mes es:$", sueldo_bruto)
print("Su bonificacion de este mes es: ", bonificacion_monto)
print("Su sueldo neto es de: $", sueldo_neto)

meses = 12 
horas_anuales = 0
sueldo_bruto_anual = 0
bonificacion_anual = 0 

mes = 1
while mes <= meses:
    horas = int(input("Ingrese sus horas trabajadas este mes: "))
    sueldo_bruto_anual += sueldo_bruto
    bonificacion_anual += bonificacion_monto
    horas_anuales += horas
    mes += 1
sueldo_anual = sueldo_bruto_anual + bonificacion_anual
if sueldo_anual > 2000000:
    descuento = 0.5
elif sueldo_anual <= 1000000 and sueldo_anual >= 2000000:
    descuento = 0.3
else:
    descuento = 0.1
descuento_anual = sueldo_anual * descuento
print("Su salario anual en bruto es: $", sueldo_bruto_anual)
print("Su bonificacion anual es de: ", bonificacion_anual)
print("Su sueldo anual es de: $", sueldo_anual)
print("Sus horas trabajadas en el año son: ", horas_anuales)

#Aqui lo mismo que en los 2 anteriores ejercicios, pero aqui calculamos sus horas en el año y sueldo anual

#7:Del punto anterior, y considerando que durante 12 meses el empleado trabajó las mismas cantidades de horas, escribe un programa que calcule el descuento anual a realizarse, considerando: 
#a. Si el sueldo anual es mayor a $2.000.000, el descuento es del %5.
#b. Si el sueldo anual esta entre $1.000.000 y $2.000.000, debe aplicarse un descuento del %3.
#c. Si el sueldo anual es menor a $1.000.000, debe aplicarse un descuento del %1. 
#d. El programa debe mostrar elsalario anual bruto, el monto anual de bonificaciones, el monto anual 
#a descontarse y las horas trabajadas en todo el año.