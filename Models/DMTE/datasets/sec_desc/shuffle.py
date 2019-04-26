import random

if __name__ == "__main__":
    with open("data.txt","r") as f:
        data = [line.rstrip("\n") for line in f]
        
    with open("graph.txt","r") as f:
        graph = [line.rstrip("\n") for line in f]
    
    ind = list(range(len(data)))
    random.shuffle(ind)
    now2shuf = {str(i):str(n) for i,n in enumerate(ind)}
    
    new_graph = [""]*len(graph)
    for i in range(len(graph)):
        g1, g2 = graph[i].split("\t")
        new_line = now2shuf[g1] + "\t" + now2shuf[g2]
        new_graph[i] = new_line
    
    new_data = [""]*len(data)
    shuf2now = {y:x for x,y in now2shuf.items()}
    for i in range(len(data)):
        new_data[i] = data[int(shuf2now[str(i)])]

    with open("new_data.txt","w") as f:
        for x in new_data:
            f.write("%s\n" % x)
    
    with open("new_graph.txt","w") as f:
        for x in new_graph:
            f.write("%s\n" % x)

    # test shuffle
    print "Old graph & data:"
    print graph[0]
    g1,g2 = map(lambda x: int(x), graph[0].split("\t"))
    print data[g1]
    print data[g2]

    print "New graph & data:"
    print new_graph[0]
    g1,g2 = map(lambda x: int(x), new_graph[0].split("\t"))
    print new_data[g1]
    print new_data[g2]