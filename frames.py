import tkinter as tk

class Frame1(tk.Frame):
    """Class frame, creating a frame with all entry and buttons for simple force flexion"""
    def __init__(self, master):

        #call the tk.Frame init, markin the master, specified when class called in app.py
        super().__init__(master, width=220, height=460)

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

        #grid L
        self.l_label.grid(row=1,column=0)
        self.l.grid(row=1,column=1)

        #grid force
        self.f_label.grid(row=2,column=0)
        self.f.grid(row=2,column=1)

        #button and grid
        self.enter = tk.Button(self, text="valider", height=1, width=20, command=self.proceed)
        self.enter.grid()
    
    def proceed(self):
        print("calcul")

class Frame2(tk.Frame):
    """this frame is force evenly placed force"""
    def __init__(self, master):
        #igz
        super().__init__(master, width=220, height=460)
        self.igz_label = tk.Label(self, text="igz2 omg ca a changé")
        self.igz = tk.Entry(self)

        #grid igz
        self.igz_label.grid(row=0,column=0)
        self.igz.grid(row=0,column=1)

#Create a class to simplify images creation
def make_label(master, path):
    """create an image as a label, require img path, returns the label itself"""
    img = tk.PhotoImage(path)
    return tk.Label(master, image=img)