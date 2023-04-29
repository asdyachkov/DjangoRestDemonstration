from django.forms import model_to_dict
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book
from .serializers import BooksGetSerializer, BookSerializer


class BookApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BooksApiView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BooksGetSerializer

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"added_book": serializer.data})
