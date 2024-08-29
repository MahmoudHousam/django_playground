from .models import Book, Library
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import DetailView, CreateView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import (
    UserPassesTestMixin,
    LoginRequiredMixin,
    PermissionRequiredMixin,
)


############################################################
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


############################################################
# Implement Basic User Authentication
class UserSignUp(CreateView):
    form_class = UserCreationForm
    template_name = "register.html"
    success_url = reverse_lazy("login")


class UserLogin(LoginView):
    form_class = AuthenticationForm
    template_name = "login.html"


class UserLogout(LogoutView):
    next_page = reverse_lazy("login")


############################################################
# Implement Role-based Access Control
class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.userprofile.role == "Admin"


class LibrarianRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.userprofile.role == "Librarian"


class MemberRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.userprofile.role == "Member"


class AdminView(LoginRequiredMixin, AdminRequiredMixin, TemplateView):
    template_name = "admin_view.html"


class LibrarianView(LoginRequiredMixin, LibrarianRequiredMixin, TemplateView):
    template_name = "librarian_view.html"


class MemberView(LoginRequiredMixin, MemberRequiredMixin, TemplateView):
    template_name = "member_view.html"


############################################################
# Implement Custom Permissions
class BookCreateView(PermissionRequiredMixin, CreateView):
    model = Book
    fields = ["title", "author"]
    template_name = "add_book.html"
    success_url = reverse_lazy("book_list")
    permission_required = "book_store.can_add_book"


class BookUpdateView(PermissionRequiredMixin, CreateView):
    model = Book
    fields = ["title", "author"]
    template_name = "update_book.html"
    success_url = reverse_lazy("book_list")
    permission_required = "book_store.can_update_book"


class BookDeleteView(PermissionRequiredMixin, CreateView):
    model = Book
    template_name = "delete_book.html"
    success_url = reverse_lazy("book_list")
    permission_required = "book_store.can_delete_book"
