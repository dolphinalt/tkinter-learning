import customtkinter as ctk
from ctypes import windll, byref, sizeof, c_int

try: from ctypes import windll, byref, sizeof, c_int
except: from ctypes import byref, sizeof, c_int


app = ctk.CTk(fg_color = '#FF00FF')
app.geometry('300x200')

try:
    # change the title bar color
    HWND = windll.user32.GetParent(app.winfo_id())
    title_bar_color = 0x00FF00FF
    windll.dwmapi.DwmSetWindowAttribute(HWND, 35, byref(c_int(title_bar_color)), sizeof(c_int))

    HWND = windll.user32.GetParent(app.winfo_id())
    title_text_color = 0x00FF0099
    windll.dwmapi.DwmSetWindowAttribute(HWND, 36, byref(c_int(title_text_color)), sizeof(c_int))
except:
    pass

# run
app.mainloop()