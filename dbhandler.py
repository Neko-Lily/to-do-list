import sqlite3
import task as ts

connection = sqlite3.connect("todolist.db")
cursor = connection.cursor()
listOfTables = []
listOfTasks = []

def init_table():
    check_for_table()
    get_todos()


def check_for_table():
    listOfTables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name ='tasks'").fetchall()
    if listOfTables == []:
        _create_new_table()
        print("Table 'tasks' created.")
    else:
        pass

def _create_new_table():
    cursor.execute("CREATE TABLE tasks(status, task, due_date)")

def get_todos():
    result = cursor.execute("SELECT * FROM tasks")
    rows = result.fetchall()
    for row in rows:
        task = ts.Task(row[1],row[2])
        if row[0] == True:
            task.complete()
        listOfTasks.append(task) 

def add_task_to_db(task, due_date):
    status = False
    cursor.execute("""
        INSERT INTO tasks (status, task, due_date) VALUES (?, ?, ?)
    """, (status, task, due_date))
    connection.commit()

def show_current_tasks():
    i = 0
    headline_printed = False
    for task in listOfTasks:
        if headline_printed == False:
            print("# | Done  |   Task   | Due Time")
            headline_printed = True
        print(str(i+1)+ " - " + str(task.completed) + " | " + task.task_name + " | " + str(task.due_date))
        i += 1

def change_to_completed(indice):
    task = listOfTasks[indice].task_name 
    cursor.execute("""
    UPDATE tasks
    SET status = ?
    WHERE task = ?
    """, (True, task))
    connection.commit()

def delete_task_from_db(indice):
    task = listOfTasks[indice].task_name
    cursor.execute("""
    DELETE FROM tasks 
    WHERE task = ?;
    """, (task,))
    connection.commit()

def quit_program(): 
    connection = sqlite3.connect("todolist.db")
    connection.commit()
    connection.close()
    quit