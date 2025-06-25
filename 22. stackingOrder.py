import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Stacking Order')
window.geometry('400x400')

# widgets
label1 = ttk.Label(window, text = 'Label 1', background = 'green')
label2 = ttk.Label(window, text = 'Label 2', background = 'red')

# label1.lift()
# label2.lower()

button1 = ttk.Button(window, text = 'raise label 1', command = lambda: label1.tkraise(aboveThis = label2))
button2 = ttk.Button(window, text = 'raise label 2', command = lambda: label2.tkraise())

# layout
label1.place(x = 50, y = 100, width = 200, height = 150)
label2.place(x = 150, y = 60, width = 140, height = 100)

button1.place(rely= 1, relx = 0.8, anchor = 'se')
button2.place(rely= 1, relx = 1, anchor = 'se')

# exercise
# add a third label and button
label3 = ttk.Label(window, text = 'Label 3', background = 'blue')
button3 = ttk.Button(window, text = 'raise label 3', command = lambda: label3.tkraise())
label3.place(x = 20, y = 80, width = 180, height = 100)
button3.place(rely= 1, relx = 0.6, anchor = 'se')

# run
window.mainloop()