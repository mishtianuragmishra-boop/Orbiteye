import tkinter as tk

def gen_incstat():
    popup=tk.Toplevel()
    popup.title("Inclination")
    popup.geometry("350x150")
    popup.configure(bg="#DA2C43")
    tk.Label(
        popup,
        text="Generating Inclination Statistics . . . .",
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
  
