# Using networkx implementation of Graph
# Source: https://networkx.github.io/documentation/stable/_downloads/networkx_reference.pdf
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    G = None

    def __init__(self, weighted_edge_list = []):
        self.G = nx.DiGraph()
        self.add_edge(weighted_edge_list)

    def add_edge(self, weighted_edge_list):
        self.G.add_weighted_edges_from(weighted_edge_list)

    def draw(self):
        nx.draw_networkx(self.G)
        labels = nx.get_edge_attributes(self.G,'weight')
        labels = nx.get_edge_attributes(self.G,'weight')
        pos=nx.planar_layout(self.G) # pos = nx.nx_agraph.graphviz_layout(G)
        nx.draw_networkx_edge_labels(self.G,pos,edge_labels=labels)
        plt.show()

    def greedy_tsp(self, start):
        visited = set()
        current = self.G[start]
        while True:
            lowest = None
            for nbr in current:
                if lowest is None or lowest._atlas.weight > current._atlas.weight:
                    lowest = self.G[nbr]
            print(lowest)


        if len(visited) == self.G.number_of_nodes():
            pass

    def print_graph(self):
        for node in self.G:
            print(node)
