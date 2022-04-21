from collections import defaultdict

class Grafo():
    def __init__(self, raiz, es_dirigido = False):
        self.vertices = defaultdict(dict)
        self.aristas = defaultdict(dict)
        self.es_dirigido = es_dirigido
        self.raiz = raiz

    def agregar_vertice(self, vertice):
        self.vertices[vertice] = dict()

    def agregar_arista(self, origen, destino, peso = 1):
        self.aristas[(origen, destino)] = int(peso)
        adyacentes = self.vertices[origen]
        adyacentes[destino] = int(peso)

        if not self.es_dirigido:
            self.aristas[(destino, origen)] = int(peso)
            adyacentes_destino = self.vertices.get(destino)
            adyacentes_destino[origen] = int(peso)

        return True
    
    def borrar_vertice(self, vertice):
        if vertice not in self.vertices:
            return False

        for v in self.vertices:
            try:
                del self.vertices[v][vertice]
            except KeyError:
                pass

        del self.vertices[vertice]

        for arista in self.aristas:
            if vertice in arista:
                self.aristas.remove(arista)

        return True

    def borrar_arista(self, origen, destino):
        try:
            del self.aristas[(origen, destino)]
            del self.vertices[origen][destino]
            if not self.es_dirigido:
                del self.vertices[destino][origen]
            return True
        except KeyError:
            return False

    def son_adyacentes(self, origen, destino):
        adyacente = (origin, destino) in self.aristas
        if self.es_dirigido:
            return adyacente
        else:
            return adyacente or (destino, origin) in self.aristas

    def existe_vertice(self, vertice):
        return vertice in self.vertices

    def obtener_vertices(self): # O(n)
        return tuple(self.vertices.keys())

    def obtener_aristas(self): # O(1)
        return self.aristas

    def obtener_adyacentes(self, vertice):
        if vertice not in self.vertices.keys():
            return None
        return self.vertices[vertice].keys()

    def peso(self, origen, destino):
        if origen not in self.vertices or \
           destino not in self.vertices[origen]:
            return None

        return self.vertices[origen][destino]

    def __len__(self):
        return len(self.vertices)

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.vertices))

def Bellman_Ford(grafo, origen):                         # O(V * E)
    vertices = grafo.obtener_vertices()                  # O(V)
    aristas = grafo.obtener_aristas()                    # O(1)
    dist = {}
    predecesores = {}

    # Inicializar distancias en infinito
    for v in grafo.obtener_vertices():                   # O(V)
        dist[v] = float("inf") 

    # Inicializar distancias al origen en cero y 
    dist[origen] = 0
    predecesores[origen] = None

    # Ejecutar por cada vertice
    for _ in vertices:                                   # O(V * E)
        cambio = False
        for (v, w), peso in aristas.items():             # O(E)
            if dist[v] + peso < dist[w]:
                cambio = True
                predecesores[w] = v
                dist[w] = dist[v] + peso

        if not cambio:
            return

    # Chequear si hay ciclos negativos
    # y calcular dicho ciclo y su peso
    ciclo = []
    peso_ciclo = 0
    for (v, w), peso in aristas.items():                 # O(E)
        if dist[v] + peso < dist[w]:
            ciclo.append(v)
            arista_actual = v
            predecesor = predecesores[v]
            peso_ciclo = grafo.peso(predecesor, arista_actual)

            while predecesor != v:
                ciclo.append(predecesor)
                arista_actual = predecesor
                predecesor = predecesores[predecesor]
                peso_actual = grafo.peso(predecesor, arista_actual)
                peso_ciclo += peso_actual

            return ciclo[::-1], peso_ciclo               # O(V)
