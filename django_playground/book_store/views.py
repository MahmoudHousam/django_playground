from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Author, Book, Library, Librarian
from django.views.generic import DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView


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


class UserSignUp(CreateView):
    form_class = UserCreationForm
    template_name = "register.html"
    success_url = reverse_lazy("login")


class UserLogin(LoginView):
    form_class = AuthenticationForm
    template_name = "login.html"


class UserLogout(LogoutView):
    next_page = reverse_lazy("login")
