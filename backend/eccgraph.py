import tkinter as tk
import matplotlib.pyplot as plt

def gen_eccgraph():

    ecc=[]
    with open("data/starlink.tle.txt","r",encoding="utf-8") as f:
        lines=f.readlines()
    
    for i in range(2,len(lines),3):
        parts=lines[i].split()
        ecc.append(float("0." + parts[4]))

    fig,ax=plt.subplots(figsize=(8,5))

    ax.hist(
        ecc,
        bins=30,
        color="#FF8FAB",
        edgecolor="#D20A2E"
    )
    ax.set_facecolor("#FFF5F8")

    ax.set_title("Eccenricity Distribution")
    ax.set_xlabel("ECC")
    ax.set_ylabel("Numbe of satellites")

    ax.grid(alpha=0.3)
    fig.tight_layout()

    return fig