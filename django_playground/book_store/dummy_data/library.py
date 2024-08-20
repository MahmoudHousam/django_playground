from book_store.models import Book, Library

books_fetch = Book.objects.all()
books_dict = {book.title: book for book in books_fetch}

create_libraries = [
    Library(name="The Grey Publisher", books=books_dict["1984"]),
    Library(name="The Grey Publisher", books=books_dict["Animal Farm"]),
    Library(name="The Grey Publisher", books=books_dict["Homage to Catalonia"]),
    Library(name="The Grey Publisher", books=books_dict["To Kill a Mockingbird"]),
    Library(name="The Grey Publisher", books=books_dict["Go Set a Watchman"]),
    Library(
        name="The Grey Publisher",
        books=books_dict["Harry Potter and the Sorcerer’s Stone"],
    ),
    Library(
        name="The Grey Publisher",
        books=books_dict["Harry Potter and the Chamber of Secrets"],
    ),
    Library(
        name="The Grey Publisher",
        books=books_dict["Harry Potter and the Prisoner of Azkaban"],
    ),
    Library(name="The Grey Publisher", books=books_dict["The Great Gatsby"]),
    Library(name="The Grey Publisher", books=books_dict["Tender Is the Night"]),
    Library(name="The Grey Publisher", books=books_dict["The Beautiful and Damned"]),
    Library(name="The Grey Publisher", books=books_dict["The Lord of the Rings"]),
    Library(name="The Grey Publisher", books=books_dict["The Hobbit"]),
    Library(name="The Grey Publisher", books=books_dict["The Silmarillion"]),
    Library(name="The Grey Publisher", books=books_dict["Pride and Prejudice"]),
    Library(name="House of Paper", books=books_dict["Sense and Sensibility"]),
    Library(name="House of Paper", books=books_dict["Emma"]),
    Library(
        name="House of Paper", books=books_dict["The Adventures of Huckleberry Finn"]
    ),
    Library(name="House of Paper", books=books_dict["The Adventures of Tom Sawyer"]),
    Library(
        name="House of Paper",
        books=books_dict["A Connecticut Yankee in King Arthurs Court"],
    ),
    Library(name="House of Paper", books=books_dict["War and Peace"]),
    Library(name="House of Paper", books=books_dict["Anna Karenina"]),
    Library(name="House of Paper", books=books_dict["The Death of Ivan Ilyich"]),
    Library(name="House of Paper", books=books_dict["Frankenstein"]),
    Library(name="House of Paper", books=books_dict["The Last Man"]),
    Library(name="House of Paper", books=books_dict["One Hundred Years of Solitude"]),
    Library(name="House of Paper", books=books_dict["Love in the Time of Cholera"]),
    Library(name="House of Paper", books=books_dict["Chronicle of a Death Foretold"]),
]
create_libraries = []


for book_title, book_instance in books_dict.items():
    library_object = Library(name="The Grey Publisher")
    create_libraries.append(library_object)
    library_object = Library(name="House of Paper")
    create_libraries.append(library_object)

library = Library.objects.bulk_create(create_libraries)
