import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

# window
window = tk.Tk()
window.title('Sliders')

# slider
scale_float = tk.DoubleVar(value = 15)
scale = ttk.Scale(window, command = lambda value: progress.stop(), from_ = 0, to = 25, length = 300, orient = 'vertical', variable = scale_float)
scale.pack()

# progress bar
progress = ttk.Progressbar(window, variable = scale_float, maximum = 25, orient = 'horizontal', mode = 'indeterminate', length = 400)
progress.pack()

# progress.start(1000)

# Scrolledtext
scrolled_text = scrolledtext.ScrolledText(window, width = 100, height = 5)
scrolled_text.pack()

# exercise
# create a progress that is vertical, starts automatically and also show the progress as a number
# there should also be a scale slider that is affected by the progress bar
exercise_frame = ttk.Frame(master = window)
exercise_int = tk.IntVar()
exercise_scale = ttk.Scale(exercise_frame, variable = exercise_int, from_ = 0, to = 100, orient = 'vertical', length = 100)
exercise_scale.pack(side = 'left')
exercise_progress = ttk.Progressbar(exercise_frame, variable = exercise_int, maximum = 100, orient = 'vertical', length = 100)
exercise_progress.pack(side = 'left', padx = 10)
exercise_label = ttk.Label(exercise_frame, textvariable = exercise_int)
exercise_label.pack(side = 'left', padx = 10)
exercise_frame.pack(pady = 10)

exercise_progress.start()

# run
window.mainloop()