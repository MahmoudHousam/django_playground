from book_store.models import Library, Librarian

grey_publisher_library = Library.objects.get(name="The Grey Publisher")
house_of_paper_library = Library.objects.get(name="House of Paper")

create_librarian = [
    Librarian(name="John Smith", library=grey_publisher_library),
    Librarian(name="Frank Kisy", library=house_of_paper_library),
]
librarian = Librarian.objects.bulk_create(create_librarian)
