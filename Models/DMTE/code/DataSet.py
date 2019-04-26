import sys

reload(sys)
import config

sys.setdefaultencoding("utf-8")
import numpy as np
from tensorflow.contrib import learn
from sklearn.preprocessing import normalize
from negativeSample import InitNegTable
import random
import pdb


class dataSet:
    def __init__(self, text_path, graph_path):

        text_file, graph_file = self.load(text_path, graph_path)

        self.edges = self.load_edges(graph_file)

        self.text, self.num_vocab, self.num_nodes = self.load_text(text_file)
        
        self.nodes = range(0, self.num_nodes)

        self.negative_table = InitNegTable(self.edges)
        
        self.P = self.P_matrix(self.edges, self.num_nodes)

    def load(self, text_path, graph_path):
        text_file = open(text_path, 'rb').readlines()
        graph_file = open(graph_path, 'rb').readlines()

        return text_file, graph_file

    def load_edges(self, graph_file):
        edges = []
        fw = open('test_graph.txt','wb')
        for i in graph_file:
            if np.random.uniform(0.0, 1.0) <= config.ratio:
                edges.append(map(int, i.strip().split('\t')))
	    else:
                fw.write(i)

        return edges

    def load_text(self, text_file):
        vocab = learn.preprocessing.VocabularyProcessor(config.MAX_LEN)
        text = np.array(list(vocab.fit_transform(text_file)))
        num_vocab = len(vocab.vocabulary_)
        num_nodes = len(text)

        return text, num_vocab, num_nodes

    def negative_sample(self, edges):
        node1, node2 = zip(*edges)
        sample_edges = []
        func = lambda: self.negative_table[random.randint(0, config.neg_table_size - 1)]
        for i in range(len(edges)):
            neg_node = func()
            while node1[i] == neg_node or node2[i] == neg_node:
                neg_node = func()
            sample_edges.append([node1[i], node2[i], neg_node])

        return sample_edges

    def generate_batches(self, mode=None):

        num_batch = len(self.edges) / config.batch_size
        edges = self.edges
        if mode == 'add':
            num_batch += 1
            edges.extend(edges[:(config.batch_size - len(self.edges) % config.batch_size)])
        if mode != 'add':
            random.shuffle(edges)
        sample_edges = edges[:num_batch * config.batch_size]
        sample_edges = self.negative_sample(sample_edges)

        batches = []
        for i in range(num_batch):
            batches.append(sample_edges[i * config.batch_size:(i + 1) * config.batch_size])
        return batches
    
    def nodes_batches(self, mode=None):

        num_batch = len(self.nodes) / config.batch_size
        nodes = self.nodes
        if mode == 'add':
            num_batch += 1
            nodes.extend(nodes[:(config.batch_size - len(self.nodes) % config.batch_size)])
            random.shuffle(nodes)
        if mode != 'add':
            random.shuffle(nodes)
        sample_nodes = nodes[:num_batch * config.batch_size]

        batches = []
        for i in range(num_batch):
            batches.append(sample_nodes[i * config.batch_size:(i + 1) * config.batch_size])
        return batches

    def P_matrix(self, edges, num_nodes):
        a_list,b_list=zip(*edges)
        a_list=list(a_list)
        b_list=list(b_list)
    
        P = np.zeros((num_nodes,num_nodes))
        for i in range(len(a_list)):
            P[a_list[i],b_list[i]]=1
            P[b_list[i],a_list[i]]=1
        
        P = normalize(P, axis=1, norm='l1')
        
        return P
