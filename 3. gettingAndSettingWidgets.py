import tkinter as tk
from tkinter import ttk

def button_func():
    label['text'] = entry.get()
    entry['state'] = 'disabled'
    # print(label.configure())

def button2_func():
    label['text'] = 'some text'
    entry['state'] = 'enabled'

# window
window = tk.Tk()
window.title('Getting and setting widgets')

# widgets
label = ttk.Label(master = window, text = 'Some text')
label.pack()
entry = ttk.Entry(master = window)
entry.pack()
button = ttk.Button(master = window, text = 'The button', command = button_func)
button.pack()

# exercise
# add another button that changes text back to 'some text' and that enables entry
button2 = ttk.Button(master = window, text = 'The button2', command = button2_func)
button2.pack()

# run
window.mainloop()