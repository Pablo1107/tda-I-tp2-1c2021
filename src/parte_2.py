#!/usr/bin/env python3
import sys
from grafo import Grafo, Bellman_Ford

def leer_grafo(nombre_fichero):
    """
    Lee un grafo a partir de un fichero de texto.
    Devuelve un objeto de clase Grafo
    """
    
    with open(nombre_fichero, 'r') as f:
        raiz = f.readline()[0]
        grafo = Grafo(raiz)
        
        for linea in f:
            linea = linea.rstrip()
            nodo1, nodo2, peso = linea.split(',')
            grafo.agregar_arista(nodo1, nodo2, int(peso))
        return grafo

def main(nombre_fichero):
    grafo = leer_grafo(nombre_fichero)
    res = Bellman_Ford(grafo, grafo.raiz)
    if res:
        ciclos, costo = res
        ciclos = ','.join(ciclos)
        print(f'Existen al menos un ciclo negativo en el grafo. {ciclos} → costo: {costo}')
    else: 
        print('No existen ciclos negativos en el grafo')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: {} <filename>'.format(sys.argv[0]))
        sys.exit(1)

    main(sys.argv[1])
