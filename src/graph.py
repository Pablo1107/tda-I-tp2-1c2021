class Grafo():
    def __init__(self, raiz, es_dirigido = False, es_pesado = False):
        self.vertices = dict()
        self.es_dirigido = es_dirigido
        self.es_pesado = es_pesado
        self.raiz = raiz

    def __len__(self):
        return len(self.vertices)

    def agregar_vertice(self,vertice):
        if vertice not in self.vertices.keys():
            self.vertices[vertice] = dict()
            return True
        else :
            return False

    def agregar_arista(self, origen, destino, peso = 1):
        if origen not in self.vertices.keys():
            self.agregar_vertice(origen)
        if destino not in self.vertices.keys():
            self.agregar_vertice(destino)

        ady = self.vertices.get(origen)
        ady[destino] = peso

        if not self.es_dirigido:
            ady2 = self.vertices.get(destino)
            ady2[origen] = peso
        return True
    
    def borrar_vertice(self, vertice):
        if vertice not in self.vertices.keys():
            return False

        for v in self.vertices:
            if v in self.vertices[v].keys():
                del self.vertices[v][vertices]
        del  self.vertices[vertice]
        return True

    def borrar_arista(self, origen, destino):
        del self.vertices[origen][destino]
        if not self.es_dirigido:
            del self.vertices[destino][origen]

    def son_adyacentes(self, origen, destino):
        if destino in self.vertices[origen].keys():
            return True
        else:
            return False

    def existe_vertice(self,vertice):
        if vertice in self.vertices:
            return True
        else:
            return False

    def obtener_vertices(self):
        return tuple(self.vertices.keys())

    def obtener_adyacentes(self, vertice):
        if vertice not in self.vertices.keys():
            return None
        return tuple(self.vertices[vertice].keys())

    def peso(self, origen, destino):
        if origen not in self.vertices.keys():
            return None
        if destino not in self.vertices[origen].keys():
            return None
        return int(self.vertices[origen][destino])

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.vertices))

def obterner_aristas(grafo):                             # O(V + E)
    aristas = []
    for v in grafo.obtener_vertices():
        for w in grafo.obtener_adyacentes(v):
            aristas.append((v, w, grafo.peso(v, w)))
    return aristas

def Bellman_Ford(grafo, origen):
    dist = {}
    padres = {}
    ciclo = []
    peso_ciclo = 0
    for v in grafo.obtener_vertices():                   # O(V)
        dist[v] = float("inf") 
    dist[origen] = 0
    padres[origen] = None
    aristas = obterner_aristas(grafo)                    # O(V + E)
    for i in range(len(grafo.obtener_vertices())):       # O(V * E)
        cambio = False
        for v, w, peso in aristas:
            if dist[v] + peso < dist[w]:
                cambio = True
                padres[w] = v
                dist[w] = dist[v] + peso

        if not cambio:                       # Si no cmabia en toda una pasada
            return None

    for v, w, peso in aristas:               # Se hace una iteracion mas
        if dist[v] + peso < dist[w]:
            from pprint import pprint

            print('v: ', v)
            print('w: ', w)

            ciclo.append(v)
            arista_actual = v
            padre = padres[v]
            peso_ciclo = grafo.peso(padre, arista_actual)

            while padre != v:
                ciclo.append(padre)
                arista_actual = padre
                padre = padres[padre]
                peso_actual = grafo.peso(padre, arista_actual)
                peso_ciclo += peso_actual

            return ciclo, peso_ciclo

    return None

# Este algoritmo sirve cuando hay aristas negativas
# Esto sirve para todos los grafos, pero como tarda mucho mas que Dijkstra no se usa
# Solo combiene cuando es un grafo dirigido que admite aristas negativas
# Tambien sirve para detectar ciclos negativos
