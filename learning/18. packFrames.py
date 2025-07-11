import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Pack parenting')
window.geometry('400x600')

# Top frame
top_frame = ttk.Frame(window)
label1 = ttk.Label(top_frame, text = 'First label', background = 'red')
label2 = ttk.Label(top_frame, text = 'Label2', background = 'blue')

# middle widget
label3 = ttk.Label(window, text = 'Another label', background = 'green')

# bottom frame
bottom_frame = ttk.Frame(window)
label4 = ttk.Label(bottom_frame, text = 'Last of the labels', background = 'orange')
button = ttk.Button(bottom_frame, text = 'A Button')
button2 = ttk.Button(bottom_frame, text = 'Another button')

# exercise frame
exercise_frame = ttk.Frame(bottom_frame)
exercise_button1 = ttk.Button(exercise_frame, text = 'Button 3')
exercise_button2 = ttk.Button(exercise_frame, text = 'Button 4')
exercise_button3 = ttk.Button(exercise_frame, text = 'Button 5')

# top layout
label1.pack(side = 'left', fill = 'both', expand = True)
label2.pack(side = 'left', fill = 'both', expand = True)
top_frame.pack(fill = 'both', expand = True)

# middle layout
label3.pack(expand = True)

# bottom layout
button.pack(side = 'left', expand = True, fill = 'both')
label4.pack(side = 'left', expand = True, fill = 'both')
button2.pack(side = 'left', expand = True, fill = 'both')
bottom_frame.pack(expand = True, fill = 'both', padx = 20, pady = 20)

# exercise
# create 3 more buttons and another frame
# the frame shoudl be on the right inside of the bottom frame
# and teh buttons should be stacked vertically inside of it

exercise_button1.pack(expand = True, fill = 'both')
exercise_button2.pack(expand = True, fill = 'both')
exercise_button3.pack(expand = True, fill = 'both')
exercise_frame.pack(side = 'left', fill = 'both', expand = True)

# run
window.mainloop()