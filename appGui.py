#                     __                      ______              
# .-----.-----.--.--.|  |--.-----.----.-----.|      |.-----.-----.
# |  _  |__ --|  |  ||  _  |  _  |   _|  _  ||  --  ||     |  -__|
# |   __|_____|___  ||_____|_____|__| |___  ||______||__|__|_____|#4689
# |__|        |_____|                 |_____| appGui.py
# 
# Licensed under the terms of the LICENSE file included in this repo.
# Created On   : We, September 6th 2023, 10:39:35
# Last Modified: Th, September 7th 2023, 01:59:47

import tkinter as tk
from tkinter import ttk
from gui import Application
from app import *

if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)

    ############################# Widgets #############################
    # Frames
    titleFrame      = ttk.Frame(root)
    setupFrame      = ttk.Frame(root)
    connFrame       = ttk.Labelframe(setupFrame, text='Connection String')
    userFrame       = ttk.Labelframe(setupFrame, text= "Username")
    passFrame       = ttk.Labelframe(setupFrame, text= "Password")
    buttonFrame     = ttk.Frame(root)
    progressFrame   = ttk.Frame(root)

    # Labels
    lbl_title       = ttk.Label(titleFrame, text="Connection Mage", style = "title.TLabel")

    # Entries
    in_connection   = ttk.Entry(connFrame)
    in_username     = ttk.Entry(userFrame)
    in_password     = ttk.Entry(passFrame)
    
    # Buttons
    btn_start       = ttk.Button(buttonFrame, text="Start", style = "green.TButton")
    btn_restore     = ttk.Button(buttonFrame, text="Restore", style = "blue.TButton", command=restoreBackup)
    btn_quit        = ttk.Button(buttonFrame, text="Quit", style = "red.TButton", command=root.destroy)   
    
    # Other
    wx_seperator    = ttk.Separator(progressFrame, orient='horizontal')
    bar_operation   = ttk.Progressbar(progressFrame, mode='indeterminate')
    ############################# !Widgets #############################

    ############################# Packing #############################
    # Labels
    lbl_title.pack()

    # Entries
    in_connection.pack(fill='both', expand=True, padx=10)
    in_username.pack(side='left', padx=10)
    in_password.pack(side='left', padx=10)

    # Buttons
    btn_restore.pack(side='left', padx=10, pady=10)
    btn_start.pack(side='left', padx=10, pady=10)
    btn_quit.pack(side='left', padx=10, pady=10)

    # Other
    wx_seperator.pack(fill='x', pady=10)
    bar_operation.pack(fill='x', padx=10)

    # Frames - Swap them around to change the layout
    titleFrame.pack(fill='both')
    connFrame.pack(fill='both', expand=True, padx=10)
    userFrame.pack(side='left', expand=True, pady=10)
    passFrame.pack(side='left', expand=True, pady=10)
    setupFrame.pack(fill='both')
    buttonFrame.pack()
    progressFrame.pack(fill='x')
    ############################# !Packing #############################

    ######################### Button Callbacks #########################
    def startOperation():
        print(in_connection.get())
        print(in_username)
        print(in_password)

    
    btn_start['command'] = lambda:startOperation()
        
    ######################## !Button Callbacks #########################

    root.mainloop()