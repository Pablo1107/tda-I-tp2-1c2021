class Grafo():
    def __init__(self, es_dirigido = False, es_pesado = False):
        self.vertices = dict()
        self.es_dirigido = es_dirigido
        self.es_pesado = es_pesado

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
            self.agregar_vertice(self, origen)
        if destino not in self.vertices.keys():
            self.agregar_vertice(self, destino)

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
        return self.vertices[origen][destino]


def obterner_aristas(grafo):                             # O(V + E)
	aristas = []
	for v in grafo.obtener_vertices():
		for w in grafo.obtener_adyacentes(v):
			aristas.append(v, w, grafo.peso(v, w))
	return aristas

def Bellman_Ford(grafo, origen):
	dist = {}
	padres = {}
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
			return padres, dist              # ya convergio       

	for v, w, peso in aristas:               # Se hace una iteracion mas
		if dist[v] + peso < dist[w]:         # Si hay un cambio mas significa que
			return None                      # Hay un ciclo negativo

	return padres, dist               # Total O(V) + O(V + E) + O(V * E) = O(V * E)

# Este algoritmo sirve cuando hay aristas negativas
# Esto sirve para todos los grafos, pero como tarda mucho mas que Dijkstra no se usa
# Solo combiene cuando es un grafo dirigido que admite aristas negativas
# Tambien sirve para detectar ciclos negativos