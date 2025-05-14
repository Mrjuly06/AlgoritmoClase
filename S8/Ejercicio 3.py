from collections import deque

class TurnoFarmacia:
    def __init__(self):
        self.cola_turnos = deque()

    def registrar_paciente(self, nombre, servicio):
        paciente = {"nombre": nombre, "servicio": servicio}
        self.cola_turnos.append(paciente)
        print(f"Paciente {nombre} registrado para {servicio}.")

    def atender_paciente(self):
        if not self.esta_vacia():
            paciente = self.cola_turnos.popleft()
            print(f"Atendiendo a {paciente['nombre']} para {paciente['servicio']}.")
        else:
            print("No hay pacientes en espera.")

    def mostrar_turnos_pendientes(self):
        if not self.esta_vacia():
            print("\nTurnos pendientes:")
            for i, paciente in enumerate(self.cola_turnos, start=1):
                print(f"{i}. {paciente['nombre']} - {paciente['servicio']}")
        else:
            print("No hay turnos pendientes.")

    def esta_vacia(self):
        return len(self.cola_turnos) == 0

# Programa principal
farmacia = TurnoFarmacia()

while True:
    print("\n--- Gestión de Turnos en Farmacia ---")
    print("1. Registrar nuevo paciente")
    print("2. Atender siguiente paciente")
    print("3. Mostrar turnos pendientes")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del paciente: ")
        servicio = input("Ingrese el tipo de servicio (compra, consulta, receta): ")
        farmacia.registrar_paciente(nombre, servicio)
    elif opcion == "2":
        farmacia.atender_paciente()
    elif opcion == "3":
        farmacia.mostrar_turnos_pendientes()
    elif opcion == "4":
        print("Saliendo del sistema.")
        break
    else:
        print("Opción no válida. Intente nuevamente.")