class Task:
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date
        self.comments = []
        self.completed = False

    def is_completed(self):
        return self.completed

    def change_name(self, new_name: str):
        if new_name == self.name:
            return "Name cannot be the same."
        self.name = new_name
        return self.name

    def change_due_date(self, new_date: str):
        if new_date == self.due_date:
            return "Date cannot be the same."
        self.due_date = new_date
        return self.due_date

    def add_comment(self, comment: str):
        self.comments.append(comment)

    def edit_comment(self, comment_number: int, new_comment: str):
        if comment_number < len(self.comments):
            self.comments[comment_number] = new_comment
            return ', '.join(self.comments)
        return "Cannot find comment."

    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def is_in_tasks(self, task):
        return task in self.tasks

    def get_task_by_name(self, task_name):
        for task in self.tasks:
            if task_name == task.first_name:
                return task

    def add_task(self, new_task):
        if self.is_in_tasks(new_task):
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        # return f"Task {new_task.name} is added to the section"
        return f"Task Name: {new_task.first_name} - Due Date: {new_task.due_date} is added to the section"

    def complete_task(self, task_name: str):
        task = self.get_task_by_name(task_name)
        if not self.is_in_tasks(task):
            return f"Could not find task with the name {task_name}"
        task.completed = True
        # index = self.tasks.index(task)
        # self.tasks[index].completed = True

    def clean_section(self):
        removed_tasks_count = 0
        for task in self.tasks:
            if task.is_completed():
                removed_tasks_count += 1
                self.tasks.remove(task)
        return f"Cleared {removed_tasks_count} tasks."

    def view_section(self):
        section_info = f"Section {self.name}:\n"
        tasks_info = '\n'.join([task.details() for task in self.tasks])
        return section_info + tasks_info


task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())
