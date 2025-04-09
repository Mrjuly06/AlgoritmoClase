def calcular_importe(tipo_vehiculo, km, toneladas=0):
    tarifas = {
        "bicicleta": 100,
        "moto": 30 * km,
        "carro": 30 * km,
        "camion": (30 * km) + (25 * toneladas)
    }
    return tarifas.get(tipo_vehiculo, "Vehículo no válido")

# Solicitar datos al usuario
tipo_vehiculo = input("Ingrese el tipo de vehículo (bicicleta, moto, carro, camion): ").lower()
km = float(input("Ingrese la cantidad de kilómetros recorridos: "))
toneladas = 0

if tipo_vehiculo == "camion":
    toneladas = float(input("Ingrese la cantidad de toneladas del camión: "))

importe = calcular_importe(tipo_vehiculo, km, toneladas)
print(f"El importe a pagar es: {importe} córdobas")
