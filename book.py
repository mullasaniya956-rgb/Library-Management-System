from database import connect

def add_book(title, author, isbn, quantity):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO books (title, author, isbn, quantity)
    VALUES (?, ?, ?, ?)
    """, (title, author, isbn, quantity))

    conn.commit()
    conn.close()

    print("Book added successfully!")
def view_books():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()

    print("\n{:<5} {:<25} {:<20} {:<15} {:<10}".format(
        "ID", "Title", "Author", "ISBN", "Qty"))

    print("-"*75)

    for book in books:
        print("{:<5} {:<25} {:<20} {:<15} {:<10}".format(
            book[0], book[1], book[2], book[3], book[4]))

    conn.close()
def search_book(keyword):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM books
    WHERE title LIKE ? OR author LIKE ? OR isbn LIKE ?
    """, ('%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%'))

    books = cursor.fetchall()

    if books:
        print("\n--- Search Results ---")
        for book in books:
            print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, ISBN: {book[3]}, Quantity: {book[4]}")
    else:
        print("No books found.")

    conn.close() 