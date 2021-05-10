import tkinter as tk

class Frame1(tk.Frame):
    """Class frame, creating a frame with all entry and buttons for simple force flexion"""
    def __init__(self, master):

        #call the tk.Frame init, markin the master, specified when class called in app.py
        super().__init__(master, width=220, height=460)

        #result
        self.result_label = tk.Label(self)

        #igz
        self.igz_label = tk.Label(self, text="igz (en mm^4) : ")
        self.igz = tk.Entry(self)
        #Lenght
        self.l_label = tk.Label(self, text="L (en mm)")
        self.l = tk.Entry(self)
        #actual force
        self.f_label = tk.Label(self, text="F (en Newtons)")
        self.f = tk.Entry(self)

        #button
        self.enter = tk.Button(self, text="valider", height=1, width=20, command=self.proceed)

        #grid igz
        self.igz_label.grid(row=0,column=0)
        self.igz.grid(row=0,column=1)

        #grid L
        self.l_label.grid(row=1,column=0)
        self.l.grid(row=1,column=1)

        #grid force
        self.f_label.grid(row=2,column=0)
        self.f.grid(row=2,column=1)

        #grid button
        self.enter.grid(row=3)

        #image and grid
        self.file = tk.PhotoImage(file="assets/1.png")
        self.img = tk.Label(self, image=self.file)
        self.img.grid(row=4)
    
    def proceed(self):
        f = int(self.f.get())
        l = int(self.l.get())
        i = int(self.igz.get())
        e = 210000
        yMax = (f*l^3)/(3*e*i)

        self.result_label['text'] = yMax
        self.result_label.grid()

class Frame2(tk.Frame):
    """this frame is force evenly placed force"""
    def __init__(self, master):
        #call the tk.Frame init, markin the master, specified when class called in app.py
        super().__init__(master, width=220, height=460)

        #result
        self.result_label = tk.Label(self)

        #igz
        self.igz_label = tk.Label(self, text="igz (en mm^4) : ")
        self.igz = tk.Entry(self)
        #Lenght
        self.l_label = tk.Label(self, text="L (en mm)")
        self.l = tk.Entry(self)
        #actual force
        self.w_label = tk.Label(self, text="W (en N/mm)")
        self.w = tk.Entry(self)

        #button
        self.enter = tk.Button(self, text="valider", height=1, width=20)

        #grid igz
        self.igz_label.grid(row=0,column=0)
        self.igz.grid(row=0,column=1)

        #grid L
        self.l_label.grid(row=1,column=0)
        self.l.grid(row=1,column=1)

        #grid force
        self.w_label.grid(row=2,column=0)
        self.w.grid(row=2,column=1)

        #grid button
        self.enter.grid(row=3)

        #image and grid
        self.file = tk.PhotoImage(file="assets/2.png")
        self.img = tk.Label(self, image=self.file)
        self.img.grid(row=4)

class Frame21(tk.Frame):
    """this frame is force evenly placed force"""
    def __init__(self, master):
        #call the tk.Frame init, markin the master, specified when class called in app.py
        super().__init__(master, width=220, height=460)

        #result
        self.result_label = tk.Label(self)

        #igz
        self.igz_label = tk.Label(self, text="igz (en mm^4) : ")
        self.igz = tk.Entry(self)
        #Lenght
        self.l_label = tk.Label(self, text="L (en mm)")
        self.l = tk.Entry(self)
        #actual force
        self.mo_label = tk.Label(self, text="Moment (en N.mm)")
        self.mo = tk.Entry(self)

        #button
        self.enter = tk.Button(self, text="valider", height=1, width=20)

        #grid igz
        self.igz_label.grid(row=0,column=0)
        self.igz.grid(row=0,column=1)

        #grid L
        self.l_label.grid(row=1,column=0)
        self.l.grid(row=1,column=1)

        #grid force
        self.mo_label.grid(row=2,column=0)
        self.mo.grid(row=2,column=1)

        #grid button
        self.enter.grid(row=3)

        #image and grid
        self.file = tk.PhotoImage(file="assets/21.png")
        self.img = tk.Label(self, image=self.file)
        self.img.grid(row=4)

class Frame22(tk.Frame):
    """this frame is force evenly placed force"""
    def __init__(self, master):
        #call the tk.Frame init, markin the master, specified when class called in app.py
        super().__init__(master, width=220, height=460)

        #result
        self.result_label = tk.Label(self)

        #igz
        self.igz_label = tk.Label(self, text="igz (en mm^4) : ")
        self.igz = tk.Entry(self)
        #Lenght
        self.l_label = tk.Label(self, text="L (en mm)")
        self.l = tk.Entry(self)
        #a
        self.a_label = tk.Label(self, text="a (en mm")
        self.a = tk.Entry(self)
        #p
        self.p_label = tk.Label(self, text="P (en Newtons)")
        self.p = tk.Entry(self)
        #button
        self.enter = tk.Button(self, text="valider", height=1, width=20)

        #grid igz
        self.igz_label.grid(row=0,column=0)
        self.igz.grid(row=0,column=1)

        #grid L
        self.l_label.grid(row=1,column=0)
        self.l.grid(row=1,column=1)

        #grid a
        self.a_label.grid(row=2,column=0)
        self.a.grid(row=2,column=1)

        #grid p
        self.p_label.grid(row=3, column=0)
        self.p.grid(row=3, column=1)

        #grid button
        self.enter.grid(row=4)

        #image and grid
        self.file = tk.PhotoImage(file="assets/22.png")
        self.img = tk.Label(self, image=self.file)
        self.img.grid(row=5)

class Frame23(tk.Frame):
    """this frame is force evenly placed force"""
    def __init__(self, master):
        #call the tk.Frame init, markin the master, specified when class called in app.py
        super().__init__(master, width=220, height=460)

        #result
        self.result_label = tk.Label(self)

        #igz
        self.igz_label = tk.Label(self, text="igz (en mm^4) : ")
        self.igz = tk.Entry(self)
        #Lenght
        self.l_label = tk.Label(self, text="L (en mm)")
        self.l = tk.Entry(self)
        #actual force
        self.p_label = tk.Label(self, text="P (en Newtons)")
        self.p = tk.Entry(self)

        #button
        self.enter = tk.Button(self, text="valider", height=1, width=20)

        #grid igz
        self.igz_label.grid(row=0,column=0)
        self.igz.grid(row=0,column=1)

        #grid L
        self.l_label.grid(row=1,column=0)
        self.l.grid(row=1,column=1)

        #grid force
        self.p_label.grid(row=2,column=0)
        self.p.grid(row=2,column=1)

        #grid button
        self.enter.grid(row=3)

        #image and grid
        self.file = tk.PhotoImage(file="assets/23.png")
        self.img = tk.Label(self, image=self.file)
        self.img.grid(row=4)