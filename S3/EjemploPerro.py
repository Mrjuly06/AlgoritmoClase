class Perro:
    def __init__(self, nombre, raza, altura):
        self.nombre = nombre
        self.raza = raza
        self.altura = altura

    def comer(self):
        return "El perro está comiendo"

    def dormir(self):
        return "El perro está durmiendo"

    def ladrar(self):
        return "El perro está ladrando"

firu = Perro("Firulai", "Pastor alemán", 0.6)

print(firu.nombre)       # Firulai
print(firu.raza)         # Pastor alemán
print(firu.altura)       # 0.6
print(firu.comer())      # El perro está comiendo
print(firu.dormir())     # El perro está durmiendo
print(firu.ladrar())     # El perro está ladrando
