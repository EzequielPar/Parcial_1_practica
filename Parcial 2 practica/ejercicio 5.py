def buscar_numero(lista, numero):
    for indice, elemento in enumerate(lista):
        if elemento == numero:
            return indice  
    return -1  

def main():
    print("Búsqueda de un número en una lista")
    lista = [100, 200, 300, 400, 500, 600, 700, 800, 900, 2] 
    numero_buscar = int(input("Ingrese el número que desea buscar: "))
    indice_en = buscar_numero(lista, numero_buscar)
    if indice_en != -1:
        print("El número", numero_buscar, "se encuentra en el índice", indice_en ,"de la lista.")
    else:
        print("El número", numero_buscar ,"no se encontró en la lista.")

if __name__ == "__main__":
    main()