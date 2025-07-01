import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk

def stretch_image(event):
    global resized_tk

    # size
    width = event.width
    height = event.height

    # create an image
    resized_image = image_original.resize((width, height))
    resized_tk = ImageTk.PhotoImage(resized_image)

    # place on the canvas
    canvas.create_image(0,0, image = resized_tk, anchor = 'nw')

def fill_image(event):
    global resized_tk

    # current ratio
    canvas_ratio = event.width / event.height

    # get coordinates
    if canvas_ratio > image_ratio:
        width = int(event.width)
        height = int(width / image_ratio)
    else:
        height = int(event.height)
        width = int(height * image_ratio)

    resized_image = image_original.resize((width, height))
    resized_tk = ImageTk.PhotoImage(resized_image)
    canvas.create_image(int(event.width / 2), int (event.height / 2), image = resized_tk, anchor = 'center')

# exercise:
# create a third scaling behavior to always show the full image without cutting off parts

def show_full_image(event):
    global resized_tk

    # current ratio
    canvas_ratio = event.width / event.height

    # get coordinates
    if canvas_ratio > image_ratio:
        height = int(event.height)
        width = int(height * image_ratio)
    else:
        width = int(event.width)
        height = int(width / image_ratio)

    resized_image = image_original.resize((width, height))
    resized_tk = ImageTk.PhotoImage(resized_image)
    canvas.create_image(int(event.width / 2), int (event.height / 2), image = resized_tk, anchor = 'center')

# setup
window = tk.Tk()
window.geometry('600x400')
window.title('Images')

# grid layout
window.columnconfigure((0,1,2,3), weight = 1, uniform = 'a')
window.rowconfigure(0, weight = 1)

# import an image
image_original = Image.open('assets\dolphin.jpg')
image_ratio = image_original.size[0] / image_original.size[1]
image_width = image_original.size[0]
image_height = image_original.size[1]
image_tk = ImageTk.PhotoImage(image_original)

python_dark = Image.open('assets\python_dark.png').resize((30,30))
python_dark_tk = ImageTk.PhotoImage(python_dark)

python_dark = Image.open('assets\python_light.png').resize((30,30))
img_ctk = ctk.CTkImage(light_image = python_dark, dark_image = python_dark)

# widget
# label = ttk.Label(window, text = 'dolphin', image = image_tk)
# label.pack()
button_frame = ttk.Frame(window)
# button
button = ttk.Button(button_frame, text = '    A button', image = python_dark_tk , compound = 'left')
button.pack(pady = 10)

button_ctk = ctk.CTkButton(button_frame, text = '    A button', image = img_ctk , compound = 'left')
button_ctk.pack(pady = 10)

button_frame.grid(column = 0, row = 0, sticky = 'nsew')

# canvas -> image
canvas = tk.Canvas(window, background = 'red', bd = 0, highlightthickness = 0, relief = 'ridge')
canvas.grid(column = 1, columnspan = 3, row = 0, sticky = 'nsew')

canvas.bind('<Configure>', show_full_image)

# run
window.mainloop()