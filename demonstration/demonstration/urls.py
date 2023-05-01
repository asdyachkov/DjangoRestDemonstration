from django.contrib import admin
from django.urls import path, re_path, include

from library.views import BookApiView, BooksApiView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/books/", BooksApiView.as_view()),
    path("api/books/<int:pk>/", BookApiView.as_view()),
    path("api/auth/", include("djoser.urls")),
    re_path(r"^auth/", include("djoser.urls.authtoken")),
]
