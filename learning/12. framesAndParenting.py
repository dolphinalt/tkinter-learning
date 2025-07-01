import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.geometry('600x400')
window.title('frames and parenting')

# frame
frame = ttk.Frame(window, width = 200, height = 200, borderwidth = 10, relief = tk.GROOVE)
frame.pack_propagate(False)
frame.pack(side = 'left')

# master setting
label = ttk.Label(frame, text = 'Label in frame')
label.pack()

button = ttk.Button(frame, text = 'Button in a frame')
button.pack()

# example
label2 = ttk.Label(window, text = 'Label outside frame')
label2.pack(side = 'left')

# exercise
# create anopther frame with a label, a button and an entry and place it to the right
# of the other widgets
exercise_frame = ttk.Frame()
exercise_label = ttk.Label(exercise_frame, text = "exercise label")
exercise_label.pack()
exercise_button = ttk.Button(exercise_frame, text = "exercise button")
exercise_button.pack()
exercise_entry = ttk.Entry(exercise_frame)
exercise_entry.pack()
exercise_frame.pack(side = 'left')

# run
window.mainloop()