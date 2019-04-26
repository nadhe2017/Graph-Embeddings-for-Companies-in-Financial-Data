import json

if __name__ == "__main__":
    # graph_file = "rd_graph.txt"
    # graph_file = "../../Data/Scripts/sentence_level_rd_graph.txt"
    # graph_file = "../../Data/Scripts/sentence_level_graph.txt"
    # graph_file = "max_connected_graph.txt"
    graph_file = "final_graph.txt"
    with open(graph_file,"r") as f:
        graph = [line.rstrip("\n").rstrip("\r").split("\t") for line in f]
    
    node_set = set([])
    for x,y in graph:
        node_set.add(x)
        node_set.add(y)

    result = {}
    result["nodes"] = [{"id":x, "pos":int(x)} for x in node_set]
    result["links"] = [{"source":int(x),"target":int(y),"value":1} for x,y in graph]
    
    # with open('sentence_level_graph_rd.json','w') as f:
    # with open('sentence_level_graph.json','w') as f:
    # with open("max_connected_graph_rd.json","w") as f:
    with open("final_graph.json","w") as f:
        json.dump(result,f)