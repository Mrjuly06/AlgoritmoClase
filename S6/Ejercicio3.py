def convBinario(numero):
    if numero == 0:
        return [0]

    pila = Stack()

    while numero > 0:
        resto = numero % 2
        pila.push(resto)
        numero //= 2

    binario = []
    while not pila.is_empty():
        binario.append(pila.pop())

    return binario

# Prueba
numero = 12
print(f"Binario de {numero}:", convBinario(numero))