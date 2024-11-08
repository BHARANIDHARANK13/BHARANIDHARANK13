import json
import os

book_catalogue = {}

def load_books():
    global book_catalog
    if os.path.exists('book_catalogue.json'):
        with open('book_catalogue.json','r') as file:
            book_catalog = json.load(file)
    else:
        book_catalog = {}

def save_books():
    with open('book_catalogue.json', 'w') as file:
        json.dump(book_catalog, file, indent=4)

def add_book():
    title = input('Enter book title: ').strip()
    author = input('Enter author name: ').strip()
    genre = input('Enter book genre: ').strip()
    year = input('Enter publication year: ').strip()
    isbn = input('Enter ISBN number: ').strip()
    if title and author:
        book_catalogue[title] = {
            'author': author,
            'details': {
                'genre': genre,
                'year': year,
                'isbn': isbn
            }
        }
        print(f'Book "{title}" by {author} added successfully.')
        save_books()
    else:
        print("Title and author are required fields. Book not added.")

def view_books():
    if not book_catalogue:
        print('No books in catalog.')
        return
    print('-' * 50)
    for title, info in book_catalogue.items():
        print(f"Title: {title}")
        print(f"Author: {info['author']}")
        details = info['details']
        print(f"Genre: {details['genre']}")
        print(f"Year: {details['year']}")
        print(f"ISBN: {details['isbn']}")
        print('-' * 20)

def search_books():
    keyword = input("Enter keyword to search: ").strip().lower()
    results = []
    for title, info in book_catalogue.items():
        if (keyword in title.lower() or keyword in info["author"].lower() or
            keyword in info["details"]["genre"].lower()):
            results.append(title)
    if results:
        print("Found books:")
        for book in results:
            print(book)
    else:
        print("No books found matching that keyword.")

# Load books from file at the start
load_books()

# Main program loop
while True:
    print("\nBook Catalog Menu:")
    print("1. Add Book")
    print('2. View Books')
    print('3. Search Books')
    print('4. Exit')
    choice = input('Enter your choice (1-4): ').strip()
    if choice == '1':
        add_book()
    elif choice == '2':
        view_books()
    elif choice == '3':
        search_books()
    elif choice == '4':
        break
    else:
        print('Invalid choice. Please try again.')
