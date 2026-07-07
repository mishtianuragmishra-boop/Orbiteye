import tkinter as tk
import matplotlib.pyplot as plt

def gen_incgraph():
    popup=tk.Toplevel()
    popup.title("Inclination")
    popup.geometry("350x150")
    popup.configure(bg="#DA2C43")
    tk.Label(
        popup,
        text="Generating Inclination Graph . . . .",
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

    inc=[]
    with open("data/starlink.tle.txt","r",encoding="utf-8") as f:
        lines=f.readlines()
    
    for i in range(2,len(lines),3):
        parts=lines[i].split()
        inc.append(float(parts[2]))

    plt.figure(figsize=(8,5))

    plt.hist(
        inc,
        bins=30,
        color="#FF8FAB",
        edgecolor="#D20A2E"
    )

    plt.gca().set_facecolor("#FFF5F8")

    plt.title("Inclination Distribution")
    plt.xlabel("Inclination  (rev/days)")
    plt.ylabel("Number of Satellites")

    plt.grid(alpha=0.3)

    popup.update
    popup.destroy

    plt.show()
  
