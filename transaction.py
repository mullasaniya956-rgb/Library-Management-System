from database import connect
from datetime import datetime

def borrow_book(book_id, user_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT quantity FROM books WHERE book_id=?", (book_id,))
    book = cursor.fetchone()

    if book is None:
        print("Book not found!")
        conn.close()
        return

    if book[0] <= 0:
        print("Book not available!")
        conn.close()
        return

    cursor.execute("""
    UPDATE books
    SET quantity = quantity - 1
    WHERE book_id=?
    """, (book_id,))

    borrow_date = datetime.now().strftime("%Y-%m-%d")

    cursor.execute("""
    INSERT INTO transactions (book_id, user_id, borrow_date, return_date)
    VALUES (?, ?, ?, NULL)
    """, (book_id, user_id, borrow_date))

    conn.commit()
    conn.close()

    print("Book borrowed successfully!")


def return_book(book_id, user_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT transaction_id FROM transactions
    WHERE book_id=? AND user_id=? AND return_date IS NULL
    """, (book_id, user_id))

    transaction = cursor.fetchone()

    if transaction is None:
        print("No active borrow record found!")
        conn.close()
        return

    return_date = datetime.now().strftime("%Y-%m-%d")

    cursor.execute("""
    UPDATE transactions
    SET return_date=?
    WHERE transaction_id=?
    """, (return_date, transaction[0]))

    cursor.execute("""
    UPDATE books
    SET quantity = quantity + 1
    WHERE book_id=?
    """, (book_id,))

    conn.commit()
    conn.close()

    print("Book returned successfully!")

def view_transactions():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT t.transaction_id, b.title, u.username, t.borrow_date, t.return_date
    FROM transactions t
    JOIN books b ON t.book_id = b.book_id
    JOIN users u ON t.user_id = u.user_id
    """)

    records = cursor.fetchall()

    print("\n--- Borrow History ---")

    for r in records:
        print(f"Transaction ID: {r[0]}, Book: {r[1]}, User: {r[2]}, Borrowed: {r[3]}, Returned: {r[4]}")

    conn.close()