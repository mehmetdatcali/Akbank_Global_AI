class Library:
    def __init__(self):
        self.file_path = "books.txt"
        self.file = open(self.file_path, "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        book_lines = self.file.read().splitlines()
        for line in book_lines:
            book_info = line.split(',')
            print(f"Book: {book_info[0]}, Author: {book_info[1]}")

    def add_book(self):
        title = input("Book title: ")
        author = input("Author's name: ")
        release_year = input("Release year: ")
        num_pages = input("Number of pages: ")

        book_info = f"{title},{author},{release_year},{num_pages}\n"
        self.file.write(book_info)
        print("Book added!")

    def remove_book(self):
        title_to_remove = input("Enter the title of book: ")

        self.file.seek(0)
        book_lines = self.file.read().splitlines()

        updated_book_list = [line for line in book_lines if title_to_remove not in line]

        self.file.seek(0)
        self.file.truncate()

        for line in updated_book_list:
            self.file.write(line + '\n')

        print("Book removed!")

lib = Library()

while True:
    print("MENU")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    elif choice == '4':
        break
    else:
        print("Enter your choice (1-4): ")