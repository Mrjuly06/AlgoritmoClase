import collections

class Grafo:
    def __init__(self, es_dirigido=False):
        self.grafo = {}
        self.es_dirigido = es_dirigido

    def agregar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []

    def agregar_arista(self, u, v, peso=1):
        self.agregar_vertice(u)
        self.agregar_vertice(v)
        self.grafo[u].append((v, peso))
        if not self.es_dirigido:
            self.grafo[v].append((u, peso))

    def obtener_vecinos(self, vertice):
        if vertice in self.grafo:
            return [vecino for vecino, _ in self.grafo[vertice]]
        else:
            return []

    def existe_arista(self, u, v):
        if u in self.grafo:
            return any(vecino == v for vecino, _ in self.grafo[u])
        return False

    # --- Metodo para verificar si el grafo no dirigido es conexo ---
    def es_conexo(self):
        if not self.grafo:
            return True  
            # Un grafo vacio se considera conexo
            
        # Elegimos un vertice arbitrario como punto de partida
        inicio = next(iter(self.grafo))
        visitados = set()

        # Funcion recursiva DFS para visitar nodos
        def dfs(v):
            visitados.add(v)
            for vecino in self.obtener_vecinos(v):
                if vecino not in visitados:
                    dfs(vecino)

        dfs(inicio)
        # Comprobamos si todos los vertices fueron visitados
        
        return len(visitados) == len(self.grafo)

    # --- Metodo para encontrar un camino simple de inicio a fin usando BFS ---
    
    def encontrar_camino(self, inicio, fin):
        if inicio not in self.grafo or fin not in self.grafo:
            return []  
            # Uno de los vertices no existe

        visitados = set()
        padres = {}  
        # Para reconstruir el camino
        
        cola = collections.deque()

        cola.append(inicio)
        visitados.add(inicio)
        padres[inicio] = None  
        # El nodo inicial no tiene padre

        while cola:
            actual = cola.popleft()

            if actual == fin:
                # Reconstruimos el camino desde fin hacia inicio
                
                camino = []
                while actual is not None:
                    camino.append(actual)
                    actual = padres[actual]
                return camino[::-1]  
                # Devolver camino en orden correcto

            for vecino in self.obtener_vecinos(actual):
                if vecino not in visitados:
                    visitados.add(vecino)
                    padres[vecino] = actual
                    cola.append(vecino)

        return []  
        # No se encontro camino

grafo = Grafo(es_dirigido=False)

# Agregar aristas (los vertices se crean automaticamente)
aristas = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E')]
for u, v in aristas:
    grafo.agregar_arista(u, v)

# Verificar conectividad
print("¿El grafo es conexo?:", grafo.es_conexo())  

# Encontrar camino de A a E
camino1 = grafo.encontrar_camino('A', 'E')
print("Camino de 'A' a 'E':", camino1)

# Buscar camino a vertice inexistente
camino2 = grafo.encontrar_camino('A', 'Z')
print("Camino de 'A' a 'Z':", camino2)