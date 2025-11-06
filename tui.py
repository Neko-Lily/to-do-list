import dbhandler

running = True

user_input = None
def check_for_user_input():
    print("Welcome to your To-Do-List!")
    
    
    user_input = input("For help type: h " + "\n")

    if user_input == "h":
        print("""Your following options are: 
        \n - showlist
        \n - addtask
        \n - quit
        """)
        user_input = input("Please enter a command: \n")
    
    elif user_input == "showlist":
        dbhandler.show_current_tasks()
        user_input = input("Please enter a new command: \n")
    
    elif user_input == "addtask":
        dbhandler.add_task()
        user_input = input("Task has been added, enter your command: \n")
    
    elif user_input == "quit":
        print("Thanks for using this program!")
        runing = False
        quit()
