from tkinter import *

window = Tk()



def clear_view(window):
    for el in window.grid_slaves():
        el.destroy()


def render_list_tasks_view(window):
    clear_view(window)
    window.title("List tasks")
    window.geometry("300x400")

    # Back button
    btn_1 = Button(window, text="Back", command=lambda: render_main_view(window))
    btn_1.grid(row=0, column=0, padx=20, pady=20)
    pass


def render_create_task_view(window):
    pass


def render_main_view(window):
    window.title("ToDo App")
    window.geometry("350x80")

    # button 1 - List tasks
    btn_1 = Button(window, text="List tasks", bg='blue', fg='yellow', command=lambda: render_list_tasks_view(window))
    btn_1.grid(row=0, column=0, padx=20, pady=20)

    # button2 - Create a task
    btn_2 = Button(window, text="Create task", bg='green', fg='white', command=lambda: render_create_task_view(window))
    btn_2.grid(row=0, column=1, padx=20, pady=20)


render_main_view(window)
window.mainloop()
