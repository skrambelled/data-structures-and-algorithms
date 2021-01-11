class Vertex:
    def __init__(self, value):
        self.value = value


class Edge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight


class Graph:
    def __init__(self):
        self._adjecency_list = {}

    def add_node(self, value):
        vertex = Vertex(value)

        self._adjecency_list[vertex] = []

        return vertex

    def get_nodes(self):
        return self._adjecency_list.keys()

    def add_edge(self, start, end, weight=0):
        if start not in self._adjecency_list:
            raise KeyError(f'{start} not a vertex in {self}')

        if end not in self._adjecency_list:
            raise KeyError(f'{start} not a vertex in {self}')

        edge = Edge(end, weight)

        self._adjecency_list[start].append(edge)

    def get_neighbors(self, vertex):
        if vertex not in self._adjecency_list:
            raise KeyError(f'{vertex} not a vertex in {self}')

        return self._adjecency_list[vertex]

    def size(self):
        return len(self._adjecency_list)
