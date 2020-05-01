from tkinter import *
import numpy as np
import math
import time
from tkinter import messagebox
import matplotlib
from os import listdir
import os
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Window(Frame):
    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        self.frame = None
        self.panel = None

        # parameters that you want to send through the Frame class.
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    # Function for the creation of Initial Window of GUI
    def init_window(self):
        # changing the title of our master widget
        self.master.title("Suryanarayan Kumar")

        # packing the frame
        self.pack(fill=BOTH, expand=1)
        self.title = Label(self, text="Update your Info and create PortFolio.", font="Verdana 10 bold", fg="blue", bg="yellow")
        self.title.place(x=400, y=5)

        self.base_btn = Button(self, text="Save", height=2, width=5, fg="red", bg="black", font="Verdana 10 bold")
        self.base_btn.configure()
        self.base_btn.grid(row=1, column=0, pady=1, rowspan=2, columnspan=2)

        self.base_timer = StringVar()
        self.base_timer.set("Time\nLeft:")

        self.base_timer_label = Label(self, textvariable=self.base_timer)
        self.base_timer_label.grid(row=1, column=1, pady=1)

        self.solution = Label(self, text="Start Solution Test")
        self.solution.grid(row=2, padx=5, pady=1)

        self.solution_btn = Button(self, text="Start", height=2, width=4, fg="red")
        self.solution_btn.configure()
        self.solution_btn.grid(row=3, column=0, pady=1)

        self.solution_timer = StringVar()
        self.solution_timer.set("Time\nLeft:")

        self.solution_timer_label = Label(self, textvariable=self.solution_timer)
        self.solution_timer_label.grid(row=3, column=1, pady=1)

        self.result = Label(self, text="Plot Results")
        self.result.grid(row=4, padx=5, pady=1)

        self.result_btn = Button(self, text="Plot", height=2, width=4, fg="red", bg="black")
        self.result_btn.configure()
        self.result_btn.grid(row=5, padx=5, pady=1)

        self.reset_exp = Label(self, text="Reset Experiment")
        self.reset_exp.grid(row=6, padx=5, pady=1)

        self.reset_exp_btn = Button(self, text="Reset", height=2, width=4, fg="red", bg="black")
        self.reset_exp_btn.configure()
        self.reset_exp_btn.grid(row=7, padx=5, pady=1)

        self.save_file = Label(self, text="Save Experiment")
        self.save_file.grid(row=8, padx=5, pady=1)

        self.save_file_btn = Button(self, text="Save", height=2, width=4, fg="red", bg="black")
        self.save_file_btn.configure()
        self.save_file_btn.grid(row=9, padx=5, pady=1)

        self.open_file = Label(self, text="Open Experiment")
        self.open_file.grid(row=10, padx=5, pady=1)

        self.open_file_btn = Button(self, text="Select", height=2, width=4, fg="red", bg="black")
        self.open_file_btn.configure()
        self.open_file_btn.grid(row=11, padx=5, pady=1)

        self.power_off = Label(self, text="Power Off")
        self.power_off.grid(row=12, padx=5, pady=1)

        self.power_off_btn = Button(self, text="Select", height=2, width=4, fg="red", bg="black")
        self.power_off_btn.configure()
        self.power_off_btn.grid(row=13, padx=5, pady=0)

        f = Figure(figsize=(5.5, 4), dpi=100)
        self.a = f.add_subplot(111)
        self.a.set_title("Wavelength vs Absorption Graph")
        self.a.set_xlabel("Wavelength")
        self.a.set_ylabel("Absorption")
        self.a.set_xlim(xmin=370, xmax=760)  # a.set_ylim(ymin= ,ymax=)

        self.Canvas1 = Canvas(self)
        self.Canvas1 = FigureCanvasTkAgg(f, self)
        self.Canvas1.draw()
        self.Canvas1.get_tk_widget().place(x=235, y=40)

        toolbarFrame = Frame(self)
        toolbarFrame.place(x=235, y=5)


def main():
    root = Tk()
    # root.geometry('%dx%d+%d+%d' % (800, 480, 0, -30))
    root.geometry("1000x600")
    #root.resizable(False, False)
    root.title("DIC")

    canva = Canvas(root, bg="blue", height=150, width=152)
    canva.place(x=100, y=100)

    # creation of an instance
    app = Window(root)
    # mainloop
    root.mainloop()


if __name__ == '__main__':     main()
