import json
book_file = "books.txt"
def load_books():
    try:
        with open(book_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
def save_books(books):
    try:
        with open(book_file, "w") as file:
            json.dump(books, file)
    except Exception as e:
        print(f"Error saving books: {e}")
def add_book():
    title = input("\nEnter the title of the book: ")
    author = input("Enter the author of the book: ")
    year = int(input("Enter the year of the book: "))
    genre = input("Enter the genre of the book: ")
    status = input("Have you read this book? (yes/no): ")
    if status.lower() == "yes":
        status = "Read"
    else:
        status = "Unread"
    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "status": status,
    }
    books = load_books()
    books.append(book)
    save_books(books)
    print(f"Book added: {title} by {author} successfully!")
def remove_book():
    title = input("\nEnter the title of the book: ")
    books = load_books()
    for book in books:
        if book["title"] == title:
            books.remove(book)  
            save_books(books)
            print(f"Book '{title}' removed successfully: ")
            break
    else:
        print(f"Book not found: {title}")    
def search_book():
    search_type = input("\nEnter 1 to search by title, 2 to search by author: ")
    if search_type == "1":
        title = input("Enter the title of the book: ")
        books = load_books()
        for book in books:
            if book["title"].lower() == title.lower():
                print(f"Book found: {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {book['status']}")
                break
        else:
            print(f"Book not found: {title}")
    elif search_type == "2":
        author = input("Enter the author of the book: ")
        books = load_books()
        for book in books:
            if book["author"].lower() == author.lower():
                print(f"Book found: {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {book['status']}")
                break
        else:
            print(f"Book written by {author} not found!")
    else:
        print("Invalid search type. Please enter 1 or 2.")
def view_books():
    books = load_books()
    if not books:
        print("No books in the library.")
        return
    print("\nLibrary Catalog:\n")
    i=0
    for book in books:
        print(f"{i+1}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {book['status']}")
        i += 1
def display_statistics():
    books = load_books()
    if not books:
        print("No books in the library.")
    total_books = len(books)
    read = 0
    for book in books:
        if book["status"].lower() == "read":
            read += 1
    percentage_read = read / total_books * 100
    print(f"\nTotal books: {total_books}")
    print(f"Percentage of books read: {percentage_read:.2f}%")
def main():
    while True:
        print("\n*** Welcome to your Personal Library Manager! ***")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. View all books")
        print("5. Display Statistics")
        print("6. Exit")
        choice = input("\nEnter your choice: ")
        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            search_book()
        elif choice == "4":
            view_books()
        elif choice == "5":
            display_statistics()
        elif choice == "6":
            print("\n==== Library saved to file. Goodbye!+ ====")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
if __name__ == "__main__":
    main()

