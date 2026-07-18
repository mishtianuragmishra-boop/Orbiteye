import tkinter as tk
import matplotlib.pyplot as plt

def gen_meanmotiongraph():
    
    meanmotion=[]
    with open("data/starlink.tle.txt","r",encoding="utf-8") as f:
        lines=f.readlines()
    
    for i in range(2,len(lines),3):
        parts=lines[i].split()
        meanmotion.append(float(parts[-1]))

    fig=plt.figure(figsize=(5,4))
    ax= fig.add_subplot(111)

    ax.hist(meanmotion,bins=30)

    ax.set_facecolor("#FFF5F8")
    ax.set_title("Mean Motion Distribution")
    ax.set_xlabel("Mean Motion (Days/rev)")
    ax.set_ylabel("Number of Satellites")
    ax.grid(alpha=0.3)

    plt.gca().set_facecolor("#FFF5F8")

    plt.title("Mean Motion Distribution")
    plt.xlabel("Mean motion (rev/days)")
    plt.ylabel("Number of Satellites")

    plt.grid(alpha=0.3)
  
    return fig