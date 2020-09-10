# Using networkx implementation of Graph
# Source: https://networkx.github.io/documentation/stable/_downloads/networkx_reference.pdf
import networkx as nx
import matplotlib.pyplot as plt
from itertools import permutations
from random import randint


class Graph:
    G = None

    def __init__(self, weighted_edge_list=[]):
        self.G = nx.DiGraph()
        self.add_edge(weighted_edge_list)

    def add_edge(self, weighted_edge_list):
        self.G.add_weighted_edges_from(weighted_edge_list)

    def draw(self, route = [], name = "Normal Graph"):
        plt.figure(name)
        edges = []
        for index, node in enumerate(route):
            if(index+1 < len(route) ):
                edges.append((route[index],route[index+1]))
        
        black_edges = [edge for edge in self.G.edges() if edge not in edges]

        if(len(self.G) <= 4):
            node_pos = nx.planar_layout(self.G)
        else:
            node_pos = nx.circular_layout(self.G)

        arc_weight = nx.get_edge_attributes(self.G, 'weight')
        nx.draw_networkx_labels(self.G, node_pos)
        nx.draw_networkx_edge_labels(self.G, node_pos, edge_labels=arc_weight)
        nx.draw_networkx_nodes(self.G, node_pos, cmap=plt.get_cmap('jet'), node_size = 450)
        nx.draw_networkx_edges(self.G, node_pos, edgelist=edges, edge_color='r', arrows=True)
        nx.draw_networkx_edges(self.G, node_pos, edgelist=black_edges, arrows=False)

    def generate_paths_from(self, start):
        nodes_to_visit = list(nx.nodes(self.G))
        nodes_to_visit.remove(start)
        paths = list(permutations(nodes_to_visit))
        paths = [[start] + list(path) + [start] for path in paths]
        return paths

    def calculate_path_weight(self, path):
        sum_weights = 0
        for i in range(len(path)-1):
            sum_weights += self.G[path[i]][path[i+1]]['weight']
        return sum_weights

    def brute_force_tsp(self, start):
        print('\n--- BRUTE FORCE TSP ---')
        possible_path_permutations = self.generate_paths_from(start)
        paths_and_weights = []
        for path in possible_path_permutations:
            weight = self.calculate_path_weight(path)
            paths_and_weights.append((path, weight))

        paths_and_weights = sorted(paths_and_weights, key=lambda path: path[1])
        print('Visit order: ', paths_and_weights[0][0])
        print('Total weight: ', paths_and_weights[0][1])
        print()
        self.draw(paths_and_weights[0][0],"Brute Force Route")

    def greedy_tsp(self, start):
        print('\n--- GREEDY TSP ---')
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
                self.draw(visited,"Greedy Route")
                return
            else:
                current = lowest if lowest is not None else current
                total_weight += lowest_weight

    def print_graph(self):
        for node in self.G:
            print(node)
