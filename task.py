class Task:
    def __init__(self, task_name, due_date):
        self.task_name = task_name
        self.due_date = due_date
        self.completed = False

    def change_name(self, new_name):
        self.name = new_name

    def change_due_date(self, new_date):
        self.due_date = new_date
    
    def complete(self):
        self.completed = True