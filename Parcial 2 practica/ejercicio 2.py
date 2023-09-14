def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def main():
    print("Conversor de temperatura")
    while True:
        print("Seleccione una opción:")
        print("1. Convertir de Celsius a Fahrenheit")
        print("2. Convertir de Fahrenheit a Celsius")
        print("3. Salir")
        
        opcion = input("Ingrese el número de la opción que desea: ")
        
        if opcion == '1':
            celsius = float(input("Ingrese la temperatura en grados Celsius: "))
            fahrenheit = celsius_a_fahrenheit(celsius)
            print(f"{celsius} grados Celsius son equivalentes a {fahrenheit} grados Fahrenheit.")
        elif opcion == '2':
            fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
            celsius = fahrenheit_a_celsius(fahrenheit)
            print(f"{fahrenheit} grados Fahrenheit son equivalentes a {celsius} grados Celsius.")
        elif opcion == '3':
            print("Gracias por usar el conversor de temperatura. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
