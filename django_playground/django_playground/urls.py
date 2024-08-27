"""
URL configuration for django_playground project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from book_store.views import (
    list_books,
    DetailLibrary,
    UserSignUp,
    UserLogin,
    UserLogout,
    AdminView,
    LibrarianView,
    MemberView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("book_list/", list_books, name="list_books"),
    path("library/<int:pk>/", DetailLibrary.as_view(), name="library_detail"),
    path("signin/", UserSignUp.as_view(), name="sign-in"),
    path("login/", UserLogin.as_view(), name="login"),
    path("logout/", UserLogout.as_view(), name="logout"),
    path("adminview/", AdminView.as_view(), name="admin_view"),
    path("librarianview/", LibrarianView.as_view(), name="librarin_view"),
    path("memberview/", MemberView.as_view(), name="member_view"),
]
