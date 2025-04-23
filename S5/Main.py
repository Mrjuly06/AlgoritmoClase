from lista_enlazada import ListaEnlazada

lista = ListaEnlazada()

while True:
    print("\n--- MENÚ ---")
    print("1. Insertar valor al final")
    print("2. Insertar valor al inicio")
    print("3. Eliminar valor")
    print("4. Buscar valor")
    print("5. Imprimir lista")
    print("6. Mostrar longitud de la lista")
    print("7. Verificar si la lista está vacía")
    print("8. Mostrar último valor")
    print("9. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        valor = int(input("Valor a insertar al final: "))
        lista.insertar(valor)
    elif opcion == "2":
        valor = int(input("Valor a insertar al inicio: "))
        lista.insertar_inicio(valor)
    elif opcion == "3":
        valor = int(input("Valor a eliminar: "))
        if lista.eliminar(valor):
            print("Valor eliminado.")
        else:
            print("Valor no encontrado.")
    elif opcion == "4":
        valor = int(input("Valor a buscar: "))
        if lista.buscar(valor):
            print("Valor encontrado.")
        else:
            print("Valor no está en la lista.")
    elif opcion == "5":
        lista.imprimir()
    elif opcion == "6":
        print("Longitud de la lista:", lista.longitudLista())
    elif opcion == "7":
        if lista.esta_vacia():
            print("La lista está vacía.")
        else:
            print("La lista no está vacía.")
    elif opcion == "8":
        ultimo = lista.ultimo_valor()
        if ultimo is None:
            print("La lista está vacía.")
        else:
            print("Último valor de la lista:", ultimo)
    elif opcion == "9":
        print("Saliendo del programa.")
        break
    else:
        print("Opción inválida. Intente de nuevo.")