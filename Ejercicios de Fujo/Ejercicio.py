def generar_lista_impares():
    return [i for i in range(1, 20, 2)]

def calcular_suma(lista):
    return sum(lista)

def calcular_producto(lista):
    producto = 1
    for num in lista:
        producto *= num
    return producto

def main():
    lista_impares = generar_lista_impares()
    
    while True:
        print("\nMenú de opciones:")
        print("a) Introducir un valor entero impar entre 1 y 19 (Se genera automáticamente)")
        print("b) Calcular la serie numérica 1 + 3 + 5 + ... + n")
        print("c) Calcular 1 * 3 * 5 * ... * n")
        print("d) Salir del programa")
        
        opcion = input("Seleccione una opción (a, b, c, d): ").lower()
        
        if opcion == "a":
            print(f"Lista de números impares: {lista_impares}")
        elif opcion == "b":
            print(f"La suma de la serie es: {calcular_suma(lista_impares)}")
        elif opcion == "c":
            print(f"El producto de la serie es: {calcular_producto(lista_impares)}")
        elif opcion == "d":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    main()