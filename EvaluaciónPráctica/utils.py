def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Registrar nuevo estudiante")
    print("2. Agregar calificación a un estudiante")
    print("3. Mostrar información de un estudiante")
    print("4. Mostrar todos los estudiantes")
    print("5. Salir")

def validar_edad(edad_str):
    if edad_str.isdigit() and int(edad_str) > 0:
        return int(edad_str)
    else:
        print("Edad inválida. Debe ser un entero positivo.")
        return None

def buscar_estudiante(nombre, lista):
    for estudiante in lista:
        if estudiante.nombre.lower() == nombre.lower():
            return estudiante
    return None