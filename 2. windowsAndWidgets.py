import tkinter as tk
from tkinter import ttk

def button_function():
    print('a button was pressed')

def button2_function():
    print('hello')

# create a window
window = tk.Tk()
window.title('Window and Widgets')
window.geometry('800x500')

# create widgets
text = tk.Text(master = window)
text.pack()

# ttk widgets
label = ttk.Label(master = window, text = 'This is a test')
label.pack()

# ttk entry
entry = ttk.Entry(master = window)
entry.pack()

# exercise
label2 = ttk.Label(master = window, text = "my label")
label2.pack()

# ttk button
button = ttk.Button(master = window, text = 'A button', command = button_function)
button.pack()

# exercise
# add one more text label and a button that prints 'hello'
# the label should say "my label" and be between the entry widget and the button
button2 = ttk.Button(master = window, text = "Hello Button", command = button2_function)
button2.pack()

# run
window.mainloop()