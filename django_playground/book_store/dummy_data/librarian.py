from book_store.models import Librarian

create_librarian = [
    Librarian(name="John Smith", library="The Grey Publisher"),
    Librarian(name="Frank Kisy", library="House of Paper"),
]
librarian = Librarian.objects.bulk_create(create_librarian)
