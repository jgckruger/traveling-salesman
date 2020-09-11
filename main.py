import pandas as pd
import matplotlib.pyplot as plt
import time
from classes.graph import Graph

df = pd.read_csv('input.txt')
start = df.iloc[-1][0]
df = df[:-1]
df.index = df.columns.tolist()

def generate_weighted_edge_list(df):
    weighted_edge_list = []
    for idx, row in df.iterrows():
        for col, weight in row.iteritems():
            edge = (idx, col, float(row[col]))
            if edge[2] < 0:
                continue
            weighted_edge_list.append(edge)
    return weighted_edge_list

g = Graph(generate_weighted_edge_list(df))

startTime = time.time()
g.greedy_tsp(start)
endTime = time.time()
print('Greedy:', endTime-startTime, 'seconds')


startTime = time.time()
g.brute_force_tsp(start)
endTime = time.time()
print('Brute force:', endTime-startTime, 'seconds')

g.draw()
plt.axis('off')
plt.show()
