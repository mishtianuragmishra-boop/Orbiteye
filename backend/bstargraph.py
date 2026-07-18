import tkinter as tk
import matplotlib.pyplot as plt

def gen_bstargraph():
    
    bstar=[]
    with open("data/starlink.tle.txt","r",encoding="utf-8") as f:
        lines=f.readlines()
    
    for i in range(2,len(lines),3):
        parts=lines[i].split()
        raw=parts[6]
        mantissa=raw[:-2]
        exponent=raw[-2:]
        value=float(f"0.{raw[:-2]}e{raw[-2:]}")
        bstar.append(value)

    fig,ax=plt.subplots(figsize=(8,5))

    ax.hist(
        bstar,
        bins=30,
        color="#FF8FAB",
        edgecolor="#D20A2E"
    )
    ax.set_facecolor("#99D88E")

    ax.set_title("BSTAR Distribution")
    ax.set_xlabel("BSTAR")
    ax.set_ylabel("Numbe of satellites")

    ax.grid(alpha=0.3)
    fig.tight_layout()
    print(len(bstar))

    return fig
