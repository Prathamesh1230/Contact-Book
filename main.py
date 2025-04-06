from database import connect
from ui import menu

if __name__ == "__main__":
    connect()  # Setup database
    menu()     # Launch CLI
