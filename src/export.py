#!/usr/bin/env python3
import sys
import graphviz
import parte_2

def main(nombre_archivo):
    grafo = parte_2.leer_grafo(nombre_archivo)

    dot = graphviz.Digraph(comment='Grafo', format='svg', graph_attr={'rankdir': 'LR' })

    for u, v, peso in grafo.aristas:
        dot.edge(u, v, label=str(peso))

    dot.view()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: {} <filename>'.format(sys.argv[0]))
        sys.exit(1)

    main(sys.argv[1])
