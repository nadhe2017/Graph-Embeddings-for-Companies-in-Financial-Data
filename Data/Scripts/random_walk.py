from collections import defaultdict

if __name__ == "__main__":
    # graph_file = "../manual/sec_dataset/graph.txt"
    graph_file = "sentence_level_graph.txt"
    with open(graph_file,"r") as f:
        aj_list = [line.rstrip("\n").rstrip("\r").split("\t") for line in f]
    
    with open(graph_file,"w") as f:
        for x,y in aj_list:
            f.write("%s\t%s\n" % (x,y))

    graph = defaultdict(list)
    for edge in aj_list:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    
    keys = graph.keys()
    keys.sort(key=lambda x: len(graph[x]),reverse=True)
    top50p = len(graph[keys[len(keys)//2]])

    print "In original graph, there are {0} nodes.".format(len(keys))
    print "In original graph, there are {0} edges.".format(len(aj_list))

    select_length = 2000
    picked = set([])
    cnt = 0
    while len(picked) <= select_length:
        cnt += 1
        for x in keys:
            if x not in picked:
                picked.add(x)
                stack = [x]
                break
        while len(picked) <= select_length and stack:
            cur = stack.pop()
            for x in graph[cur]:
                picked.add(x)
                if len(graph[x]) >= top50p and x not in picked:
                    stack.append(x)
    
    new_graph = []
    for x,y in aj_list:
        if x in picked and y in picked:
            new_graph.append([x,y])
    
    print "Selected {0} times.".format(cnt)
    print "Selected {0} nodes.".format(len(picked))
    print "Selected {0} edges.".format(len(new_graph))
    
    save_file = "sentence_level_rd_graph.txt"
    with open(save_file,"w") as f:
        for x,y in new_graph:
            f.write("%s\t%s\n" % (x,y))

