import tkinter as tk
import matplotlib.pyplot as plt

def gen_epochgraph():
    popup=tk.Toplevel()
    popup.title("Epoch")
    popup.geometry("350x150")
    popup.configure(bg="#DA2C43")
    tk.Label(
        popup,
        text="Generating Epoch Graph . . . .",
        bg="#DA2C43",
        fg="#FFB5C0",
        font=("Segoe UI",10,"bold")
    ).pack(pady=30)
    tk.Button(
        popup,
        text="OK",
        bg="#D20A2E",
        fg="#FFB5C0",
        width=12,
        command=popup.destroy
    ).pack()

    epoch=[]
    with open("data/starlink.tle.txt","r",encoding="utf-8") as f:
        lines=f.readlines()
    
    for i in range(2,len(lines),3):
        parts=lines[i].split()
        epoch.append(float(parts[3]))

    plt.figure(figsize=(8,5))

    plt.hist(
        epoch,
        bins=30,
        color="#FF8FAB",
        edgecolor="#D20A2E"
    )

    plt.gca().set_facecolor("#FFF5F8")

    plt.title("Epoch Distribution")
    plt.xlabel("Epoch (rev/days)")
    plt.ylabel("Number of Satellites")

    plt.grid(alpha=0.3)

    popup.update
    popup.destroy

    plt.show()
  
