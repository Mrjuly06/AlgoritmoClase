#Ejemplificacion de clase python
class Alumnos:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

    def saludar(self):
        print(f"Hola,{self.nombre} la edad es:{self.edad}")


alumnos=Alumnos(input("Digite un Nombre:"),int(input("ingrese la edad")))
#alumno.saludar()
Alumnos.saludar(alumnos)

