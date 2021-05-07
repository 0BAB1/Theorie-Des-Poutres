import tkinter as tk
from frames import *

class Application(tk.Tk):
    """main app, initialise and lunch mainloop to start"""

    def __init__(self):
        tk.Tk.__init__(self)
        #initialize windows bases
        self.geometry("720x480")
        self.make_widgets()
        self.config(menu=self.menuBar, bg="skyblue")

    def make_widgets(self):
        """Create All Widget On The Front Page"""
        #creating menu
        self.menuBar = tk.Menu()

        #menus to select which flexion
        flexionMenu = tk.Menu(self.menuBar, tearoff=0)
        flexionMenu.add_command(label="force en bout")
        flexionMenu.add_command(label="force repartie")
        flexionMenu.add_separator()
        flexionMenu.add_command(label="moment, double appui")
        flexionMenu.add_command(label="force x=a")
        flexionMenu.add_command(label="force x=L/2")
        self.menuBar.add_cascade(label="flexion", menu=flexionMenu)

        #menus to select which section
        sectionMenu = tk.Menu(self.menuBar, tearoff=0)
        sectionMenu.add_command(label="rectangulaire")
        sectionMenu.add_command(label="rectangulaire creuse")
        sectionMenu.add_command(label="circulaire")
        sectionMenu.add_command(label="circulaire creuse")
        self.menuBar.add_cascade(label="section", menu=sectionMenu)

        #create the left frame
        self.left_frame = tk.Frame(self, width=240, height=480)
        self.left_frame.grid(row=0, column=0, padx=10, pady=5, sticky="NESW")

        #create differetn interfaces for each flexion cases, and grid it into a frame
        frame1 = Frame1(self.left_frame)
        frame1.grid()

    def activate_flexion(self, type):
        pass
