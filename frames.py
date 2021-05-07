import tkinter as tk

class Frame1(tk.Frame):
    """Class frame, creating a frame with all entry and buttons for simple force flexion"""
    def __init__(self, master):

        #call the tk.Frame init, markin the master, specified when class called in app.py
        super().__init__(master, width=220, height=460)

        #array containing entries, and creating the frame to pack everithing in
        entries = []

        #igz
        self.igz_label = tk.Label(self, text="igz")
        self.igz = tk.Entry(self)
        #Lenght
        self.l_label = tk.Label(self, text="L")
        self.l = tk.Entry(self)
        #actual force
        self.f_label = tk.Label(self, text="F")
        self.f = tk.Entry(self)

        #grid igz
        self.igz_label.grid(row=0,column=0)
        self.igz.grid(row=0,column=1)
        entries.append(self.igz)

        #grid L
        self.l_label.grid(row=1,column=0)
        self.l.grid(row=1,column=1)
        entries.append(self.l)

        #grid force
        self.f_label.grid(row=2,column=0)
        self.f.grid(row=2,column=1)
        entries.append(self.f)

        #button and grid
        self.enter = tk.Button(self, text="valider", height=1, width=20)
        self.enter.grid()