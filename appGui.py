import tkinter as tk
from gui import Application

if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)

    

    def startBackupOperation():
        # Take the values from fields and send to app
        
        pass

    def startRestoreOperation():
        # Only enable if web.config.back is present
        # MOVE the backup in place of the original
        pass

    


    root.mainloop()