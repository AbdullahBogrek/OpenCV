import tkinter as tk
import tkinter.ttk as ttk

from widgets.base import Base

class Application():
    def __init__(self, master):
        base = Base(master)
        base.pack(expand=True, fill='both')

        master.mainloop()

if __name__ == '__main__':
    window = tk.Tk()
    window.geometry("800x600")
    window.title("PhotoCV")
    app = Application(window) 