#!/usr/bin/env python3
import sys
from graph import Grafo

def leer_grafo(nombre_fichero):
    """
    Lee un grafo a partir de un fichero de texto.
    Devuelve un objeto de clase Graph
    """
    grafo = Grafo(es_dirigido=True,es_pesado=True)
    with open(nombre_fichero, 'r') as f:
        f.readline() # ignore first line
        for linea in f:
            linea = linea.rstrip()
            nodo1, nodo2, peso = linea.split(',')
            grafo.agregar_arista(nodo1, nodo2, peso)
    return grafo

def main(nombre_fichero):
    grafo = leer_grafo(nombre_fichero)
    print(grafo)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: {} <filename>'.format(sys.argv[0]))
        sys.exit(1)

    main(sys.argv[1])
