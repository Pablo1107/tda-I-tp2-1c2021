class Grafo():
    def __init__(self, raiz):
        self.raiz = raiz
        self.aristas = list()
        self.vertices = set()
        self.agregar_vertice(raiz)

    def agregar_vertice(self, vertice):
        self.vertices.add(vertice)

    def agregar_arista(self, origen, destino, peso = 1):
        self.aristas.append((origen, destino, peso))
        self.agregar_vertice(origen)
        self.agregar_vertice(destino)

    def peso(self, origen, destino):                     # O(E)
        for arista in self.aristas:
            if arista[0] == origen and arista[1] == destino:
                return arista[2]
        return None
    
def Bellman_Ford(grafo, origen):
    dist = {}
    predecesores = {}

    # Inicializar distancias en infinito
    for v in grafo.vertices:
        dist[v] = float("inf") 

    # Inicializar distancias al origen en cero y 
    dist[origen] = 0
    predecesores[origen] = None

    # Ejecutar por cada vertice
    for _ in grafo.vertices:
        cambio = False
        for v, w, peso in grafo.aristas:
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
    visitados = set()
    for v, w, peso in grafo.aristas:
        if dist[v] + peso < dist[w]:
            predecesor = predecesores[v]

            visitados.add(v)
            while predecesor not in visitados:
                visitados.add(predecesor)
                predecesor = predecesores[predecesor]

            arista_actual = predecesor
            while predecesor not in ciclo:
                ciclo.append(predecesor)
                arista_actual = predecesor
                predecesor = predecesores[predecesor]
                peso_actual = grafo.peso(predecesor, arista_actual)
                peso_ciclo += peso_actual

            return ciclo[::-1], peso_ciclo
