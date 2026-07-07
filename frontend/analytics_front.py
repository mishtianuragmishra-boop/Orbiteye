import tkinter as tk
from frontend import gui

from backend.bstargraph import gen_bstargraph
from backend.bstarstat import gen_bstarstats

from backend.eccgraph import gen_eccgraph
from backend.eccstat import gen_eccstat

from backend.epochgraph import gen_epochgraph
from backend.epochstat import gen_epochstat

from backend.meanmotiongraph import gen_meanmotiongraph
from backend.meanmotionstat import gen_meanmotionstat

from backend.incgraph import gen_incgraph
from backend.incstat import gen_incstat

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def analytics():

    window=tk.Toplevel(gui.root)
    window.title("Analytics")
    window.geometry("700x950")
    window.configure(bg="#DA2C43")

    #mainframe

    main_frame=tk.Frame(
        controls_frame,
        bg="#DA2C43"
    )
    main_frame.pack(fill="both",expand=True)

    #gaphframe

    graph_frame=tk.Frame(
        main_frame,
        bg="#FFF5F8",
        width=500,
        height=750
    )
    graph_frame.pack(side="left",padx=20,pady=20)
    graph_frame.pack_propagate(False)

    #controls frame(RIGHT)

    controls_frame=tk.Frame(
        main_frame,
        bg="#DA2C43"
    )
    controls_frame.pack(side="right",fill="y",padx=20,pady=20)

    def show_graph(fig):
        for widget in graph_frame.winfo_children():
            widget.destroy()

        canvas=FigureCanvasTkAgg(fig,master=graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both",expand=True)

#title
    title=tk.Label(
        controls_frame,
        text="Analytics",
        font=("Segoe UI",30,"Italic","bold"),
        bg="#DA2C43",
        fg="#FFB5C0"
    )
    title.pack(pady=15)

#BSTAR

    bstar_label=tk.Label(
        controls_frame,
        text="BSTAR",
        bg="#DA2C43",
        fg="#FFB5C0",
        font=("Segoe UI",22,"italic")
    )
    bstar_label.pack()

    bstar_button_frame=tk.Frame(
        controls_frame,
        bg="#DA2C43"
    )
    bstar_button_frame.pack(pady=5)


    bstargraph_btn=tk.Button(
        bstar_button_frame,
        text="Graph",
        width=15,
        bg="#D20A2E",
        fg="#FFB5C0",
        height=2,
        command=lambda:show_graph(gen_bstargraph())
        
    )
    bstargraph_btn.pack(side="left",padx=10)

    bstarstat_btn=tk.Button(
        bstar_button_frame,
        text="Statistics",
        width=15,
        bg="#D20A2E",
        fg="#FFB5C0",
        height=2,
        command=gen_bstarstats
    )
    bstarstat_btn.pack(side="left", padx=10)
#meanmotion
    meanmotion_frame=tk.Frame(
        controls_frame,
        bg="#DA2C43"
    )
    meanmotion_frame.pack(pady=(20,5))

    meanmotion_label=tk.Label(
        meanmotion_frame,
        text="Mean Motion",
        bg="#DA2C43",
        font=("Segoe UI",22,"italic"),
        fg="#FFB5C0"
    )
    meanmotion_label.pack()

    meanmotion_button_frame=tk.Frame(
        meanmotion_frame,
        bg="#DA2C43"
    )
    meanmotion_button_frame.pack(pady=5)

    meanmotiongraph_btn=tk.Button(
        meanmotion_button_frame,
        text="Graph",
        width=15,
        bg="#D20A2E",
        fg="#FFB5C0",
        height=2,
        command=lambda: show_graph(gen_meanmotiongraph())
    )

    meanmotiongraph_btn.pack(side="left",padx=15)

    meanmotionstat_btn=tk.Button(
        meanmotion_button_frame,
        text="Statistics",
        width=15,
        bg="#D20A2E",
        fg="#FFB5C0",
        height=2,
        command=gen_meanmotionstat
    )
    meanmotionstat_btn.pack(side="left", padx=10)
#INCLINATION

    inc_frame=tk.Frame(
        controls_frame,
        bg="#DA2C43"
    )
    inc_frame.pack(pady=5)

    title=tk.Label(
        inc_frame,
        text="Inclination",
        bg="#DA2C43",
        font=("Segoe UI",22,"italic"),
        fg="#FFB5C0"
    )
    title.pack(pady=5)

    inc_button_frame=tk.Frame(
        inc_frame,
        bg="#DA2C43"
    )
    inc_button_frame.pack(pady=5)

    incgraph_btn=tk.Button(
        inc_button_frame,
        text="Graph",
        width=15,
        bg="#D20A2E",
        fg="#FFB5C0",
        height=2,
        command=lambda: show_graph(gen_incgraph())
    )

    incgraph_btn.pack(side="left", padx=10)

    incstat_btn=tk.Button(
        inc_button_frame,
        text="Statistics",
        width=15,
        bg="#D20A2E",
        fg="#FFB5C0",
        height=2,
        command=gen_incstat
    )
    incstat_btn.pack(side="left", padx=10)

    # Eccentricity 

    ecc_frame=tk.Frame(
        controls_frame,
        bg="#DA2C43"
    )
    ecc_frame.pack(pady=5)

    title=tk.Label(
        ecc_frame,
        text="Eccentricity",
        bg="#DA2C43",
        fg="#FFB5C0",
        font=("Segoe UI",22,"italic")
    )
    title.pack(pady=5)

    ecc_button_frame=tk.Frame(
        ecc_frame,
        bg="#DA2C43"
    )
    ecc_button_frame.pack(pady=5)

    eccgraph_btn=tk.Button(
        ecc_button_frame,
        text="Graph",
        width=15,
        bg="#D20A2E",
        fg="#FFB5C0",
        height=2,
        command=lambda: show_graph(gen_eccgraph())
    )
    eccgraph_btn.pack(side="left", padx=10)

    eccstat_btn=tk.Button(
        ecc_button_frame,
        text="Statistics",
        width=15,
        bg="#D20A2E",
        fg="#FFB5C0",
        height=2,
        command=gen_eccstat
    )
    eccstat_btn.pack(side="left", padx=10)

    #epoch
     
    epoch_frame=tk.Frame(
        controls_frame,
        bg="#DA2C43"
    )
    epoch_frame.pack(pady=5)

    title=tk.Label(
        epoch_frame,
        text="Epoch",
        font=("Segoe UI",22,"italic"),
        bg="#DA2C43",
        fg="#FFB5C0"
    )
    title.pack(pady=5)

    epoch_button_frame=tk.Frame(
        epoch_frame,
        bg="#DA2C43"
    )
    epoch_button_frame.pack(pady=5)

    epochgraph_btn=tk.Button(
        epoch_button_frame, 
        text="Graph",
        width=15,
        bg="#D20A2E",
        fg="#FFB5C0",
        height=2,
        command=lambda:show_graph(gen_epochgraph())
    )
    epochgraph_btn.pack(side="left", padx=10)

    epochstat_btn=tk.Button(
        epoch_button_frame, 
        text="Statistics",
        width=15,
        bg="#D20A2E",
        fg="#FFB5C0",
        height=2,
        command=gen_epochstat
    )
    epochstat_btn.pack(side="left", padx=10)
