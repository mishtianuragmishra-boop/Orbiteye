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


    #main analytics window
    try:
        print("1")
        window=tk.Toplevel(gui.root)
        window.title("Analytics")
        window.geometry("1200x950")
        window.configure(bg="#DA2C43")


    #mainframe

        print("2")
        main_frame=tk.Frame(
            window,
            bg="#DA2C43"
        )
        main_frame.pack(fill="both",expand=True)


    #gaphframe

        print("3") 
        graph_frame=tk.Frame(
            main_frame,
            bg="#FFF5F8",
            width=700,
            height=850
        )
        graph_frame.pack(side="left",padx=20,pady=20)
        graph_frame.pack_propagate(False)


#right control frame
        print("4")
        controls_frame=tk.Frame(
            main_frame,
            bg="#DA2C43",
            width=350,
            height=850
        )


        controls_frame.pack(side="right",padx=20,pady=20,fill="y")


        controls_frame.pack_propagate(False)
        print("controlframe")


#showing graph function

        def show_graph(fig):
            print("Show graph called")
            print(fig)
            for widget in graph_frame.winfo_children():
                widget.destroy()
            canvas=FigureCanvasTkAgg(fig,master=graph_frame)
            canvas.draw()
            widget=canvas.get_tk_widget()
            widget.pack(
                fill="both",
                expand=True
            )
            graph_frame.update_idletasks()
            print("canvas packed")


#title
        print("6")
        title=tk.Label(
            controls_frame,
            text="Analytics",
            font=("Segoe UI",30,"italic","bold"),
            bg="#DA2C43",
            fg="#FFB5C0"
        )
        title.pack(pady=15)
        print("ttt-timetotwice")


#helper for making ever single analytics function
        print("7")

        def add_section(title,graph_function,stat_function):
            print("Creating")
            frame=tk.Frame(
            controls_frame,
            bg="#DA2C43"
             )
            frame.pack(pady=15)
            print(title,"frame ok")

            tk.Label(
                frame,
                text=title,
                font=("Segoe UI",15,"italic"),
                bg="#DA2C43",
                fg="#FFB5C0"
            ).pack()
            print(title,"label ok")

            button_frame=tk.Frame(
                frame,
                bg="#DA2C43"
            )
            button_frame.pack(pady=5)
            print(title,"button frame ok")

            tk.Button(
                button_frame,
                text="Graph",
                width=15,
                height=2,
                bg="#D20A2E",
                fg="#FFB5C0",
                command=lambda:show_graph(graph_function())
            ).pack(side="left",padx=10)
            print(title,"graph button ok")


            tk.Button(
                button_frame,
                text="Statistics",
                width=15,
                height=2,
                bg="#D20A2E",
                fg="#FFB5C0",
                command=stat_function
            ).pack(side="left",padx=10)
            print(title,"stats button ok")

    #sections


        add_section(
                "BSTAR",
                gen_bstargraph,
                gen_bstarstats
            )
        add_section(
            "Inclination",
            gen_incgraph,
            gen_incstat
        )
        add_section(
            "Mean Motion",
            gen_meanmotiongraph,
            gen_meanmotionstat
        )
        add_section(
            "Epoch",
            gen_epochgraph,
            gen_epochstat
        )
        add_section(
            "Eccentricity",
            gen_eccgraph,
            gen_eccstat
               
        )
    except Exception as e:
        import traceback
        traceback.print_exc()



