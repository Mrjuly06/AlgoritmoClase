# Clase que representa una estación
class Station:
    def __init__(self, name, time_to_next):
        self.name = name
        self.time_to_next = time_to_next
        self.next = None

# Clase que representa la ruta como una lista enlazada
class Route:
    def __init__(self):
        self.head = None

    def add_station(self, name, time_to_next):
        new_station = Station(name, time_to_next)
        if not self.head:
            self.head = new_station
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_station

    def show_route(self):
        stations = []
        current = self.head
        while current:
            stations.append(current.name)
            current = current.next
        return ' -> '.join(stations)

    def estimated_time(self, start_name, end_name):
        current = self.head
        total_time = 0
        found_start = False

        while current:
            if current.name == start_name:
                found_start = True

            if found_start:
                if current.name == end_name:
                    return f"Tiempo estimado de {start_name} a {end_name}: {total_time} minutos"
                total_time += current.time_to_next

            current = current.next

        return "Origen o destino no encontrados en la ruta."

# Crear la ruta
my_route = Route()

# Ingresar estaciones desde consola
num_stations = int(input("¿Cuántas estaciones quieres agregar?: "))

for i in range(num_stations):
    name = input(f"Ingrese el nombre de la estación {i+1}: ")
    if i < num_stations - 1:
        time_to_next = int(input(f"Ingrese minutos hasta la siguiente estación: "))
    else:
        time_to_next = 0  # última estación, no hay siguiente
    my_route.add_station(name, time_to_next)

# Mostrar ruta completa
print("\nRuta completa:")
print(my_route.show_route())

# Consultar tiempos entre estaciones
while True:
    print("\nConsulta de tiempo estimado")
    start = input("Ingresa estación de origen: ")
    end = input("Ingresa estación de destino: ")
    print(my_route.estimated_time(start, end))

    again = input("¿Quieres hacer otra consulta? (s/n): ").lower()
    if again != 's':
        break

print("Programa finalizado.")
