import dbhandler
import task as ts


menu = { 
    1: 'Add New Task',
    2: 'View All Tasks',
    3: 'Mark Task as Completed',
    4: 'Delete Task',
    5: 'Quit'
}

def show_menu_options():
    print("Welcome to your To-Do List!")
    for key, value in menu.items():
        print(f'{key} -- {value}')

def add_task():
    task = input("Task to be added: ")
    due_date = input("Due date: ")
    new_todo = ts.Task(task, due_date)
    dbhandler.add_task_to_db(new_todo.task_name, new_todo.due_date)
    dbhandler.listOfTasks.append(new_todo)


def show_tasks():
    dbhandler.show_current_tasks()

def task_completed():
    show_tasks()
    completed_number = int(input("Enter number of task to be completed: ")) - 1
    dbhandler.listOfTasks[completed_number].complete()
    dbhandler.change_to_completed(completed_number)


def delete_task():
    pass