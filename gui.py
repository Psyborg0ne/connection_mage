#                     __                      ______              
# .-----.-----.--.--.|  |--.-----.----.-----.|      |.-----.-----.
# |  _  |__ --|  |  ||  _  |  _  |   _|  _  ||  --  ||     |  -__|
# |   __|_____|___  ||_____|_____|__| |___  ||______||__|__|_____|#4689
# |__|        |_____|                 |_____| gui.py
# 
# Licensed under the terms of the LICENSE file included in this repo.
# Created On   : We, September 6th 2023, 10:39:35
# Last Modified: Th, September 7th 2023, 01:59:59

import tkinter as tk
from tkinter import ttk

class Application(ttk.Frame):
    def __init__(self, root, *args, **kwargs):
        ttk.Frame.__init__(self, root, *args, **kwargs)

        # Init
        root.title("Connection Mage")
        root.iconbitmap('./app.ico')
        root.minsize(400, 250)
        root.geometry("400x250+100+100")

        #----------------------------------------------------------------------
        # Style

        style = ttk.Style()
        style.theme_use("alt")

        # Button Styles
        style.configure("TButton", font=("Helvetica", 16), foreground="white")

        style.configure('red.TButton', background="#e60000")
        style.map("red.TButton", background= [('active', '#ff1a1a')])
        
        style.configure('green.TButton', background="#00bb00")
        style.map("green.TButton", background= [('active', '#00ff00')])
        
        style.configure('blue.TButton', background="#66d9ff")
        style.map("blue.TButton", background= [('active', '#99e6ff')])

        # Label Styles
        style.configure("TLabel", font=("Helvetica", 12), foreground="black", padx=10)
        style.configure("title.TLabel", font=("Helvetica", 32))

        # Entry Styles
        style.configure("TEntry", font=("Helvetica", 12), foreground="black")

        # Frame Styles
        style.configure("TLabelFrame", font=("Helvetica", 12), foreground="black")
        
        # Style End
        #----------------------------------------------------------------------
        
        self.pack()
    

