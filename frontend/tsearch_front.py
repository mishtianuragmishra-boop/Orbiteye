import tkinter as tk
from frontend import gui
import frontend.namesearch_front as namesearch_front
import frontend.noradsearch_front as noradsearch_front


def search():
    window=tk.Toplevel(gui.root)
    window.title("SEARCH")
    window.geometry("700x500")
    window.configure(bg="#DA2C43")

    title=tk.Label(
        window,
        text="Search",
        font=("Segoe UI",22,"italic"),
        bg="#DA2C43",
        fg="#FFB5C0"
    )
    title.pack(pady=20)

    name_btn=tk.Button(
        window,
        text="Search by Name",
        width=22,
        bg="#D20A2E",
        fg="#FFB5C0",
        height=2,
        command=namesearch_front.namesearch
    )
    name_btn.pack(pady=(10,20))

    norad_btn=tk.Button(
        window,
        text="Search by Norad ID",
        width=22,
        bg="#D20A2E",
        fg="#FFB5C0",
        height=2,
        command=noradsearch_front.noradsearch
    )
    norad_btn.pack(pady=(10,20))
    