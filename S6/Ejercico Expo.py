# Clase que representa una estación 
class Station:
    def __init__(self, name, time_to_next):
        self.name = name  # nombre de la estación
        self.time_to_next = time_to_next  # tiempo en minutos hacia la siguiente estación
        self.next = None  # referencia a la siguiente estación


# Clase que representa la ruta como una lista enlazada
class Route:
    def __init__(self):
        self.head = None  # inicio de la ruta

    # Método para agregar estaciones a la ruta
    def add_station(self, name, time_to_next):
        new_station = Station(name, time_to_next)
        if not self.head:
            self.head = new_station
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_station

    # Mostrar todas las estaciones de la ruta
    def show_route(self):
        stations = []
        current = self.head
        while current:
            stations.append(current.name)
            current = current.next
        return ' -> '.join(stations)

    # Calcular tiempo estimado desde una estación origen hasta una estación destino
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

# Agregar estaciones y sus tiempos hacia la siguiente estación
my_route.add_station("Estación A", 5)
my_route.add_station("Estación B", 7)
my_route.add_station("Estación C", 4)
my_route.add_station("Estación D", 6)
my_route.add_station("Estación E", 3)  # última estación, tiempo a siguiente es 0

# Mostrar ruta completa
print("Ruta:", my_route.show_route())

# Calcular tiempo estimado entre dos estaciones
print(my_route.estimated_time("Estación B", "Estación E"))
print(my_route.estimated_time("Estación A", "Estación C"))
print(my_route.estimated_time("Estación C", "Estación E"))