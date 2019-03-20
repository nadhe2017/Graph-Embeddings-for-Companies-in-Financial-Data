import pandas as pd 
import json

if __name__ == "__main__":
    df = pd.read_table('./dblp/graph.txt', delim_whitespace=True, names=('source', 'target'))
    set_of_node = set(df['source']) | set(df['target'])
    result = {}
    result["nodes"] = [{"id":str(x)} for x in set_of_node]
    data_array = df.values
    result["links"] = [{"source":str(data_array[row,0]),"target":str(data_array[row,1]),"value":1}\
                        for row in range(len(data_array[:,0]))]
    with open('dblp.json','w') as f:
        json.dump(result,f)