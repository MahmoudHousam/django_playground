from django.shortcuts import render
from django.views.generic import DetailView
from .models import Author, Book, Library, Librarian


# Create your views here.
def list_books(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(
        request=request,
        template_name="list_books.html",
        context=context,
    )


class DetailLibrary(DetailView):
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"
