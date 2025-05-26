from clases.cola import Cola
from clases.separador import Separador

# Crear la cola original
cola = Cola()
for elemento in ['A', 'B', 'C', 'D', 'E']:
    cola.encolar(elemento)

# Instanciar y ejecutar el separador
separador = Separador(cola)
separador.separar_elementos()
resultado = separador.resultado()

# Mostrar resultados
print("Cola (pares):", resultado["Cola (pares)"])
print("Pila (impares):", resultado["Pila (impares)"])
