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
sueldo = horas * valorhora
bonificacion_monto = sueldo * bonificacion
sueldo_neto = sueldo + bonificacion_monto
print("Su sueldo de este mes es:$", sueldo)
print("Su bonificacion de este mes es: ", bonificacion_monto)
print("Su sueldo neto es de: $", sueldo_neto)
#Aqui pedimos lo mismo que el punto anterior, con la diferencia que aqui calculamos su bonificacion, sueldo neto y bruto

#6: Del punto anterior, calcular y mostrar por pantalla el sueldo bruto, el monto a bonificar y el sueldo neto (bruto + bonif), considerando:
#a. Si trabajo más de 120hs, la bonificación es de %18
#b. Si trabajo entre 80 y 120 horas, la bonificación es de %15
#c. Si trabajo menos de 80 horas, la bonificación es de %13.