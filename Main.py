from DisjointSet import DisjointSet


class Graph(object):

    def __init__(self):
        self.nodes = set()
        self.edges = []

    def insertEdge(self, from_node, to_node, weight):
        edge = Edge(weight, from_node, to_node)
        self.edges.append(edge)
        self.nodes.add(from_node)
        self.nodes.add(to_node)

    def insertNode(self, value):
        node = Node(value)
        self.nodes.add(node)

    def makeKruskal(self):
        disjoint = DisjointSet()
        a = []
        soma = 0
        for node in self.nodes:
            disjoint.makeSet(node)
        sorted_edges = sorted(self.edges)
        for edge in sorted_edges:
            if disjoint.findSet(edge.node_from) != disjoint.findSet(edge.node_to):
                soma += edge.weight
                a.append((edge.node_from, edge.node_to, edge.weight))
                disjoint.union(edge.node_from, edge.node_to)

        print('Caminho:')

        for edge in a:
            print(edge[0], ' -- ', edge[1], 'Peso:', edge[2])

        print('Peso do caminho gerado pelo Kruskal:', soma)


class Edge(object):
    def __init__(self, weight, node_from, node_to):
        self.weight = weight
        self.node_from = node_from
        self.node_to = node_to

    def __lt__(self, other):
        return not other.weight < self.weight

    def __str__(self):
        return f"{self.node_from} -- {self.node_to} : peso: {self.weight}"


class Node(object):
    def __init__(self, value):
        self.value = value


if __name__ == '__main__':

    graph = Graph()

    graph.insertEdge('a', 'b', 4)
    graph.insertEdge('a', 'h', 8)
    graph.insertEdge('b', 'c', 8)
    graph.insertEdge('b', 'h', 11)
    graph.insertEdge('c', 'i', 2)
    graph.insertEdge('c', 'd', 7)
    graph.insertEdge('c', 'f', 4)
    graph.insertEdge('d', 'e', 9)
    graph.insertEdge('d', 'f', 14)
    graph.insertEdge('e', 'f', 10)
    graph.insertEdge('f', 'g', 2)
    graph.insertEdge('g', 'h', 1)
    graph.insertEdge('g', 'i', 6)
    graph.insertEdge('h', 'i', 7)

    graph.makeKruskal()
