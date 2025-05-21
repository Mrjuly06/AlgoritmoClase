# Clase para representar a un paciente
class Patient:
    # Constructor de la clase Patient (debe ser __init__, no _init_)
    def __init__(self, name, service_type):
        self.name = name                      # Nombre del paciente
        self.service_type = service_type      # Tipo de servicio solicitado por el paciente
    
    # Método para mostrar una representación legible del objeto Patient
    def __str__(self):
        return f"Paciente: {self.name}, Servicio: {self.service_type}"

# Clase para la cola de turnos de la farmacia
class PharmacyQueue:
    # Constructor de la clase PharmacyQueue (debe ser __init__, no _init_)
    def __init__(self):
        self.queue = []  # Se inicializa una lista vacía para almacenar los pacientes en cola
    
    # Método para agregar un paciente a la cola
    def add_patient(self, patient):
        self.queue.append(patient)  # Agrega el paciente al final de la cola
        print(f"{patient.name} ha sido agregado a la cola para {patient.service_type}.")
    
    # Método para atender al siguiente paciente en la cola
    def serve_next(self):
        if self.is_empty():  # Verifica si la cola está vacía
            return "No hay pacientes en la cola."
        patient = self.queue.pop(0)  # Extrae al primer paciente de la cola
        return f"Atendiendo a {patient.name} para {patient.service_type}."
    
    # Método para verificar si la cola está vacía
    def is_empty(self):
        return len(self.queue) == 0  # Retorna True si la cola está vacía, False si no
    
    # Método para mostrar todos los turnos pendientes
    def show_pending(self):
        if self.is_empty():  # Si no hay pacientes en la cola
            return "No hay turnos pendientes."
        result = "Turnos pendientes:\n"
        for i, patient in enumerate(self.queue, 1):  # Recorre la cola enumerando desde 1
            result += f"{i}. {patient}\n"  # Agrega la información de cada paciente al resultado
        return result  # Retorna la cadena con todos los turnos pendientes


# Función principal que controla el menú interactivo
def main():
    pharmacy = PharmacyQueue()  # Crea una instancia de PharmacyQueue
    valid_services = ["compra", "consulta", "receta"]  # Tipos de servicio válidos
    
    while True:  # Ciclo infinito hasta que el usuario decida salir
        # Menú de opciones
        print("\nSistema de Gestión de Turnos - Farmacia")
        print("1. Registrar nuevo paciente")
        print("2. Atender al siguiente paciente")
        print("3. Mostrar turnos pendientes")
        print("4. Salir")
        
        option = input("Seleccione una opción (1-4): ")  # Solicita la opción al usuario
        
        if option == "1":
            # Registrar nuevo paciente
            name = input("Ingrese el nombre del paciente: ")
            service = input("Ingrese el tipo de servicio (compra, consulta, receta): ").lower()
            if service in valid_services:
                pharmacy.add_patient(Patient(name, service))  # Agrega al paciente si el servicio es válido
            else:
                print("Error: Tipo de servicio inválido. Use compra, consulta o receta.")
        
        elif option == "2":
            # Atender al siguiente paciente
            print(pharmacy.serve_next())
        
        elif option == "3":
            # Mostrar turnos pendientes
            print("\n" + pharmacy.show_pending())
        
        elif option == "4":
            # Salir del programa
            print("Saliendo del sistema...")
            break
        
        else:
            # Mensaje de error si se ingresa una opción inválida
            print("Opción inválida, por favor seleccione 1, 2, 3 o 4.")

# Esta condición permite ejecutar la función main solo si este archivo se ejecuta directamente
if __name__ == "__main__":
    main()
