# Definir un nodo para la pila
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Definir la pila
class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
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
        return result[::-1]  # fondo a tope

# Método para separar pares e impares
def separarParImpar(stack):
    pares = Stack()
    impares = Stack()

    while not stack.is_empty():
        num = stack.pop()
        if num % 2 == 0:
            pares.push(num)
        else:
            impares.push(num)

    # Primero vaciar los impares, luego los pares (pares quedan abajo)
    result = Stack()
    while not pares.is_empty():
        result.push(pares.pop())
    while not impares.is_empty():
        result.push(impares.pop())

    return result

# Prueba
entrada = [2, 3, 6, 8, 11, 13, 18, 21]
pila = Stack()
for num in entrada:
    pila.push(num)

resultado = separarParImpar(pila)
print("Salida:", resultado.to_list())
