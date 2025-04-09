class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir_info(self):
        print(f"Nombre del estudiante: {self.nombre}")
        print(f"Nota del estudiante: {self.nota}")

    def resultado(self):
        if self.nota >= 70:
            print(f"{self.nombre} ha aprobado.")
        else:
            print(f"{self.nombre} ha reprobado.")

if __name__ == "__main__":

    nombre_estudiante = input("Ingrese el nombre del estudiante: ")
    nota_estudiante = float(input("Ingrese la nota del estudiante: "))

    estudiante = Estudiante(nombre_estudiante, nota_estudiante)


    estudiante.imprimir_info()
    estudiante.resultado()