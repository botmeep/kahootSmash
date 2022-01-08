import kahootSmasher
import tkinter as tk

class client:
    def __init__(self):
        self.window = tk.Tk()
    def create(self):
        m = tk.Entry(width=7)
        b = tk.Button(text="Flood Kahoot", width=10, height=1).pack()
        m.pack()
        self.window.mainloop()


if __name__ == "__main__":
    client().create()