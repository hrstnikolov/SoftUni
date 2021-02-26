from tkinter import *

window = Tk()
window.title("ToDo App")
window.geometry("400x400")
btn_1 = Button(window, text="List tasks", bg='blue', fg='yellow')
btn_1.grid(row=0, column=0, padx=20, pady=20)

window.mainloop()
