import codecs
import json
from collections import defaultdict
import os
from nltk.corpus import stopwords 
from nltk.tokenize import RegexpTokenizer

if __name__ == "__main__":
    # data: list of dictionaries
    data = json.load(codecs.open('final_entity_description_2k.txt', 'r', 'utf-8-sig'), strict=False)

    name2node = defaultdict(list)
    node2new = defaultdict(int)
    node2text = defaultdict(str)
    node2name = defaultdict(str)

    # remove punctuations and stop words with NLTK
    stop_words = set(stopwords.words('english'))
    tokenizer = RegexpTokenizer(r'\w+')

    # remove incorrect companies
    for comp in data:
        original_name = [x for x in comp.keys() if x != "Node"][0]
        name = original_name.upper().replace(",","")
        if name[0]=="*": 
            name = name[1:]
        if "MERGER SUB" in name:
            continue
        node = comp["Node"]
        if len(name2node[name]) > 0:
            node2new[node] = name2node[name][0]
        else:
            node2new[node] = node
        name2node[name].append(node)
        meta_node = name2node[name][0]
        if node2text[meta_node] == "":
            sentense = comp[original_name].replace("\n"," ").replace("\r"," ")
            sentense = tokenizer.tokenize(sentense)
            node2text[meta_node] = " ".join([w for w in sentense if w not in stop_words])
        node2name[meta_node] = name

    to_be_pop = set([])
    for k,v in node2text.items():
        if v == "":
            # # uncomment this for full graph
            # node2text[k] = node2name[k]

            # comment this for full graph
            to_be_pop.add(k)
            
    for k in to_be_pop:
        node2text.pop(k,None)
        node2new.pop(k,None)

    new_nodes = set(node2new.values())
    new2full = {y:x for x,y in enumerate(new_nodes)}
    full2new = {y:x for x,y in new2full.items()}
    for k,v in node2new.items():
        node2new[k] = new2full[v]

    with open("max_connected_graph_2k.txt","r") as f:
        graph = [line.rstrip("\n").rstrip("\r") for line in f]
    
    list_of_nodes = node2new.keys()
    new_graph = []
    for l in graph:
        x,y = map(int,l.split("\t"))
        if x in list_of_nodes and y in list_of_nodes:
            new_graph.append([node2new[x],node2new[y]])

    save_dir = "sec_desc_part/"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    with open(save_dir+"graph.txt","w") as f:
        for x,y in new_graph:
            f.write(str(x)+"\t"+str(y)+"\n")

    with open(save_dir+"data.txt","w") as f:
        for i in range(len(new_nodes)):
            f.write(node2text[full2new[i]]+"\n")