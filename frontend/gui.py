import tkinter as tk
import frontend.tsearch_front as search
import frontend.analytics_front as analytics
import frontend.livetracker_front as tracker
root=tk.Tk()
root.title("OrbitEye")
root.geometry("900x650")
root.resizable(False, False)
root.configure(bg="#DA2C43")
root.activebackground="#B00826"
root.activeforeground="white"
cursor="hand2"
title=tk.Label(
    root,
    text="⋆｡‧˚ʚ ୨ৎ ɞ˚‧｡⋆OrbitEye⋆｡‧˚ʚ ୨ৎ ɞ˚‧｡⋆",
    font=("Segoe UI",28,"italic"),
    bg="#DA2C43",
    fg="#FFB5C0"
)
title.pack(pady=(20,20))

subtitle=tk.Label(
    root,
    text="Search ✦ Analyze ✦ Live Tracking",
    font=("Segoe UI",13,"italic"),
    bg="#DA2C43",
    fg="#FFB5C0"
)
subtitle.pack(pady=(10,10))

search_btn=tk.Button(
    root,
    text="Search",
    width="25",
    bg="#D20A2E",
    fg="#FFB5C0",
    height=3,
    font=("Segoe UI",10,"italic"),
    command=search.search
)
search_btn.pack(pady=(20,20))

analytics_btn=tk.Button(
    root,
    text="Analysis",
    width="25",
    bg="#D20A2E",
    fg="#FFB5C0",
    height=3,
    font=("Segoe UI",10,"italic"),
    command=analytics.analytics
)
analytics_btn.pack(pady=(20,20))


livetracker_btn=tk.Button(
    root,
    text="Live Tracker",
    width="25",
    bg="#D20A2E",
    fg="#FFB5C0",
    height=3,
    font=("Segoe UI",10,"italic"),
    command=tracker.livetracker
)
livetracker_btn.pack(pady=(20,20))


exit_btn=tk.Button(
    root,
    text="Exit",
    width="25",
    bg="#D20A2E",
    fg="#FFB5C0",
    height=3,
    font=("Segoe UI",10,"italic"),
    command=root.destroy
)
exit_btn.pack(pady=(20,20))

footer=tk.Label(
    root,
    text="OrbitEye ©️ 2026",
    font=("Segoe UI",10,"italic"),
    bg="#DA2C43",
    fg="#FFB5C0"
)
footer.pack(pady=(10,10))

