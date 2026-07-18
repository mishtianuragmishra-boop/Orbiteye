import tkinter as tk
import matplotlib.pyplot as plt

def gen_incgraph():

    inc=[]
    with open("data/starlink.tle.txt","r",encoding="utf-8") as f:
        lines=f.readlines()
    
    for i in range(2,len(lines),3):
        parts=lines[i].split()
        inc.append(float(parts[2]))

    fig,ax=plt.subplots(figsize=(8,5))

    ax.hist(
        inc,
        bins=30,
        color="#FF8FAB",
        edgecolor="#D20A2E"
    )
    ax.set_facecolor("#99D88E")

    ax.set_title("Inclination Distribution")
    ax.set_xlabel("Inclination")
    ax.set_ylabel("Numbe of satellites")

    ax.grid(alpha=0.3)
    fig.tight_layout()
    print(len(inc))

    return fig
  
