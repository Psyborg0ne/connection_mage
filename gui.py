import tkinter as tk
from tkinter import ttk

class Application(ttk.Frame):
    def __init__(self, root, *args, **kwargs):
        ttk.Frame.__init__(self, root, *args, **kwargs)

        # Init
        root.title("Connection Mage")
        root.iconbitmap('./app.ico')
        root.minsize(400, 600)
        root.geometry("400x600+100+100")

        #----------------------------------------------------------------------
        # Style

        style = ttk.Style()
        style.theme_use("default")

        # Button Styles
        style.configure("TButton", font=("Helvetica", 16), foreground="white", padding=[10,10,10,10])

        style.configure('red.TButton', background="#e60000")
        style.map("red.TButton", background= [('active', '#ff1a1a')])
        
        style.configure('green.TButton', background="#00bb00")
        style.map("green.TButton", background= [('active', '#00ff00')])
        
        style.configure('blue.TButton', background="#66d9ff")
        style.map("blue.TButton", background= [('active', '#99e6ff')])

        # Label Styles
        style.configure("TLabel", font=("Helvetica", 16), foreground="black", padding=[10,10,10,10])
        style.configure("title.TLabel", fontsize=32)
        
        # Style End
        #----------------------------------------------------------------------

        # Frames
        titleFrame = ttk.Frame(self).pack(fill="both", expand=True)
        setupFrame = ttk.Frame(self).pack(fill="both", expand=True)
        buttonFrame = ttk.Frame(self).pack(fill="both", expand=True)
        logFrame = ttk.Frame(self).pack(fill="both", expand=True)

        # Labels
        ttk.Label(titleFrame, text="Connection Mage", style = "title.TLabel").pack(fill='both')



        # Buttons
        mybutton = ttk.Button(buttonFrame, text="Start", style = "green.TButton").pack(side='left')
        myButton1 = ttk.Button(buttonFrame, text="Quit", style = "red.TButton").pack(side='left')
        mybutton2 = ttk.Button(buttonFrame, text="Restore", style = "blue.TButton").pack(side='left')

        self.pack(fill="both", expand = True)
    

