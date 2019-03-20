import pandas as pd 
import json
import os 

if __name__ == "__main__":
    nodes = {}
    links = []
    files = ["Q1","Q2","Q3","Q4"]
    for fn in files:
        with open(fn+"_names.txt","r") as f:
            for line in f.read().splitlines():
                entities = line.split(",")
                print entities
                for comp in entities:
                    if comp != "" and comp not in nodes:
                        nodes[comp] = [len(nodes),0]
                    elif comp == "":
                        entities.remove("")
                for i in range(len(entities)):
                    for j in range(i+1,len(entities)):
                        source = entities[i]
                        target = entities[j]
                        nodes[source][1] += 1
                        nodes[target][1] += 1
                        links.append({"source":nodes[source][0],"target":nodes[target][0],"value":1})

    result = {}
    result["nodes"] = [{"id":x,"pos":y} for x,(y,z) in nodes.items() if z>0]
    result["links"] = links

    print "Number of Nodes: ", len(result["nodes"])
    print "Number of Links: ", len(result["links"])

    with open('manual.json','w') as f:
        json.dump(result,f)
    with open('../../Visualization/force_plot/manual.json','w') as f:
        json.dump(result,f)
