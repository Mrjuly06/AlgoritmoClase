from ModuloVersion1 import Estudiante
from utils import mostrar_menu, validar_edad, buscar_estudiante

estudiantes = []

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Nombre del estudiante: ")
        edad_input = input("Edad: ")
        edad = validar_edad(edad_input)
        if edad is None:
            continue
        carrera = input("Carrera: ")
        nuevo = Estudiante(nombre, edad, carrera)
        estudiantes.append(nuevo)
        print("Estudiante registrado exitosamente.")

    elif opcion == "2":
        nombre = input("Nombre del estudiante: ")
        est = buscar_estudiante(nombre, estudiantes)
        if est:
            try:
                nota = float(input("Ingrese la calificación (0-100): "))
                est.agregar_calificacion(nota)
            except ValueError:
                print("Por favor, ingrese un número válido.")
        else:
            print("Estudiante no encontrado.")

    elif opcion == "3":
        nombre = input("Nombre del estudiante: ")
        est = buscar_estudiante(nombre, estudiantes)
        if est:
            est.mostrar_info()
        else:
            print("Estudiante no encontrado.")

    elif opcion == "4":
        if not estudiantes:
            print("No hay estudiantes registrados.")
        for est in estudiantes:
            est.mostrar_info()
            print("------------------")

    elif opcion == "5":
        print("Saliendo del programa. Hasta pronto!")
        break

    else:
        print("Opción no válida. Intente de nuevo.")
