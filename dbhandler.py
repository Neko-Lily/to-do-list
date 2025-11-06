import sqlite3
connection = sqlite3.connect("todolist.db")
cursor = connection.cursor()
listOfTables = []

def init_table():
    check_for_table()

def check_for_table():
    listOfTables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name ='tasks'").fetchall()
    if listOfTables == []:
        _create_new_table()
        print("Table 'tasks' created.")
    else:
        pass

def _create_new_table():
    cursor.execute("CREATE TABLE tasks(status, task)")

def return_results():
    result = cursor.execute("SELECT name FROM sqlite_master")
    print(result.fetchone())

def add_task():
    status = False
    task = input("Task to be added: ")
    cursor.execute("""
        INSERT INTO tasks (status, task) VALUES (?, ?)
    """, (status, task))
    connection.commit()
    

def show_current_tasks():
    result = cursor.execute("SELECT status, task FROM tasks")
    print(result.fetchall())