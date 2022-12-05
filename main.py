import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.10
SHORT_BREAK_MIN = 0.05
LONG_BREAK_MIN = 20
reps = 0


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60
    mark=""

    if reps % 8 == 0:  # If it is the 8th rep
        countdown(long_break_seconds)
        timer_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:  # If it s the 2nd, 4th or 6th rep
        countdown(short_break_seconds)
        timer_label.config(text="Short Break", fg=PINK)
    else:  # If it s the 1st, 3rd, 5th or 7th rep
        countdown(work_seconds)
        timer_label.config(text="Work time", fg=GREEN)

    if reps % 2 == 0:
        mark += "✔️"
        # checkmark_label.config(text=mark)
        checkmark_label['text'] += mark





# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(time_text, text=f"{minutes}:{seconds}")
    if count > 0:
        window.after(1000, countdown, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
# Window

window = tkinter.Tk()
window.title("Pomodoro Timer")
window.minsize(width=400, height=400)
window.configure(bg=YELLOW)
window.config(padx=20, pady=20)

# Timer Label
timer_label = tkinter.Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50,), bg=YELLOW)
timer_label.grid(column=1, row=0)

# Canvas
canvas = tkinter.Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
tomatoe_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomatoe_img)
time_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Start Button
Start_button = tkinter.Button(text="Start", highlightthickness=0, command=start_timer)
Start_button.grid(column=0, row=2)

# Reset Button
reset_button = tkinter.Button(text="Reset", )
reset_button.grid(column=2, row=2)

# Label
checkmark_label = tkinter.Label( fg=GREEN, bg=YELLOW)
checkmark_label.grid(column=1, row=3)

window.mainloop()
