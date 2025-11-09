import dbhandler
import tui
current_tasks = []
choice = ""

def main():
    dbhandler.init_table()
    tui.show_menu_options()
    global choice

    while choice != '5':
        # Add Task
        if choice == '1':
            tui.add_task()
        # Show all tasks
        elif choice == '2':
            tui.show_tasks()
        # Mark task as completed
        elif choice == '3':
            tui.task_completed()
        # Remove Task
        elif choice == '4':
            pass
        # Show menu tooltips
        elif choice == 'h':
            tui.show_menu_options()
        # Quit Program
        elif choice == '5':
            dbhandler.quit_program()
        
        choice = input("For help enter h \n"
        "Please enter your selection: ")


if __name__ == "__main__":
    main()