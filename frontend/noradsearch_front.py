import tkinter as tk
from frontend import gui
import backend.tsearch as tsearch
def noradsearch():
    window=tk.Toplevel(gui.root)
    window.title("Search by NORAD ID")
    window.geometry("700x500")
    window.configure(bg="#DA2C43")

    title=tk.Label(
        window,
        text="Search by NORAD ID",
        font=("Segoe UI",22,"italic"),
        bg="#DA2C43",
        fg="#FFB5C0"
    )
    title.pack(pady=20)

    noradentry=tk.Entry(
        window,
        width=30,
        font=("Segoe UI",14),
        bg="#D20A2E",
        fg="#FFB5C0"
    )
    noradentry.pack(pady=(10,20))

    result=tk.Label(
        window,
        text="",
        font=("Segoe UI",14),
        bg="#DA2C43",
        fg="#FFB5C0",
        justify="left" 
    )
    result.pack(pady=20)

    def searchsatellite():
        satellite=tsearch.searchbynoradid(noradentry.get())
        if satellite is None:
            result.config(text="Satellite not found")
            return
        text=""
        for key, value in satellite.items():
            text+=f"{key}: {value}\n"
        result.config(text=text)
    search_btn=tk.Button(
        window,
        text="Search",
        width=25,
        height=2,
        bg="#D20A2E",
        fg="#FFB5C0",
        command=searchsatellite
    )
    search_btn.pack(pady=10)