from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

from .models import Book, Autor
from .serializers import BooksGetSerializer, BookSerializer


class BookApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated,)


class BooksApiView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BooksGetSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        token = request.META["HTTP_AUTHORIZATION"].split()[1]
        User = get_user_model()
        token = Token.objects.get(key=token)
        user = User.objects.get(id=token.user_id)
        try:
            autor = Autor.objects.filter(
                name=user.first_name, surname=user.last_name
            ).first()
            id_ = autor.id
        except:
            autor = Autor.objects.create(name=user.first_name, surname=user.last_name)
        request.data.update(autor=autor.id)
        serializer = BooksGetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"added_book": serializer.data})
