from book_store.models import Book, Library

books_fetch = Book.objects.all()
books_dict = {book.title: book for book in books_fetch}
libraries_data = {
    "The Grey Publisher": [
        "1984",
        "Animal Farm",
        "Homage to Catalonia",
        "To Kill a Mockingbird",
        "Go Set a Watchman",
        "Harry Potter and the Sorcerer Stone",
        "Harry Potter and the Chamber of Secrets",
        "Harry Potter and the Prisoner of Azkaban",
        "The Great Gatsby",
        "Tender Is the Night",
        "The Beautiful and Damned",
        "The Lord of the Rings",
        "The Hobbit",
        "The Silmarillion",
        "Pride and Prejudice",
    ],
    "House of Paper": [
        "Sense and Sensibility",
        "Emma",
        "The Adventures of Huckleberry Finn",
        "The Adventures of Tom Sawyer",
        "A Connecticut Yankee in King Arthur’s Court",
        "War and Peace",
        "The Death of Ivan Ilyich",
        "Anna Karenina",
        "Frankenstein",
        "The Last Man",
        "Love in the Time of Cholera",
        "One Hundred Years of Solitude",
        "Chronicle of a Death Foretold",
    ],
}

create_libraries = []


for (
    library_name,
    book_title,
) in libraries_data.items():
    library_object = Library(name=library_name)
    library_object.save()
    create_libraries.append(library_object)

library = Library.objects.bulk_create(create_libraries)

for library, book_titles in zip(create_libraries, libraries_data.values()):
    book_instances = [books_dict[title] for title in book_titles]
    library.books.set(book_instances)
