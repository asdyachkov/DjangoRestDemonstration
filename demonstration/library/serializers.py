from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = "__all__"
        read_only_fields = ['id']

    def to_representation(self, instance):
        """
        Функция изменяет выводимое поле author объекта book с id автора на его имя и фамилию
        :param instance: Объект книги
        :return: Измененный объект для вывода
        """
        rep = super(BookSerializer, self).to_representation(instance)
        rep['autor'] = f"{instance.autor.name} {instance.autor.surname}"
        return rep


class BooksGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ["id", "name", "autor", "publish_date"]
        extra_kwargs = {'autor': {'write_only': True}, 'publish_date': {'write_only': True}}
