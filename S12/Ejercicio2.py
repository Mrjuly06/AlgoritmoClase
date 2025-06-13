import collections

class Grafo:
    def __init__(self, es_dirigido=False):
        # Diccionario donde cada vértice tiene una lista de vecinos (con pesos opcionales)
        self.grafo = {}
        self.es_dirigido = es_dirigido
    
    def agregar_vertice(self, vertice):
        # Si el vértice no existe aún, lo agrega automáticamente con una lista vacía de vecinos
        if vertice not in self.grafo:
            self.grafo[vertice] = []
    
    def agregar_arista(self, u, v, peso=1):
        # Aseguramos que ambos vértices existan en el grafo
        self.agregar_vertice(u)
        self.agregar_vertice(v)
        
        # Agregamos la arista de u a v
        self.grafo[u].append((v, peso))
        
        # Si el grafo no es dirigido, también agregamos la arista de v a u
        if not self.es_dirigido:
            self.grafo[v].append((u, peso))
            
    def obtener_vecinos(self, vertice):
        # Devolvemos solo los nombres de los vecinos (ignoramos pesos aquí)
        if vertice in self.grafo:
            return [vecino for vecino, _ in self.grafo[vertice]]
        else:
            return []
    
    def existe_arista(self, u, v):
        # Verificamos si hay una arista de u a v
        if u in self.grafo:
            return any(vecino == v for vecino, _ in self.grafo[u])
        return False
    
    def bfs(self, inicio):
        if inicio not in self.grafo:
            print(f"Error: el vértice '{inicio}' no existe.")
            return []
        
        visitados = set()                # Conjunto para marcar los vértices visitados
        cola = collections.deque()       # Cola para el recorrido BFS
        recorrido = []                   # Lista para almacenar el orden de visita
        
        cola.append(inicio)
        visitados.add(inicio)
        
        while cola:
            actual = cola.popleft()      # Sacamos el primer vértice de la cola
            recorrido.append(actual)
            
            for vecino in self.obtener_vecinos(actual):
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)
        
        return recorrido
    
    def dfs(self, inicio):
        if inicio not in self.grafo:
            print(f"Error: el vértice '{inicio}' no existe.")
            return []
        
        visitados = set()                # Conjunto para marcar vértices visitados
        recorrido = []                   # Lista para almacenar el orden de visita
        
        # Función recursiva interna
        def _dfs_recursivo(vertice):
            visitados.add(vertice)
            recorrido.append(vertice)
            
            for vecino in self.obtener_vecinos(vertice):
                if vecino not in visitados:
                    _dfs_recursivo(vecino)
        
        _dfs_recursivo(inicio)
        return recorrido

# Crear grafo no dirigido
grafo = Grafo(es_dirigido=False)

# Agregar aristas (los vértices se crean automáticamente)
aristas = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E')]
for u, v in aristas:
    grafo.agregar_arista(u, v)
    
# Agregar un vértice aislado (desconectado)
grafo.agregar_vertice('F')

# Realizar BFS y DFS desde el vértice 'A'
print("Recorrido BFS desde 'A':", grafo.bfs('A'))
print("Recorrido DFS desde 'A':", grafo.dfs('A'))

# Realizar BFS y DFS desde el vértice aislado 'F'
print("Recorrido BFS desde 'F':", grafo.bfs('F'))
print("Recorrido DFS desde 'F':", grafo.dfs('F'))
