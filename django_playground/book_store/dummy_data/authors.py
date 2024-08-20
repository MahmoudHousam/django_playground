from book_store.models import Author

create_authors = [
    Author(name="George Orwell"),
    Author(name="Harper Lee"),
    Author(name="J.K. Rowling"),
    Author(name="F. Scott Fitzgerald"),
    Author(name="J.R.R. Tolkien"),
    Author(name="Jane Austen"),
    Author(name="Mark Twain"),
    Author(name="Leo Tolstoy"),
    Author(name="Mary Shelley"),
    Author(name="Gabriel García Márquez"),
]
authors = Author.objects.bulk_create(create_authors)
