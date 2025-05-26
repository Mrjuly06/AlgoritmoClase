from collections import deque

class Cola:
    def __init__(self):
        self.items = deque()

    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
        return self.items.popleft() if not self.esta_vacia() else None

    def esta_vacia(self):
        return len(self.items) == 0

    def tamano(self):
        return len(self.items)

    def mostrar(self):
        return list(self.items)
