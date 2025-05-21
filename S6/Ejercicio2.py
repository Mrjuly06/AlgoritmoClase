class Node:
    def _init_(self, value):
        self.value = value
        self.next = None

class Stack:
    def _init_(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        value = self.top.value
        self.top = self.top.next
        return value

    def is_empty(self):
        return self.top is None

    def to_list(self):
        current = self.top
        result = []
        while current:
            result.append(current.value)
            current = current.next
        return result[::-1]  # De fondo a cima

# Método para ordenar la pila de mayor (fondo) a menor (cima)
def ordena(stack):
    aux_stack = Stack()

    while not stack.is_empty():
        temp = stack.pop()
        while not aux_stack.is_empty() and aux_stack.top.value > temp:
            stack.push(aux_stack.pop())
        aux_stack.push(temp)

    return aux_stack

# Método para separar pares e impares: pares al fondo, impares en la cima
def separarParImpar(stack):
    pares = Stack()
    impares = Stack()

    while not stack.is_empty():
        valor = stack.pop()
        if valor % 2 == 0:
            pares.push(valor)
        else:
            impares.push(valor)

    # Primero ponemos los pares en la pila original (para que queden al fondo)
    resultado = Stack()
    temp = []
    while not pares.is_empty():
        temp.append(pares.pop())
    for val in reversed(temp):
        resultado.push(val)

    # Luego los impares encima
    temp = []
    while not impares.is_empty():
        temp.append(impares.pop())
    for val in reversed(temp):
        resultado.push(val)

    return resultado

# ========================
# Prueba de funcionamiento
# ========================

entrada = list(map(int, input("Ingresa los números separados por espacio: ").split()))
pila = Stack()
for num in entrada:
    pila.push(num)

# Elegir operación
opcion = input("¿Qué deseas hacer? (1 = separarParImpar, 2 = ordena): ")

if opcion == "1":
    resultado = separarParImpar(pila)
    print("Pila después de separar pares/impares:", resultado.to_list())
elif opcion == "2":
    resultado = ordena(pila)
    print("Pila ordenada de mayor a menor:", resultado.to_list())
else:
    print("Opción no válida.")