import tkinter as tk

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
        self.left_frame.grid(row=0, column=0, padx=10, pady=5)

        #create differetn interfaces for each flexion cases, and grid it into a frame
        self.frame1 = tk.Frame(self.left_frame, width=220, height=460)
        #igz
        self.igz_label1 = tk.Label(self.frame1, text="igz")
        self.igz1 = tk.Entry(self.frame1)
        #Lenght
        self.l_label1 = tk.Label(self.frame1, text="L")
        self.l1 = tk.Entry(self.frame1)
        #actual force
        self.f_label1 = tk.Label(self.frame1, text="F")
        self.f1 = tk.Entry(self.frame1)

        self.igz_label1.grid(row=0,column=0)
        self.igz1.grid(row=0,column=1)
        self.l_label1.grid(row=1,column=0)
        self.l1.grid(row=1,column=1)
        self.f_label1.grid(row=2,column=0)
        self.f1.grid(row=2,column=1)

        self.frame1.grid()
    
    def get_entry(self, ent):
        """get entry of a specified button"""
        e = ent.get()
        print(e)

    def activate_flexion(self, type):
        pass
