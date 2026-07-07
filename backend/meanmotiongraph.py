import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def gen_meanmotiongraph():
    popup=tk.Toplevel()
    popup.title("Mean Motion")
    popup.geometry("350x150")
    popup.configure(bg="#DA2C43")
    tk.Label(
        popup,
        text="Generating Mean Motion Graph. . . .",
        bg="#AA1C41",
        fg="#FFB5C0",
        font=("Segoe UI",10,"bold")
    ).pack(pady=30)
    tk.Button(
        popup,
        text="OK",
        bg="#FFE8B4",
        fg="#FFB5C0",
        width=12,
        command=popup.destroy
    ).pack()

    meanmotion=[]
    with open("data/starlink.tle.txt","r",encoding="utf-8") as f:
        lines=f.readlines()
    
    for i in range(2,len(lines),3):
        parts=lines[i].split()
        meanmotion.append(float(parts[-1]))

    graph_frame=tk.Frame(
        popup,
        width=450,
        height=500,
        bg="#DA2C43"
    )
    graph_frame.pack(side="left",padx=20,pady=20)
    plt.figure(figsize=(5,4)),
    fig=plt.figure(figsize=(5,4))
    ax= fig.add_subplot(111)

    ax.hist(meanmotion,bins=30)

    ax.set_facecolor("#FFF5F8")
    ax.set_title("Mean Motion Distribution")
    ax.set_xlabel("Mean Motion (Days/rev)")
    ax.set_ylabel("Number of Satellites")
    ax.grid(alpha=0.3)

    canvas=FigureCanvasTkAgg(fig,master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both",expand=True)

    plt.gca().set_facecolor("#FFF5F8")

    plt.title("Mean Motion Distribution")
    plt.xlabel("Mean motion (rev/days)")
    plt.ylabel("Number of Satellites")

    plt.grid(alpha=0.3)

    popup.update
    popup.destroy

    plt.show()