def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "No se puede dividir por cero"
    return a / b

def main():
    print("Calculadora Modular")
    while True:
        print("Seleccione una operación:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        
        opcion = input("Ingrese el número de la operación que desea realizar: ")
        
        if opcion == '1':
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            resultado = suma(num1, num2)
            print(f"Resultado: {resultado}")
        elif opcion == '2':
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            resultado = resta(num1, num2)
            print(f"Resultado: {resultado}")
        elif opcion == '3':
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            resultado = multiplicacion(num1, num2)
            print(f"Resultado: {resultado}")
        elif opcion == '4':
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            resultado = division(num1, num2)
            print(f"Resultado: {resultado}")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()