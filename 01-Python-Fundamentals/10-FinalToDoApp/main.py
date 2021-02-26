from tkinter import *

tk = Tk()
tk.geometry("1000x400")


def render_main_view():
    Button(tk, text="List Tasks", bg="blue", fg="white").grid(row=0, column=0, padx=200, pady=200)
    Button(tk, text="Create Tasks", bg="green", fg="white", command=render_create_task_view).grid(row=0, column=1, padx=10, pady=30)


render_main_view()
tk.mainloop()
