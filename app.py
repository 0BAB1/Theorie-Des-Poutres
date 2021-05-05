import tkinter as tk

class Application(tk.Tk):
    """main app, initialise and lunch mainloop to start"""

    def __init__(self):
        tk.Tk.__init__(self)
        #radiobutton type variable
        self.type_flexion = tk.StringVar()
        self.type_section = tk.StringVar()
        #initialize windows bases
        self.geometry("640x480")
        self.make_widgets()

    def make_widgets(self):
        """Create All Widget On The Front Page"""
        #flexion label
        self.hello = tk.Label(text="type de flexion ?")

        #radio buttons in order to select which flexion mode we're in
        ##single embedding link
        self.type_flexion1 = tk.Radiobutton(text = "force en bout", value="1", variable=self.type_flexion, command= lambda : self.activate_flexion(1))
        self.type_flexion2 = tk.Radiobutton(text = "force repartie", value="2", variable=self.type_flexion, command= lambda : self.activate_flexion(2))
        ##double embedding link
        self.type_flexion21 = tk.Radiobutton(text = "moment point d'appui", value="21", variable=self.type_flexion, command= lambda : self.activate_flexion(21))
        self.type_flexion22 = tk.Radiobutton(text = "force x=a", value="22", variable=self.type_flexion, command= lambda : self.activate_flexion(22))
        self.type_flexion23 = tk.Radiobutton(text = "force x= L/2", value="23", variable=self.type_flexion, command= lambda : self.activate_flexion(23))
        ##the command on the radio button wil activate certain entries (specified with nubers indexation)

        #radio buttons to determinate polar section I
        ##square
        self.type_section_square = tk.Radiobutton()
        ##empty square
        self.type_section_square = tk.Radiobutton()
        ##circle
        self.type_section_square = tk.Radiobutton()
        ##empty_cicle
        self.type_section_square = tk.Radiobutton()

        #entries for different flexion cases

        #entries for differents section cases

        #frames for each case, where we pack all entries

        #pack all
        self.hello.pack()
        self.type_flexion1.pack()
        self.type_flexion2.pack()
        self.type_flexion21.pack()
        self.type_flexion22.pack()
        self.type_flexion23.pack()
    
    def get_entry(self, button):
        """get entry of a specified button"""
        e = button.get()
        print(e)

    def activate_flexion(self, type):
        pass
