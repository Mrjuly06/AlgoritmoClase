import collections

class Grafo: 
    def __init__(self, es_dirigido=False):
        self.grafo = {}
        self.es_dirigido = es_dirigido
    
    def agregar_vertice(self, vertice):      
        '''Si el vertice no está en el diccionario,
        lo añade con un conjunto vacio de vecinos. '''
        if vertice not in self.grafo:
            self.grafo[vertice] = set()
            print(f"Vértice '{vertice}' agregado. ")
        else: 
            print(f"Vértice '{vertice}' ya existe. ")
    
    def agregar_arista(self, u, v, peso=1):
        #Asegure de que ambos vértices existen en el grafo
        self.agregar_vertice(u)
        self.agregar_vertice(v)
        
        #Añadir la arista
        self.grafo[u].add(v)
        print(f"Arista {u}  -> {v} agregada. ")
        
        #Si no es dirigido, añadir la arista en la direccion opuesta tambien
        if not self.es_dirigido:
            self.grafo[v].add(u)
            print(f"Arista {v} -> {u} (bidireccional) agregado")
    
    def obtener_vecinos(self, vertice):
        if vertice in self.grafo:
            return list(self.grafo[vertice])
            #Convertir a lista para devolver
        return []
        #Si el vertice no existe, no tiene vecinos
    
    def existe_arista(self, u, v):
        #Verifica si ambos vertcies existen y si 'v' esta en la lista de adyacencia de 'u'
        return u in self.grafo and v in self.grafo[u]
    
    def bfs(self, inicio):
        visitados = set()
        #Conjunto para guardar los vertices ya visitados
        cola = collections.deque()
        # cola para los vertices a visitar
        
        # Empezar el recorrido desde el vertice inicial
        cola.append(inicio)
        visitados.add(inicio)
        
        recorrido = []
        #Lista para almacenar el orden de visita
        
        while cola:
            vertice_actual = cola.popleft()
            #Sacar el primer elemento de la cola
            recorrido.append(vertice_actual)
            print(f"Visitando: {vertice_actual}")
            
            #Añadir a la cola los vecinos no visitados
            for vecino in self.obtener_vecinos(vertice_actual):
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)
        return recorrido
    
    def dfs(self, inicio):
        visitados = set()
        recorrido = []
        
        def _dfs_recursivo(vertice):
            visitados.add(vertice)
            recorrido.append(vertice)
            print(f"Visitado: {vertice}")
            
            for vecino in self.obtener_vecinos(vertice):
                if vecino not in visitados:
                    _dfs_recursivo(vecino)
        
        #Iniciar el DFS desde el vertice dado
        _dfs_recursivo(inicio)
        return recorrido
    
    def imprimir_grafo(self):
        print("\n---Representación del grafo---")
        for vertice, vecinos in self.grafo.items():
            print(f"{vertice}: {','.join(vecinos)}")
        print("-----------------------------")
    
    def es_conexo(self):
        if not self.grafo:
            return True
        
        #Tomar el primer vertice para iniciar el BFS/DFS
        primer_vertice = next(iter(self.grafo))
        
        #Realizar un BFS desde el primer vertice
        recorrido_bfs = self.bfs(primer_vertice)
    
    def encontrar_camino(self, inicio, fin):
        if inicio not in self.grafo or fin not in self.grafo:
            print(f"Error: '{inicio}' o '{fin}' no existen en el grafo. ")
            return []
    
        cola = collections.deque()
        visitados = set()
        padres = {}
        #Para recontstruir el camino: padres[Hijo] = padre
        
        cola.append(inicio)
        visitados.add(inicio)
        padres[inicio] = None
        #El inicio no tiene padre
        
        while cola:
            vertice_actual = cola.popleft()
            
            if vertice_actual == fin:
                #Hemos llegado al destino, reconstruir el camino
                camino = []
                temp = fin
                while temp is not None:
                    camino.append(temp)
                    temp = padres[temp]
                return camino[::-1]
                #Invertir el camino para que vaya de inicio a fin
            
            for vecino in self.obtener_vecinos(vertice_actual):
                if vecino not in visitados:
                    visitados.add(vecino)
                    padres[vecino] = vertice_actual
                    #GUardar el padre
                    cola.append(vecino)
    
        return []
        #No se encontro ningun camino

#--- EJECUCION DEL EJEMPLO COMPLETO ---
print("--- Creación de Grafo No dirigido ---")
mi_grafo = Grafo(es_dirigido=False)

mi_grafo.agregar_arista('Managua', 'Masaya')
mi_grafo.agregar_arista('Managua', 'León')
mi_grafo.agregar_arista('Masaya', 'Granada')
mi_grafo.agregar_arista('Granada', 'Rivas')
mi_grafo.agregar_arista('Managua', 'Granada')
#Arista adicional para mayor conectividad

mi_grafo.imprimir_grafo()

print("\n--- Operaciones Básicas ---")
print(f"Vecinos de Managua: {mi_grafo.obtener_vecinos('Managua')}")
print(f"¿Existe arista entre Managua y Masaya? {mi_grafo.existe_arista('Managua', 'Masaya')}")
print(f"¿Existe arista entre Managua y Rivas? {mi_grafo.existe_arista('Managua', 'Rivas')}")

print("\n--- Recorridos ---")
print(f"Orden de recorrido BFS desde Managua: {mi_grafo.bfs('Managua')}")
print(f"Orden de recorrido DFS desde Managua: {mi_grafo.dfs('Managua')}")

print("\n--- Conectividad y camino ---")
print(f"¿Es el grafo conexo? {mi_grafo.es_conexo()}")

camino = mi_grafo.encontrar_camino('Managua', 'Rivas')
print(f"Camino de Managua a Rivas: {camino}")

camino_inexistente = mi_grafo.encontrar_camino('Managua', 'Juigalpa')
print(f"Camino de Managua a Juigalpa: {camino_inexistente}")

# --- Probar con un grafo dirigido ---
print("\n--- Creación de Grafo Dirigido ---")
grafo_dirigido = Grafo(es_dirigido=True)
grafo_dirigido.agregar_arista('Inicio', 'A')
grafo_dirigido.agregar_arista('A', 'B')
grafo_dirigido.agregar_arista('B', 'C')
grafo_dirigido.agregar_arista('C', 'Fin')
grafo_dirigido.agregar_arista('Inicio', 'D')
grafo_dirigido.agregar_arista('D', 'Fin')

grafo_dirigido.imprimir_grafo()

print(f"Vecinos de Inicio (Dirigido): {grafo_dirigido.obtener_vecinos('Inicio')}")
print(f"Vecinos de Fin (dirigidos): {grafo_dirigido.obtener_vecinos('Fin')}")
#Deberia ser vacío
print(f"¿Existe arista de A y B? {grafo_dirigido.existe_arista('A', 'B')}")
print(f"¿Existe arista de B y A? {grafo_dirigido.existe_arista('B', 'A')}")
#Deberia ser False

print("\n--- Recorridos en Grafo Dirigido ---")
print(f"Orden de recorrido BFS desde Inicio: {grafo_dirigido.bfs('Inicio')}")
print(f"Orden de recorrido BFS desde Inicio: {grafo_dirigido.dfs('Inicio')}")

print("\n--- Conectividdad y caminos en Grafro Dirigido ---")
# es_conexo no es tan directamente aplicable a grafos dirigidos sin modificar la definicion
# pero podemos encontrar caminos

camino_dirigidos = grafo_dirigido.encontrar_camino('Inicio', 'Fin')
print(f"Camino dirigido de Inicio a Fin: {camino_dirigidos}")

camino_dirigido_no_existente = grafo_dirigido.encontrar_camino('Fin', 'Inicio')
print(f"Camino dirigido de Fin a Inicio: {camino_dirigido_no_existente}")