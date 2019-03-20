import pandas as pd 
import json
import os, sys
from collections import defaultdict
from pprint import pprint

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_axis = int(sys.argv[1])
        print "Number of axis =", num_axis
    else:
        num_axis = 5
    nodes = {}
    links = []
    cnt = 0
    with open("../../data/manual/Q2_names.txt","r") as f:
        for line in f.read().splitlines():
            # cnt += 1
            # if cnt > 10:
            #     break
            entities = line.split(",")
            # print entities
            for comp in entities:
                if comp != "" and comp not in nodes:
                    nodes[comp] = {"id":comp}
                elif comp == "":
                    entities.remove("")
            for i in range(len(entities)):
                for j in range(i+1,len(entities)):
                    source = entities[i]
                    target = entities[j]
                    links.append({"source":nodes[source],"target":nodes[target]})
    print "Number of Nodes: ", len(nodes)
    print "Number of Links: ", len(links)

    link_degree = defaultdict(int)
    for l in links:
        link_degree[l["source"]["id"]] += 1

    groups = [len(nodes)//num_axis+1]*(num_axis-1)
    groups += [len(nodes) - sum(groups)]
    print "Group partition:",groups

    cnt = 0
    for _,n in nodes.items():
        for i in range(num_axis):
            if cnt < sum(groups[:i+1]):
                x = i
                y = cnt - sum(groups[:i]) if i > 0 else cnt
                break
        n["x"] = x
        n["y"] = float(y)/groups[x]
        cnt += 1

    result = {}
    result["nodes"] = [v for k,v in nodes.items()]
    result["links"] = links
    with open('manual.json','w') as f:
        json.dump(result,f)
    
    # pprint(result["nodes"])
