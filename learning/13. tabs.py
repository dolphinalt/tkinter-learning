import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.geometry('600x400')
window.title('Tab Widget')

# Notebook widget
notebook = ttk.Notebook(window)

# tab 1
tab1 = ttk.Frame(notebook)
label1 = ttk.Label(tab1, text = "Text in tab 1")
label1.pack()
button1 = ttk.Button(tab1, text = 'Button in tab 1')
button1.pack()

# tab 2
tab2 = ttk.Frame(notebook)
label2 = ttk.Label(tab2, text = 'Text in tab 2')
label2.pack()
entry2 = ttk.Entry(tab2)
# entry2.pack()

# notebook.add(tab1, text = 'Tab 1')
# notebook.add(tab2, text = 'Tab 2')
# notebook.pack()

# exercise
# add another tab with 2 buttons and one label inside
tab3 = ttk.Frame(notebook)
tab3_label = ttk.Label(tab3, text = "Tab 3")
tab3_label.pack()
tab3_button1 = ttk.Button(tab3, text = "button1")
tab3_button1.pack()
tab3_button2 = ttk.Button(tab3, text = "button2")
tab3_button2.pack()

notebook.add(tab1, text = 'Tab 1')
notebook.add(tab2, text = 'Tab 2')
notebook.add(tab3, text = 'Tab 3')
notebook.pack()

# run
window.mainloop()