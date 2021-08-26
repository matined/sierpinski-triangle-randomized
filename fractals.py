from tkinter import *
import random
import time

NUMBER_OF_POINTS = 3
SIZE = 700
FIRST_COLOR = "black"
SECOND_COLOR = "white"
CUSP_COLOR = "lawngreen"


class Cusp:
    def __init__(self, x, y, tag):
        self.x = x
        self.y = y
        self.tag = tag
        self.create_point()
        self.create_tag()

    def create_point(self):
        self.o = canvas.create_oval(
            self.x-3, self.y-3, self.x+3, self.y+3, fill=CUSP_COLOR, outline=CUSP_COLOR)

    def create_tag(self):
        self.t = canvas.create_text(
            self.x+10, self.y-10, text=self.tag, fill=CUSP_COLOR)


def create_window():
    global window
    window = Tk()
    window.geometry(f"{SIZE}x{SIZE}")
    window.resizable(height=False, width=False)
    window.config(bg=FIRST_COLOR)
    window.title("fractals")


def create_fractal_canvas():
    global canvas
    canvas = Canvas(width=SIZE, height=SIZE,
                    bg=FIRST_COLOR, highlightthickness=0)
    canvas.pack()
    random.seed()

    global points
    points = 0

    global counter
    counter = canvas.create_text(
        100, 25, text=f"points: {points}", fill=SECOND_COLOR, font=("Arial", 15, "bold"))


def place(last_x, last_y):
    which_cusp = random.randint(0, len(cusps)-1)
    new_x = (last_x + cusps[which_cusp].x)//2
    new_y = (last_y + cusps[which_cusp].y)//2
    canvas.create_oval(new_x-1, new_y-1, new_x+1, new_y+1,
                       fill=SECOND_COLOR, outline=SECOND_COLOR)
    return (new_x, new_y)


def draw_points():
    global cusps
    cusps = []

    for i in cuspsInfo:
        cusps.append(Cusp(i[0], i[1], i[2]))

    x = 100
    y = 100
    points = 0
    while True:
        new = place(x, y)
        x = new[0]
        y = new[1]
        points += 1
        canvas.itemconfig(counter, text=f"points: {points}")
        window.update()
        time.sleep(0.001)


def add_clicked(inputs):
    cuspsInfo.append((int(inputs[0].get()), int(
        inputs[1].get()), inputs[2].get()))
    inputs[0].delete(0, END)
    inputs[1].delete(0, END)
    inputs[2].delete(0, END)


def run_clicked(objects):
    objects[0].destroy()
    objects[1].destroy()
    objects[2].destroy()
    objects[3].destroy()
    objects[4].destroy()
    objects[5].destroy()
    objects[6].destroy()
    objects[7].destroy()
    objects[8].destroy()
    create_fractal_canvas()
    draw_points()


def startup_menu():
    global cuspsInfo
    cuspsInfo = []
    label = Label(window, text="Add a cusp:", font=(
        "Arial", 20, "bold"), fg=SECOND_COLOR, bg=FIRST_COLOR)
    label.place(relx=0.5, rely=0.3, anchor=CENTER)

    xInput = Entry(window)
    xInput.place(relx=0.52, rely=0.4, anchor=CENTER)
    yInput = Entry(window)
    yInput.place(relx=0.52, rely=0.45, anchor=CENTER)
    indexInput = Entry(window)
    indexInput.place(relx=0.52, rely=0.5, anchor=CENTER)

    xLabel = Label(window, text=f"x(0-{SIZE}):", font=(
        "Arial", 20, "bold"), fg=SECOND_COLOR, bg=FIRST_COLOR)
    xLabel.place(relx=0.34, rely=0.4, anchor=CENTER)
    yLabel = Label(window, text=f"y(0-{SIZE}):", font=(
        "Arial", 20, "bold"), fg=SECOND_COLOR, bg=FIRST_COLOR)
    yLabel.place(relx=0.34, rely=0.45, anchor=CENTER)
    indexLabel = Label(window, text="name:", font=(
        "Arial", 20, "bold"), fg=SECOND_COLOR, bg=FIRST_COLOR)
    indexLabel.place(relx=0.36, rely=0.5, anchor=CENTER)

    addButton = Button(window, text="add", command=lambda: add_clicked(
        (xInput, yInput, indexInput)))
    addButton.place(relx=0.45, rely=0.6, anchor=CENTER)
    runButton = Button(window, text="run", command=lambda: run_clicked(
        (label, xInput, yInput, indexInput, xLabel, yLabel, indexLabel, addButton, runButton)))
    runButton.place(relx=0.55, rely=0.6, anchor=CENTER)


def main():
    create_window()
    startup_menu()
    window.mainloop()


if __name__ == "__main__":
    main()
