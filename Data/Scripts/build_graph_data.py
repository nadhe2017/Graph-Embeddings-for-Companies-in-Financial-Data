import pandas as pd 
import json
import os

def search_comp(c):
    dirs = ["Q1","Q2","Q3","Q4"]
    t = ""
    for q in dirs:
        filename = "../Item_2.01_filings_2018_html/" + \
                        q + "/" + c + "-item_2.01.txt"
        if os.path.isfile(filename):
            with open(filename, "r") as f:
                t += f.read().replace('\n', '')
    return t

if __name__ == "__main__":
    with open("manual.json") as f:
        data = json.load(f)
    # print type(data)
    # print len(data["nodes"])
    # print len(data["links"])
    
    nodes = sorted([x["pos"] for x in data["nodes"]])
    names = [x["id"] for x in sorted(data["nodes"],key=lambda x:x["pos"])]
    nodes_map = {y:x for x,y in enumerate(nodes)}

    links = [(nodes_map[x["source"]],nodes_map[x["target"]]) \
                    for x in data["links"]]

    text = [""]*len(nodes)
    for i in range(len(nodes)):
        text[i] = search_comp(names[i])
    
    save_dir = "../sec_dataset/"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    with open(save_dir+'data.txt', 'w') as f:  
        for t in text:
            f.write('%s\n' % t)
    with open(save_dir+'graph.txt', 'w') as f:  
        for l in links:
            f.write('%s\t%s\n' % (l[0],l[1]))
    