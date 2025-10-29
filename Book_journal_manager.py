from book_manager import *


def show_menu():
    while True:
        print("=== Library Management===")
        print("1. Add Book")
        print("2. View books")
        print("3. search book bt ID")
        print("4. Delete book")
        print("5. Exit")
        choice = input('Enter your choice(1-5): ')
        
        if choice == "1":
            add_book()
        elif choice =="2":
            view_book()
        elif choice =="3":
            search_book()
        elif choice =="4":
            delete_book()
        elif choice == "5":
            break
        else:
            print("Invalid choice, Try Again")
        input("\nPress Enter To Continue...")

if __name__ == "__main__":
    show_menu()