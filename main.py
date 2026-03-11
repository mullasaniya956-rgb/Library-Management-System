from database import create_tables
from book import add_book, view_books, search_book
from user import register_user, login_user
from transaction import borrow_book, return_book, view_transactions
def main():
    create_tables()
    print("\n=================================")
    print("   LIBRARY MANAGEMENT SYSTEM")
    print("   Developed using Python")
    print("=================================\n")

    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Books")
        print("4. Register User")
        print("5. Login")
        print("6. Borrow Book")
        print("7. Return Book")
        print("8. view Borrw History")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN: ")
            quantity = int(input("Enter quantity: "))

            add_book(title, author, isbn, quantity)

        elif choice == "2":
            view_books()

        elif choice == "3":
            keyword = input("Enter title, author, or ISBN to search: ")
            search_book(keyword)
        elif choice == "4":
            name = input("Enter your name: ")
            username = input("Enter username: ")
            password = input("Enter password: ")

            register_user(name, username, password)

        elif choice == "5":
            username = input("Enter username: ")
            password = input("Enter password: ")

            user_id = login_user(username, password)

            if user_id:
                print("Welcome! User ID:", user_id)

        elif choice == "6":
            user_id = int(input("Enter your user ID: "))
            book_id = int(input("Enter book ID to borrow: "))

            borrow_book(book_id, user_id)

        elif choice == "7":
            user_id = int(input("Enter your user ID: "))
            book_id = int(input("Enter book ID to return: "))

            return_book(book_id, user_id)

        elif choice == "8":
            view_transactions()

        elif choice == "9":
            print("Exiting the system. Goodbye!")
            break
                        
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()