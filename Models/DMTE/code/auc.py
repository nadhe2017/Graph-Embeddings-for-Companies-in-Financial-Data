import random
import numpy as np

node2vec = {}
#f = open('embed.txt', 'rb') # embed_cora_swem_1_0.15
f = open('embed.txt', 'rb')
for i, j in enumerate(f):
    if j != '\n':
        node2vec[i] = map(float, j.strip().split(' '))
f1 = open('test_graph.txt','rb')
edges = [map(int, i.strip().split('\t')) for i in f1]
nodes = list(set([i for j in edges for i in j]))
a = 0
b = 0

result=[]
for i, j in edges:
    if i in node2vec.keys() and j in node2vec.keys():
        dot1 = np.dot(node2vec[i], node2vec[j])
        
        random_node = random.sample(nodes, 1)[0]
        while random_node == j or random_node not in node2vec.keys() \
             or [i,random_node] in edges or [random_node,i] in edges:
            random_node = random.sample(nodes, 1)[0]
        dot2 = np.dot(node2vec[i], node2vec[random_node])
        result.append(np.asarray([dot1,dot2]))
        if dot1 > dot2:
            a += 1
        elif dot1 == dot2:
            a += 0.5
        b += 1

print("Valid edges for AUC is",b)
print("AUC =",float(a) / b)
