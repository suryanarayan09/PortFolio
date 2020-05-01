#from django.test import TestCase

# Create your tests here.
from tkinter import *
from tkinter import messagebox
import matplotlib
from os import listdir
import os
from tkinter import filedialog
import cv2
import PIL.Image, PIL.ImageTk
import tkinter

Frame = Tk()
Frame.geometry("200x300")
Frame.title("suraj")

def load_photo_tab_two(file_path):
    # Create a window
    window = Tk()
    window.title("OpenCV and Tkinter")

    # Load an image using OpenCV
    cv_img = cv2.cvtColor(cv2.imread("../media/pics/photo.png"), cv2.COLOR_BGR2RGB)

    # Get the image dimensions (OpenCV stores image data as NumPy ndarray)
    height, width, no_channels = cv_img.shape

    # Create a canvas that can fit the above image
    canvas = Canvas(window, width=width, height=height)
    canvas.pack()

    # Use PIL (Pillow) to convert the NumPy ndarray to a PhotoImage
    photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))

    # Add a PhotoImage to the Canvas
    canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)

    # Run the window loop
    window.mainloop()

def select_image():
    global image_select
    global image_file_name
    global file_new_home
    global file_to_copy
    path_to_image = filedialog.askopenfilename(initialdir="/", title="Open File", filetype=(("PNGs", "*.png"), ("GIFs", "*.gif"), ("All Files", "*.*")))
    try:
        if path_to_image:
            image_file_name = os.path.basename(path_to_image)
            #file_new_home = sqlite_config.PHOTO_Directory + image_file_name
            file_to_copy = path_to_image
            image_select = True
            load_photo_tab_two(file_to_copy)
    except IOError as err:
        image_select = False
        messagebox.showinfo("File Error", err)

#about image of paragraph
AboutImage = Canvas(Frame, bg="blue", height=105, width=70)
AboutImage.grid(row=0, column=0, rowspan=3, columnspan=2)

ButtonAddImage = Button(Frame,text="Add Image", fg="red", bg="black", width=5)
ButtonSaveImage = Button(Frame, text="save", fg="red", bg="black", width=5)
ButtonResetImage = Button(Frame, text="reset", fg="red", bg="black", width=5)
ButtonAddImage.configure(command=select_image)
ButtonSaveImage.configure()
ButtonResetImage.configure()
ButtonAddImage.grid(row=0, column=2)
ButtonSaveImage.grid(row=1, column=2)
ButtonResetImage.grid(row=2, column=2)



S = Scrollbar(Frame)
AboutTextArea = Text(Frame, height=10, width=17)
S.grid(row=3, column=5, rowspan=3)
AboutTextArea.grid(row=3, column=0, rowspan=3, columnspan=5)
S.config(command=AboutTextArea.yview)
AboutTextArea.config(yscrollcommand=S.set)
quote = """HAMLET: To be, or not to be--that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune
Or to take arms against a sea of troubles
And by opposing end them. To die, to sleep--
No more--and by a sleep to say we end
The heartache, and the thousand natural shocks
That flesh is heir to. 'Tis a consummation
Devoutly to be wished."""
AboutTextArea.insert(END, quote)

ButtonAddPara = Button(Frame,text="Add Image", fg="red", bg="black", width=5)
ButtonSavePara = Button(Frame, text="save", fg="red", bg="black", width=5)
ButtonResetPara = Button(Frame, text="reset", fg="red", bg="black", width=5)
ButtonAddPara.configure(command=select_image)
ButtonSavePara.configure()
ButtonResetPara.configure()
ButtonAddPara.grid(row=3, column=6)
ButtonSavePara.grid(row=4, column=6)
ButtonResetPara.grid(row=5, column=6)

Frame.mainloop()
