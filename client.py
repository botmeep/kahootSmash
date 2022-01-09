"""
  _         _                 _    _____                     _     
 | |       | |               | |  / ____|                   | |    
 | | ____ _| |__   ___   ___ | |_| (___  _ __ ___   __ _ ___| |__  
 | |/ / _` | '_ \ / _ \ / _ \| __|\___ \| '_ ` _ \ / _` / __| '_ \ 
 |   < (_| | | | | (_) | (_) | |_ ____) | | | | | | (_| \__ \ | | |
 |_|\_\__,_|_| |_|\___/ \___/ \__|_____/|_| |_| |_|\__,_|___/_| |_|

Created by Meep

"""

from kahootSmasher import Smasher
import tkinter as tk
import threading, ctypes
from rpc import RPC

ctypes.windll.kernel32.SetConsoleTitleA("kahootSmasher")

class client:
    def __init__(self):
        self.window = tk.Tk()
        self.counter = 5
        self.rpc = RPC()
        self.rpc.start()

    def increase(self):
        self.counter += 1
        self.counterString.set(self.counter)

    def decrease(self):
        if self.counter == 0:
            return

        self.counter -= 1
        self.counterString.set(self.counter)

    def createBots(self):
        if self.counter <= 0:
            return
        self.rpc.updatePin(self.pin.get())
        
        self.smash = Smasher(int(self.pin.get()), rpc=self.rpc) #Pass RPC instance for bot count updating
        for x in range(self.counter):
            t = threading.Thread(target=self.smash.createBot)
            t.start()
            print(f'Started thread {x+1} of {self.counter}')

    def killBots(self):
        self.rpc.clear()
        self.smash.running = False

    def render(self):
        self.window.title("kahootSmash")
        left = tk.Frame(master=self.window, height=100, width=200, bg="orange")
        right= tk.Frame(master=self.window, width=100, bg="purple")
        left.pack_propagate(0)

        self.pin = tk.Entry(master=left)
        self.pin.pack(pady=12)
        start = tk.Button(master=left, text="Flood Kahoot", command=self.createBots).pack()
        stop = tk.Button(master=left, text="Kill Bots", command=self.killBots).pack()

        decrease = tk.Button(master=right, text="-", width=5, command=self.decrease).pack(side=tk.LEFT)
        self.counterString = tk.StringVar()
        self.counterString.set(5)
        counterLabel = tk.Label(master=right, textvariable=self.counterString, width=5).pack(side=tk.LEFT)
        
        increase = tk.Button(master=right, text="+", width=5, command=self.increase).pack(side=tk.LEFT)

        left.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        right.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        self.window.mainloop()


if __name__ == "__main__":
    client().render()