# Using networkx implementation of Graph
# Source: https://networkx.github.io/documentation/stable/_downloads/networkx_reference.pdf
import networkx as nx
import matplotlib.pyplot as plt
from itertools import permutations
from random import randint
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

    def generate_paths_from(self, start):
        nodes_to_visit = list(nx.nodes(self.G))
        nodes_to_visit.remove(start)
        paths = list(permutations(nodes_to_visit))
        paths = [ [start] + list(path) + [start] for path in paths ]

        return paths

    def calculate_path_weight(self, path):
        # TODO: implement path weight calculation
        return 1+randint(0,15)

    def brute_force_tsp(self, start):
        print('--- BRUTE FORCE TSP ---')
        possible_path_permutations = self.generate_paths_from(start)
        paths_and_weights = []
        for path in possible_path_permutations:
            weight = self.calculate_path_weight(path)
            paths_and_weights.append((path, weight))

        paths_and_weights = sorted(paths_and_weights, key=lambda path: path[1])

        print('Visit order: ', paths_and_weights[0][0])
        print('Total weight: ', paths_and_weights[0][1])
    

    def greedy_tsp(self, start):
        print('--- GREEDY TSP ---')
        visited = []
        total_weight = 0
        current = start
        while True:
            lowest = None
            lowest_weight = 0

            for edge_start, edge_end in nx.edges(self.G, current):
                if edge_end in visited:
                    continue
                weight = self.G[edge_start][edge_end]['weight']    
                if lowest is None or weight < lowest_weight:
                    lowest = edge_end
                    lowest_weight = weight
            
            visited.append(current)

            if lowest is None:
                total_weight += self.G[current][start]['weight']
                visited.append(start)
                print('Visit order: ', visited)
                print('Total weight: ', total_weight)
                return
            else:
                current = lowest if lowest is not None else current
                total_weight += lowest_weight

    def print_graph(self):
        for node in self.G:
            print(node)
