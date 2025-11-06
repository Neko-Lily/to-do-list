import dbhandler
import tui

def main():
    dbhandler.init_table()
    while tui.running == True:
        tui.check_for_user_input()


if __name__ == "__main__":
    main()