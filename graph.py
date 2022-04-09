from typing import List


class Node:
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children: List[Node] = children


Node(0, [1])
Node(1, [2])
Node(2, [0])
# Node(3, [2])

edges = [(2, 3)]


class Graph:
    def __init__(self, graph):
        self.graph = []

    def add(self, val, children: List[Node], edges: List[int]):
        newNode = Node(val, children)
        self.graph.append(newNode)

        for i, n in enumerate(self.graph):
            for e in edges:
                if n.val == e[0]:
                    n.children.append(e[1])

                    self.graph[i] = n

    
