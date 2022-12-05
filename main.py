import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
break_time = 0


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    seconds = 1
    countdown(seconds)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    global break_time

    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(time_text, text=f"{minutes}:{seconds}")
    if count > 0 and break_time == 0:
        if count == 1:
            break_time = 1
            countdown(5)
        else:
            window.after(1000, countdown, count - 1)

    if count > 0 and break_time == 1:
        if count == 1:
            break_time = 0
            countdown(10)
        else:
            window.after(1000, countdown, count - 1)



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
checkmark_label = tkinter.Label(text="✔", fg=GREEN, bg=YELLOW)
checkmark_label.grid(column=1, row=3)

window.mainloop()
