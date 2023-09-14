def es_primo(numero):
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def encontrar_primos_en_rango(inicio, fin):
    primos = []
    for numero in range(inicio, fin + 1):
        if es_primo(numero):
            primos.append(numero)
    return primos

def main():
    print("Encontrar números primos en un rango")
    inicio = int(input("Ingrese el valor inicial del rango: "))
    fin = int(input("Ingrese el valor final del rango: "))
    
    if inicio < 0 or fin < 0 or fin < inicio:
        print("Por favor, ingrese valores válidos para el rango.")
        return
    
    numeros_primos = encontrar_primos_en_rango(inicio, fin)
    
    if len(numeros_primos) == 0:
        print(f"No se encontraron números primos en el rango de {inicio} a {fin}.")
    else:
        print(f"Números primos en el rango de {inicio} a {fin}:")
        print(numeros_primos)

if __name__ == "__main__":
    main()
