import tkinter as tk
from frontend import gui
from backend.livetracker import livetracker as backend_tracker

def livetracker():
    window=tk.Toplevel(gui.root)
    window.title("Live Tracker")
    window.geometry("700x500")
    window.configure(bg="#DA2C43")

    title=tk.Label(
        window,
        text="Live tracker",
        font=("Segoe UI",22,"italic"),
        bg="#DA2C43",
        fg="#FFB5C0"
    )

    title.pack(pady=15)

    search_label=tk.Label(
        window,
        text="Satellite Name/Norad ID",
        bg="#DA2C43",
        fg="#FFB5C0",
        font=("Segoe UI",15,"bold")
    )
    search_label.pack()

    satellite_entry=tk.Entry(
        window,
        width=40,
        font=("Segoe UI",14),
        justify="center"
    )
    satellite_entry.pack(pady=10)

    def track():
        satname=satellite_entry.get()
        result=backend_tracker(satname)
        if result is None:
            status.config(text="Status: Satellite not found")
            satellite_name.config(text=f"Satellite : -------")
            latitude.config(text=f"Latitude : -------")
            longitude.config(text=f"Longitude : -------")
            altitude.config(text=f"Altitude : -------")
            velocity.config(text=f"Velocity: -------")
            return
        status.config(text="Status : Tracking")
        satellite_name.config(text=f"Satellite : {result['Name']}")
        latitude.config(text=f"Latitude : {result['Latitude']}°")
        longitude.config(text=f"Longitude : {result['Longitude']}°")
        altitude.config(text=f"Altitude : {result['Altitude']}km")
        velocity.config(text=f"Velocity: {result['Velocity']}km/s")

    track_btn=tk.Button(
        window,
        text="Track",
        width=20,
        height=2,
        bg="#DA2C43",
        fg="#FFB5C0",
        font=("Segoe UI",14,"italic"),
        command=track
    )
    track_btn.pack(pady=20)

    info_frame=tk.Frame(
        window,
        bg="#DA2C43"
    )
    info_frame.pack(pady=20)

    satellite_name=tk.Label(
        info_frame,
        text="Satellite",
        bg="#DA2C43",
        fg="#FFB5C0",
        font=("Segoe UI",15,"italic")
    )
    satellite_name.pack(anchor="w",pady=10)

    status=tk.Label(
        info_frame,
        text="Status . . . .waiting . .",
        font=("Segoe UI",15,"italic"),
        bg="#DA2C43",
        fg="#FFB5C0"
    )
    status.pack(anchor="w",pady=10)

    latitude=tk.Label(
        info_frame,
        text="Latitude . . .  .",
        font=("Segoe UI",15,"italic"),
        bg="#DA2C43",
        fg="#FFB5C0"
    )
    latitude.pack(anchor="w",pady=10)

    longitude=tk.Label(
        info_frame,
        text="Longitude . . .  .",
        font=("Segoe UI",15,"italic"),
        bg="#DA2C43",
        fg="#FFB5C0"
    )
    longitude.pack(anchor="w",pady=10)

    altitude=tk.Label(
        info_frame,
        text="Altitude . . .  .",
        font=("Segoe UI",15,"italic"),
        bg="#DA2C43",
        fg="#FFB5C0"
        )
    altitude.pack(anchor="w",pady=10)

    velocity=tk.Label(
        info_frame,
        text="Velocity . . .  .",
        font=("Segoe UI",15,"italic"),
        bg="#DA2C43",
        fg="#FFB5C0"
    )
    velocity.pack(anchor="w",pady=10)

    footer=tk.Label(
        info_frame,
        text="OrbitEye ©️ 2026",
        font=("Segoe UI",15,"italic"),
        bg="#DA2C43",
        fg="#FFB5C0"
    )
    footer.pack(side="bottom",pady=10)
    
