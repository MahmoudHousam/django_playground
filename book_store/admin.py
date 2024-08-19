from django.contrib import admin
from . import models


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_date")
    search_fields = ("title", "author")


admin.site.register(models.Book, BookAdmin)
