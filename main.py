from tkinter import *
from database import Database
from new_sys import NewPage

window = Tk()
window.title("Employment Management System")
window.minsize(200, 200)
window.config(padx=50, pady=50)

def A():
    return NewPage()

logo_label = Label(window, text="EMS", font=("Helvetica", 46))
logo_label.grid(column=1, row=0, columnspan=2, pady=10)

intro_label = Label(window, text="Employment Management System with Access to Database...")
intro_label.grid(column=1, row=0, columnspan=2, pady=5)

new_btn = Button(window, text="NEW SYSTEM", command=A)
new_btn.grid(column=0, row=2, pady=10)

old_btn = Button(window, text="EXISTING SYSTEM", command='')
old_btn.grid(column=3, row=2, pady=10)

exit_btn = Button(window, text='EXIT', command=window.quit)
exit_btn.grid(column=1, row=2, columnspan=2, pady=10)

window.mainloop()


