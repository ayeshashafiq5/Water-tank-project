from tkinter import *
from tkinter import messagebox
import winsound

# ---------------- WINDOW ----------------
root = Tk()
root.title("Water Tank Overflow Alarm System")
root.geometry("900x650")
root.config(bg="#dff6ff")

# ---------------- TITLE ----------------
title = Label(
    root,
    text="WATER TANK OVERFLOW ALARM SYSTEM",
    font=("Arial", 24, "bold"),
    bg="#dff6ff",
    fg="#003566"
)
title.pack(pady=15)

# ---------------- CANVAS ----------------
canvas = Canvas(root, width=350, height=450, bg="#dff6ff", highlightthickness=0)
canvas.place(x=50, y=100)

# Tank Outline
canvas.create_rectangle(100, 50, 250, 400, width=4)

# Water (Animated)
water = canvas.create_rectangle(102, 398, 248, 398, fill="#4ea8de", outline="#4ea8de")

# Level Lines
canvas.create_line(100, 320, 250, 320, dash=(4, 2))
canvas.create_line(100, 240, 250, 240, dash=(4, 2))
canvas.create_line(100, 160, 250, 160, dash=(4, 2))
canvas.create_line(100, 80, 250, 80, dash=(4, 2))

# Labels
canvas.create_text(60, 320, text="LOW", font=("Arial", 12, "bold"))
canvas.create_text(45, 240, text="MEDIUM", font=("Arial", 12, "bold"))
canvas.create_text(55, 160, text="HIGH", font=("Arial", 12, "bold"))
canvas.create_text(55, 80, text="FULL", font=("Arial", 12, "bold"))

# ---------------- STATUS PANEL ----------------
panel = Frame(root, bg="white", bd=3, relief="ridge")
panel.place(x=450, y=120, width=350, height=320)

heading = Label(
    panel,
    text="LEVEL INDICATORS",
    font=("Arial", 18, "bold"),
    bg="white",
    fg="#003566"
)
heading.pack(pady=10)

low_led = Label(panel, text="LOW LEVEL", width=20, height=2, bg="gray", fg="white", font=("Arial", 12, "bold"))
low_led.pack(pady=5)

medium_led = Label(panel, text="MEDIUM LEVEL", width=20, height=2, bg="gray", fg="white", font=("Arial", 12, "bold"))
medium_led.pack(pady=5)

high_led = Label(panel, text="HIGH LEVEL", width=20, height=2, bg="gray", fg="white", font=("Arial", 12, "bold"))
high_led.pack(pady=5)

full_led = Label(panel, text="FULL LEVEL", width=20, height=2, bg="gray", fg="white", font=("Arial", 12, "bold"))
full_led.pack(pady=5)

# ---------------- BUZZER ----------------
buzzer_label = Label(
    root,
    text="BUZZER OFF",
    font=("Arial", 18, "bold"),
    bg="black",
    fg="white",
    width=20
)
buzzer_label.place(x=470, y=470)

# ---------------- FUNCTIONS ----------------
def reset_leds():
    low_led.config(bg="gray", fg="white")
    medium_led.config(bg="gray", fg="white")
    high_led.config(bg="gray", fg="white")
    full_led.config(bg="gray", fg="white")

    buzzer_label.config(text="BUZZER OFF", bg="black")

def animate_water(target_y):
    current = canvas.coords(water)

    while current[1] > target_y:
        canvas.coords(water, 102, current[1]-2, 248, 398)
        root.update()
        current = canvas.coords(water)

def low_level():
    reset_leds()
    animate_water(320)
    low_led.config(bg="green")

def medium_level():
    reset_leds()
    animate_water(240)
    low_led.config(bg="green")
    medium_led.config(bg="yellow", fg="black")

def high_level():
    reset_leds()
    animate_water(160)
    low_led.config(bg="green")
    medium_led.config(bg="yellow", fg="black")
    high_led.config(bg="orange")

def full_level():
    reset_leds()
    animate_water(80)

    low_led.config(bg="green")
    medium_led.config(bg="yellow", fg="black")
    high_led.config(bg="orange")
    full_led.config(bg="red")

    buzzer_label.config(text="BUZZER ON", bg="red")

    # Buzzer Sound
    for i in range(3):
        winsound.Beep(1000, 300)

def empty_tank():
    reset_leds()
    canvas.coords(water, 102, 398, 248, 398)

# ---------------- BUTTONS ----------------
btn_frame = Frame(root, bg="#dff6ff")
btn_frame.place(x=120, y=560)

Button(
    btn_frame,
    text="LOW",
    font=("Arial", 12, "bold"),
    bg="green",
    fg="white",
    width=10,
    command=low_level
).grid(row=0, column=0, padx=10)

Button(
    btn_frame,
    text="MEDIUM",
    font=("Arial", 12, "bold"),
    bg="yellow",
    width=10,
    command=medium_level
).grid(row=0, column=1, padx=10)

Button(
    btn_frame,
    text="HIGH",
    font=("Arial", 12, "bold"),
    bg="orange",
    width=10,
    command=high_level
).grid(row=0, column=2, padx=10)

Button(
    btn_frame,
    text="FULL",
    font=("Arial", 12, "bold"),
    bg="red",
    fg="white",
    width=10,
    command=full_level
).grid(row=0, column=3, padx=10)

Button(
    btn_frame,
    text="RESET",
    font=("Arial", 12, "bold"),
    bg="black",
    fg="white",
    width=10,
    command=empty_tank
).grid(row=0, column=4, padx=10)

# ---------------- MAIN LOOP ----------------
root.mainloop()
