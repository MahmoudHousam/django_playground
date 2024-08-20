from book_store.models import Author, Book

authors_fetch = Author.objects.all()

# Step 2: Create books
author_dict = {author.name: author for author in authors_fetch}
create_books = [
    Book(title="1984", author=author_dict["George Orwell"]),
    Book(title="Animal Farm", author=author_dict["George Orwell"]),
    Book(title="Homage to Catalonia", author=author_dict["George Orwell"]),
    Book(title="To Kill a Mockingbird", author=author_dict["Harper Lee"]),
    Book(title="Go Set a Watchman", author=author_dict["Harper Lee"]),
    Book(
        title="Harry Potter and the Sorcerer Stone", author=author_dict["J.K. Rowling"]
    ),
    Book(
        title="Harry Potter and the Chamber of Secrets",
        author=author_dict["J.K. Rowling"],
    ),
    Book(
        title="Harry Potter and the Prisoner of Azkaban",
        author=author_dict["J.K. Rowling"],
    ),
    Book(title="The Great Gatsby", author=author_dict["F. Scott Fitzgerald"]),
    Book(title="Tender Is the Night", author=author_dict["F. Scott Fitzgerald"]),
    Book(title="The Beautiful and Damned", author=author_dict["F. Scott Fitzgerald"]),
    Book(title="The Lord of the Rings", author=author_dict["J.R.R. Tolkien"]),
    Book(title="The Hobbit", author=author_dict["J.R.R. Tolkien"]),
    Book(title="The Silmarillion", author=author_dict["J.R.R. Tolkien"]),
    Book(title="Pride and Prejudice", author=author_dict["Jane Austen"]),
    Book(title="Sense and Sensibility", author=author_dict["Jane Austen"]),
    Book(title="Emma", author=author_dict["Jane Austen"]),
    Book(title="The Adventures of Huckleberry Finn", author=author_dict["Mark Twain"]),
    Book(title="The Adventures of Tom Sawyer", author=author_dict["Mark Twain"]),
    Book(
        title="A Connecticut Yankee in King Arthur’s Court",
        author=author_dict["Mark Twain"],
    ),
    Book(title="War and Peace", author=author_dict["Leo Tolstoy"]),
    Book(title="The Death of Ivan Ilyich", author=author_dict["Leo Tolstoy"]),
    Book(title="Anna Karenina", author=author_dict["Leo Tolstoy"]),
    Book(title="Frankenstein", author=author_dict["Mary Shelley"]),
    Book(title="The Last Man", author=author_dict["Mary Shelley"]),
    Book(
        title="Love in the Time of Cholera",
        author=author_dict["Gabriel García Márquez"],
    ),
    Book(
        title="One Hundred Years of Solitude",
        author=author_dict["Gabriel García Márquez"],
    ),
    Book(
        title="Chronicle of a Death Foretold",
        author=author_dict["Gabriel García Márquez"],
    ),
]

books = Book.objects.bulk_create(create_books)
