from django.shortcuts import render
from .models import Book


# Create your views here.
def list_books(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(
        request=request,
        template_name="list_books.html",
        context=context,
    )
