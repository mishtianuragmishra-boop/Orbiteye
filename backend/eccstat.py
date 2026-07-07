import tkinter as tk

def gen_eccstat():
    popup=tk.Toplevel()
    popup.title("Eccentricity")
    popup.geometry("350x150")
    popup.configure(bg="#DA2C43")
    tk.Label(
        popup,
        text="Generating Eccentricity Statistics . . . .",
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
  
