import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('More on the window')
# window.geometry('600x400+100+200')

# exercise:
# start window in the middle of the screen
xdim = 1400
ydim = 600
windowx = window.winfo_screenwidth()
windowy = window.winfo_screenheight()
left = windowx/2 - xdim/2
top = windowy/2 - ydim/2
window.geometry(f'{xdim}x{ydim}+{int(left)}+{int(top)}')
window.iconbitmap('assets/icon.ico')

# window sizes
window.minsize(200, 100)
# window.maxsize(800, 700)
# window.resizable(True, False)

# screen attributes
print(window.winfo_screenwidth())
print(window.winfo_screenheight())

# window attributes
window.attributes('-alpha', 1)
# window.attributes('-topmost', True)

# security event
window.bind('<Escape>', lambda event: window.quit())

# window.attributes('-disable', True)
# window.attributes('-fullscreen', True)

# title bar
window.overrideredirect(True)
grip = ttk.Sizegrip(window)
grip.place(relx = 1.0, rely = 1.0, anchor = 'se')

# run
window.mainloop()