import struct

RECORD_SIZE = 60
FILE_NAME = "library.dat"

def pack_record(book_id, title, author, stock):
    title = title.strip().encode().ljust(30)
    author = author.strip().encode().ljust(20)
    return struct.pack('i30s20si', book_id, title, author, stock)

def unpack_record(record_bytes):
    book_id, title, author, stock = struct.unpack('i30s20si', record_bytes)
    return {
        "BookID": book_id,
        "Title": title.decode().strip(),
        "Author": author.decode().strip(),
        "Stock": stock
    }

def add_book():
    book_id = int(input("Enter book ID: "))
    title = input("Enter Title: ")
    author = input("Enter the author: ")
    stock = int(input("Enter Stock: "))
    record = pack_record(book_id, title, author, stock)
    with open(FILE_NAME, 'ab') as f:
        f.write(record)
        print("Book added successfully!")

def view_book():
    with open(FILE_NAME, 'rb') as f:
        print("\n=== Book records ===")
        while True:
            record = f.read(RECORD_SIZE)
            if not record:
                break
            book = unpack_record(record)
            print(book)

def search_book(book_id):
    with open(FILE_NAME, 'rb') as f:
        while True:
            record = f.read(RECORD_SIZE)
            if not record:
                break
            book = unpack_record(record)
            if book['BookID'] == book_id:
                print("Book found:", book)
                return
    print("Book not found")

def delete_book():
    book_id = int(input("Enter Book ID to Delete: "))
    found = False
    with open(FILE_NAME, 'r+b') as f:
        index = 0
        while True:
            f.seek(index * RECORD_SIZE)
            record = f.read(RECORD_SIZE)
            if not record:
                break
            book = unpack_record(record)
            if book["BookID"] == book_id:
                f.seek(index * RECORD_SIZE)
                # Set stock to 0 as "deleted"
                f.write(pack_record(book["BookID"], book["Title"], book["Author"], 0))
                found = True
                print("Book deleted (Stock = 0).")
                break
            index += 1
    if not found:
        print("Book not found")

