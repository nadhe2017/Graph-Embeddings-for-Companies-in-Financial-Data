import numpy as np 

if __name__ == "__main__":
    source_dir = "sec_desc/"
    with open(source_dir+"graph.txt","r") as f:
        graph = [map(int,line.rstrip("\n").rstrip("\r").split("\t")) for line in f]
    
    with open(source_dir+"data.txt","r") as f:
        text = [line for line in f]

    node2vec = {}
    with open(source_dir+"embed.txt","r") as f:
        for i, j in enumerate(f):
            if j != '\n':
                node2vec[i] = map(float, j.strip().split(' '))
    
    all_nodes = set([x for pair in graph for x in pair])
    target = 1032
    if target not in node2vec.keys():
        raise ValueError("The target node isn't embedded.")
    topn = 10
    result = []
    for i in all_nodes:
        if i != target and i in node2vec.keys():
            result.append(np.dot(node2vec[target],node2vec[i]))
    
    closestn = np.argsort(result)[-topn:][::-1]
    print "The closest {0} nodes with node {1} is:\n{2}\n".format(topn,target,closestn)
    # print "The target node description:\n", text[target], "\n"

    # for i in closestn:
    #     print "The edge between",target,"and",i,"exist" if [target,i] in graph or [i,target] in graph else "not exist."
    #     print "The node", i, "description is:\n", text[i], "\n"

    cnt = 0
    for i in closestn:
        cnt += 1 if [target,i] in graph or [i,target] in graph else 0
    
    print cnt