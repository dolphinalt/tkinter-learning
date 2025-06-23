import tkinter as tk
from tkinter import ttk

def button_func():
    print(string_var.get())
    string_var.set('button pressed')

# window
window = tk.Tk()
window.title('Tkinter Variables')

# tkinter variable
string_var = tk.StringVar(value = 'start value')
exercise_string_var = tk.StringVar(value = 'test')

# widgets
label = ttk.Label(master = window, text = 'label', textvariable = string_var)
label.pack()
entry = ttk.Entry(master = window, textvariable = string_var)
entry.pack()
button = ttk.Button(master = window, text = 'button', command = button_func)
button.pack()

# exercise
# create 2 entry fields and 1 labels, they should all be connected via a StringVar
# set a start value of 'test
exercise_entry1 = ttk.Entry(master = window, textvariable = exercise_string_var)
exercise_entry1.pack()
exercise_entry2 = ttk.Entry(master = window, textvariable = exercise_string_var)
exercise_entry2.pack()
exercise_label = ttk.Label(master = window, textvariable = exercise_string_var)
exercise_label.pack()

# run
window.mainloop()