import tkinter as tk
import matplotlib.pyplot as plt

def gen_epochgraph():

    epoch=[]
    with open("data/starlink.tle.txt","r",encoding="utf-8") as f:
        lines=f.readlines()
    
    for i in range(2,len(lines),3):
        parts=lines[i].split()
        epoch.append(float(parts[3]))

    fig,ax=plt.subplots(figsize=(8,5))

    ax.hist(
        epoch,
        bins=30,
        color="#7BB76C",
        edgecolor="#D20A2E"
    )
    ax.set_facecolor("#E3708F")

    ax.set_title("Epoch Distribution")
    ax.set_xlabel("Epoch")
    ax.set_ylabel("Number of satellites")

    ax.grid(alpha=0.3)
    fig.tight_layout()
    print(len(epoch))

    return fig


