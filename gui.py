from tkinter import *
from PIL import Image, ImageTk
import action
import spech_to_text
import os

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))


# ================== LOGIQUE (inchangée) ==================
def User_send():
    send = entry1.get()
    bot = action.Action(send)
    # Message utilisateur
    text.insert(END, "💬 Vous : " + send + "\n")
    # Message bot
    if bot is not None:
        text.insert(END, "🤖 Assistant IA : " + str(bot) + "\n")
    if bot == "ok sir":
        root.destroy()

def ask():
    ask_val = spech_to_text.spech_to_text()

    if not ask_val:
        text.insert(END, "💬 Vous : [entrée vocale indisponible]\n")
        return

    bot_val = action.Action(ask_val)
    text.insert(END, "💬 Vous : " + ask_val + "\n")
    if bot_val is not None:
        text.insert(END, "🤖 Assistant IA : " + str(bot_val) + "\n")
    if bot_val == "ok sir":
        root.destroy()

def delete_text():
    text.delete("1.0", "end")

# ================== FUTURISTIC DARK NEON THEME ==================
BG_MAIN       = "#050505"     # Deep black
CARD          = "#0c0f23"     # Very dark blue/indigo
CARD_GLASS    = "#11152e"     # Glassy indigo-blue
BORDER        = "#6d28d9"     # Electric purple glow
PRIMARY       = "#c026d3"     # Magenta/Pink neon (Send)
PRIMARY_H     = "#a21caf"     # Hover pink-purple
SECONDARY     = "#4f46e5"     # Indigo for accents
CYAN_GLOW     = "#00e5ff"     # Cyan/Teal neon
TEXT_MAIN     = "#e0e7ff"     # Soft blue-white text
TEXT_MUTED    = "#7dd3fc"     # Light cyan text
CHAT_BG       = "#0b1120"     # Dark blue chat bg
BTN_GRAY      = "#1e293b"     # Gray-blue buttons
BTN_GRAY_H    = "#334155"     # Hover gray-blue


# ================== MAIN WINDOW ==================
root = Tk()
root.geometry("850x600")
root.title("AI Assistant")
root.resizable(True, True)
root.config(bg=BG_MAIN)

# ================== HEADER ==================
header = Frame(root, bg=BG_MAIN)
header.pack(fill="x", padx=25, pady=(20, 10))

title_lbl = Label(
    header, text="Assistante Virtuel IA",
    font=("Segoe UI Semibold", 24, "bold"),
    bg=BG_MAIN, fg=CYAN_GLOW
)
title_lbl.pack(anchor="w")

subtitle_lbl = Label(
    header, text="Posez vos questions. Je suis là pour vous aider.",
    font=("Segoe UI", 10),
    bg=BG_MAIN, fg=TEXT_MUTED
)
subtitle_lbl.pack(anchor="w")

# Neon gradient bar
accent = Frame(root, bg=BG_MAIN)
accent.pack(fill="x", padx=25, pady=(0, 15))

bar_left  = Frame(accent, bg=PRIMARY, height=3)
bar_mid   = Frame(accent, bg=CYAN_GLOW, height=3)
bar_right = Frame(accent, bg=SECONDARY, height=3)

bar_left.pack(side="left", fill="x", expand=True)
bar_mid.pack(side="left", fill="x", expand=True)
bar_right.pack(side="left", fill="x", expand=True)

# ================== MAIN CONTENT ==================
content = Frame(root, bg=BG_MAIN)
content.pack(fill="both", expand=True, padx=25, pady=10)

content.columnconfigure(1, weight=1)
content.rowconfigure(0, weight=1)

# ---------- LEFT AVATAR PANEL ----------
left = Frame(content, bg=CARD, highlightthickness=2, highlightbackground=SECONDARY)
left.grid(row=0, column=0, sticky="ns", padx=(0, 15))

avatar_frame = Frame(left, bg=CARD)
avatar_frame.pack(padx=20, pady=(22, 10))

try:
    image_path = os.path.join(script_dir, "image", "assitant.png")
    avatar_img = Image.open(image_path).resize((180, 180))
    Display_Image = ImageTk.PhotoImage(avatar_img)
except:
    Display_Image = None

img_lbl = Label(avatar_frame, image=Display_Image, bg=CARD)
img_lbl.pack()

name_lbl = Label(
    left, text="ZENA",
    font=("Segoe UI", 12, "bold"),
    bg=CARD, fg=CYAN_GLOW
)
name_lbl.pack(pady=(8, 2))

status_lbl = Label(
    left, text="● en ligne",
    font=("Segoe UI", 9, "bold"),
    bg=CARD, fg="#22c55e"
)
status_lbl.pack()

hint_lbl = Label(
    left,
    text="Astuces:\n•  Parler: parlez avec moi\n•  Envoyer: envoyez votre message\n•  vider: tout supprimer",
    font=("Segoe UI", 9),
    bg=CARD, fg=TEXT_MUTED,
    justify="left"
)
hint_lbl.pack(padx=15, pady=15, anchor="w")

# ---------- RIGHT CHAT PANEL ----------
right = Frame(content, bg=CARD, highlightthickness=2, highlightbackground=SECONDARY)
right.grid(row=0, column=1, sticky="nsew")

right.rowconfigure(0, weight=1)
right.columnconfigure(0, weight=1)

chat_border = Frame(right, bg=SECONDARY)
chat_border.grid(row=0, column=0, sticky="nsew", padx=15, pady=15)

chat_frame = Frame(chat_border, bg=CHAT_BG)
chat_frame.pack(fill="both", expand=True, padx=1, pady=1)

text = Text(
    chat_frame, font=("Consolas", 11),
    bg=CHAT_BG, fg=TEXT_MAIN,
    wrap="word", bd=0, relief="flat",
    insertbackground=PRIMARY
)
text.pack(side="left", fill="both", expand=True, padx=(10, 0), pady=10)

scroll = Scrollbar(chat_frame, command=text.yview)
scroll.pack(side="right", fill="y", padx=6)
text.config(yscrollcommand=scroll.set)

text.insert("end", "💬 Bonjour! Je suis ton assistante IA.\nComment puis-je t’aider aujourd’hui ?\n\n")

# ================== INPUT AREA ==================
bottom = Frame(right, bg=CARD)
bottom.grid(row=1, column=0, sticky="ew", padx=15, pady=(0, 15))
bottom.columnconfigure(0, weight=1)

# Input box
entry_border = Frame(bottom, bg=CYAN_GLOW)
entry_border.grid(row=0, column=0, sticky="ew", padx=(0, 10))

entry_inner = Frame(entry_border, bg=CARD_GLASS)
entry_inner.pack(fill="x", padx=1, pady=1)

entry1 = Entry(
    entry_inner, font=("Segoe UI", 11),
    bg=CARD_GLASS, fg=TEXT_MAIN,
    bd=0, insertbackground=PRIMARY
)
entry1.pack(fill="x", padx=10, pady=8)

# Buttons
btn_frame = Frame(bottom, bg=CARD)
btn_frame.grid(row=0, column=1)

def hover(widget, normal, hover_color):
    widget.bind("<Enter>", lambda e: widget.config(bg=hover_color))
    widget.bind("<Leave>", lambda e: widget.config(bg=normal))

b_ask = Button(
    btn_frame, text="🎙 Parler",
    font=("Segoe UI", 9, "bold"),
    bg=BTN_GRAY, fg=TEXT_MAIN,
    bd=0, padx=12, pady=6,
    command=ask, cursor="hand2"
)
b_ask.grid(row=0, column=0, padx=3)
hover(b_ask, BTN_GRAY, BTN_GRAY_H)

b_clear = Button(
    btn_frame, text="🧹Vider",
    font=("Segoe UI", 9),
    bg=BTN_GRAY, fg=TEXT_MAIN,
    bd=0, padx=12, pady=6,
    command=delete_text, cursor="hand2"
)
b_clear.grid(row=0, column=1, padx=3)
hover(b_clear, BTN_GRAY, BTN_GRAY_H)

b_send = Button(
    btn_frame, text="➤ Envoyer",
    font=("Segoe UI", 10, "bold"),
    bg=PRIMARY, fg="white",
    bd=0, padx=16, pady=6,
    command=User_send, cursor="hand2"
)
b_send.grid(row=0, column=2, padx=3)
hover(b_send, PRIMARY, PRIMARY_H)

# ================== ANIMATIONS ==================
bar_colors = [PRIMARY, CYAN_GLOW, SECONDARY, "#9333ea"]  # electric purple

def animate_bar():
    animate_bar.index = (animate_bar.index + 1) % len(bar_colors)
    c1 = bar_colors[animate_bar.index]
    c2 = bar_colors[(animate_bar.index + 1) % len(bar_colors)]
    c3 = bar_colors[(animate_bar.index + 2) % len(bar_colors)]
    bar_left.config(bg=c1)
    bar_mid.config(bg=c2)
    bar_right.config(bg=c3)
    root.after(600, animate_bar)

animate_bar.index = 0
animate_bar()

status_colors = ["#22c55e", "#4ade80"]

def animate_status():
    animate_status.index = (animate_status.index + 1) % len(status_colors)
    status_lbl.config(fg=status_colors[animate_status.index])
    root.after(900, animate_status)

animate_status.index = 0
animate_status()

root.mainloop()