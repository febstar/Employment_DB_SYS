from tkinter import *
from tkinter.tix import ComboBox
from tkinter.ttk import Combobox
from database import Database

class NewPage:
    def __init__(self):
        self.window = Tk()
        self.window.title("NEW DATABASE")
        self.window.minsize(500, 500)
        self.window.config(padx=50, pady=50)
        self.label = Label(self.window, text="New DB System", font=("Helvetica", 26)).grid(column=0, row=0, columnspan=2)
        self.info = {}
        self.send_data = {}
        self.cols = []
        self.d_type = []
        self.Entry()
        
        
    def Entry(self):
        DB_label = Label(self.window, text="Enter DataBase Name:").grid(column=1, row=1)
        self.DB_name = Entry(self.window)
        self.DB_name.grid(column=2, row=1)
        Table_label = Label(self.window, text="Enter Table Name:").grid(column=1, row=2)
        self.Table_name = Entry(self.window)
        self.Table_name.grid(column=2, row=2)
        cols_name = Label(self.window, text="Number of Columns:").grid(column=1, row=3)
        self.cols_option = Spinbox(self.window, from_=1 ,to=10)
        self.cols_option.grid(column=2, row=3)
        cols_confirm = Button(self.window, text="GO", command=self.DataCollect).grid(column=3, row=3)
        label_def = Label(self.window, text="Columns and Data Types").grid(column=0, row=4, columnspan=2)
        confirm = Button(self.window, text="SEND", command=self.ComData).grid(column=3, row=20)
        
    def DataCollect(self):
        self.info['DataBase'] = self.DB_name.get()
        self.info['Table'] = self.Table_name.get()
        self.info['Columns'] = self.cols_option.get()
        
        for i in range(int(self.info['Columns'])):
            new = Entry(self.window)
            self.cols.append(new)
            new.grid(column=1, row=5+i)
            l_new = Combobox(self.window, values=["INTEGER","TEXT"] )
            self.d_type.append(l_new)
            l_new.grid(column=2, row=5+i)
            
        
    def ComData(self):
        for i in range(len(self.cols)):
            self.send_data[self.cols[i].get()] = self.d_type[i].get()
        print(self.send_data)
        created = Database(self.info['DataBase'])
        created.create_table(self.info['Table'], self.send_data)
        
        
            