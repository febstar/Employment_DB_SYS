from tkinter import *

class NewPage:
    def __init__(self):
        self.window = Tk()
        self.window.title("NEW DATABASE")
        self.window.minsize(500, 500)
        self.window.config(padx=50, pady=50)
        self.label = Label(self.window, text="New DB System", font=("Helvetica", 26)).grid(column=0, row=0, columnspan=2)
        self.info = {}
        self.Entry()
        
    def Entry(self):
        DB_label = Label(self.window, text="Enter DataBase Name:").grid(column=1, row=1)
        DB_name = Entry(self.window).grid(column=2, row=1)
        Table_label = Label(self.window, text="Enter Table Name:").grid(column=1, row=2)
        Table_name = Entry(self.window).grid(column=2, row=2)
    