from django.contrib import admin
from .models import Autor, Book


class AutorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "surname", "birth_date")
    list_display_links = ("id", "name", "birth_date")
    search_fields = ("name", "birth_date")


class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "autor", "publish_date")
    list_display_links = ("id", "name",)
    search_fields = ("name", "autor", "publish_date")


admin.site.register(Autor, AutorAdmin)
admin.site.register(Book, BookAdmin)
