from django.contrib import admin
from .models import Autor, Book


class AutorAdmin(admin.ModelAdmin):
    list_display = ("name", "surname", "birth_date")
    list_display_links = ("name", "birth_date")
    search_fields = ("name", "birth_date")


class BookAdmin(admin.ModelAdmin):
    list_display = ("name", "autor", "publish_date")
    list_display_links = ("name",)
    search_fields = ("name", "autor", "publish_date")


admin.site.register(Autor, AutorAdmin)
admin.site.register(Book, BookAdmin)
