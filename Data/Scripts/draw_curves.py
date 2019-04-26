import matplotlib.pyplot as plt 

if __name__ == "__main__":
    dw = [0.882, 0.941, 0.954, 0.964]
    n2v = [0.800, 0.906, 0.941, 0.966]
    dmte = [0.894, 0.956, 0.933, 0.935]

    x = [0.15,0.35,0.55,0.85]
    plt.plot(x,dw,":",label="DeepWalk",linewidth=2)
    plt.plot(x,n2v,"-.",label="Node2Vec",linewidth=2)
    plt.plot(x,dmte,"-",label="DMTE",linewidth=2)
    plt.ylim(0.75,1.0)
    plt.xlim(0.0,1.0)
    plt.xlabel("Ratio of Training Edges")
    plt.ylabel("Area Under Curve")
    plt.legend()
    plt.show()