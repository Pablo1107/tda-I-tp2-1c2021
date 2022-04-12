import pprint
from collections import defaultdict

class Graph(object):
    def __init__(self, connections=None):
        self._graph = defaultdict(dict)
        if connections:
            self.add_connections(connections)

    def add_connections(self, connections):
        for node1, node2, weight in connections:
            self.add(node1, node2, weight)

    def add(self, node1, node2, weight=1):
        if self._graph[node1] is None:
            self._graph[node1] = dict()

        self._graph[node1][node2] = weight

    def remove(self, node):
        for n, cxns in self._graph.items():
            try:
                cxns.remove(node)
            except KeyError:
                pass
        try:
            del self._graph[node]
        except KeyError:
            pass

    def is_connected(self, node1, node2):
        return node2 in self._graph[node1]

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))
