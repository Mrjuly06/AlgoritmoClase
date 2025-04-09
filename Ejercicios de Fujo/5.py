import math

def calcular_area(opcion):
    if opcion == 1:
        lado = float(input("Ingrese el lado del cuadrado: "))
        return lado * lado
    elif opcion == 2:
        radio = float(input("Ingrese el radio del círculo: "))
        return math.pi * radio * radio
    elif opcion == 3:
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        return base * altura
    elif opcion == 4:
        base1 = float(input("Ingrese la base mayor del trapecio: "))
        base2 = float(input("Ingrese la base menor del trapecio: "))
        altura = float(input("Ingrese la altura del trapecio: "))
        return (base1 + base2) * altura / 2
    elif opcion == 5:
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        return (base * altura) / 2
    else:
        return None

while True:
    print("=" * 40)
    print("CÁLCULO DE SUPERFICIES (versión 1.0)")
    print("=" * 40)
    print("1. Cuadrado\n2. Círculo\n3. Rectángulo\n4. Trapecio\n5. Triángulo")
    print("0. Salir")
    opcion = int(input("Seleccione una opción (0-5): "))
    
    if opcion == 0:
        print("Saliendo del programa...")
        break
    
    area = calcular_area(opcion)
    
    if area is not None:
        print(f"El área calculada es: {area:.2f}\n")
    else:
        print("Opción no válida. Intente de nuevo.\n")