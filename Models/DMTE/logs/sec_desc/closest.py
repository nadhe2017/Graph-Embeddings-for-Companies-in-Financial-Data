import numpy as np 
import matplotlib.pyplot as plt

if __name__ == "__main__":
    folder = "sec55_desc/"
    with open(folder+"embed.txt") as f:
        embed = [line.rstrip("\n").split() for line in f]
    
    for i in range(len(embed)):
        if len(embed[i]) != 200:
            embed[i] = np.zeros(200)
        else:
            embed[i] = np.array(map(lambda x: float(x),embed[i]))
        print embed[i].shape
    
    pivot = embed[50]
    hist = []
    for i in range(len(embed)):
        hist.append(pivot.dot(embed[i]))

    closest_n = np.argsort(hist)[-5:][::-1]
    print closest_n

    data_dir = "../../datasets/sec_desc/"
    with open(data_dir+"data.txt","r") as f:
        data = [line.rstrip("\n") for line in f]
    
    for x in range(len(closest_n)):
        print "Dot: ", hist[closest_n[x]]
        print data[closest_n[x]]
        print "\n"
    
    plt.plot(list(range(len(embed))),hist)
    plt.show()