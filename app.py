import tkinter as tk
from frames import *

class Application(tk.Tk):
    """main app, initialise and lunch mainloop to start"""

    def __init__(self):
        tk.Tk.__init__(self)
        #create a convenient array to store frames
        self.frames = []
        #initialize windows bases
        self.geometry("720x480")
        self.make_widgets()
        self.config(menu=self.menuBar, bg="skyblue")
        self.resizable(False, False)

    def make_widgets(self):
        """Create All Widget On The Front Page"""
        #creating menu
        self.menuBar = tk.Menu()

        #menus to select which flexion
        flexionMenu = tk.Menu(self.menuBar, tearoff=0)
        flexionMenu.add_command(label="force en bout", command = lambda : self.activate_flexion(0))
        flexionMenu.add_command(label="force repartie", command = lambda : self.activate_flexion(1))
        flexionMenu.add_separator()
        flexionMenu.add_command(label="moment, double appui", command = lambda : self.activate_flexion(2))
        flexionMenu.add_command(label="force x=a", command = lambda : self.activate_flexion(3))
        flexionMenu.add_command(label="force x=L/2", command = lambda : self.activate_flexion(4))
        self.menuBar.add_cascade(label="flexion", menu=flexionMenu)

        #menus to select which section
        sectionMenu = tk.Menu(self.menuBar, tearoff=0)
        sectionMenu.add_command(label="rectangulaire")
        sectionMenu.add_command(label="rectangulaire creuse")
        sectionMenu.add_command(label="circulaire")
        sectionMenu.add_command(label="circulaire creuse")
        self.menuBar.add_cascade(label="section", menu=sectionMenu)

        #create the left frame
        self.left_frame = tk.Frame(self)
        self.left_frame.grid(row=0, column=0)

        #create differetn interfaces for each flexion cases, and add it to our frames array, ready to grid
        frame1 = Frame1(self.left_frame)
        self.frames.append(frame1)
        
        frame2 = Frame2(self.left_frame)
        self.frames.append(frame2)

        frame21 = Frame21(self.left_frame)
        self.frames.append(frame21)

        frame22 = Frame22(self.left_frame)
        self.frames.append(frame22)

        frame23 = Frame23(self.left_frame)
        self.frames.append(frame23)

    def activate_flexion(self, i):
        for frame in self.frames:
            frame.grid_forget()
        
        self.frames[i].grid()
