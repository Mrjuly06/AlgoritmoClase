# Método para ordenar una pila de mayor a menor
def ordena(stack):
    aux_stack = Stack()

    while not stack.is_empty():
        temp = stack.pop()
        while not aux_stack.is_empty() and aux_stack.top.value > temp:
            stack.push(aux_stack.pop())
        aux_stack.push(temp)

    return aux_stack

# Prueba
entrada = [1, 3, 2, 4]
pila = Stack()
for num in entrada:
    pila.push(num)

resultado = ordena(pila)
print("Salida:", resultado.to_list())