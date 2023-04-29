from django.db import models


class Autor(models.Model):

    name = models.TextField(null=False, verbose_name='Имя')
    surname = models.TextField(null=False, verbose_name='Фамилия')
    birth_date = models.DateField(null=False, verbose_name='Дата рождения')

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
        db_table = "autors"
        ordering = ["birth_date"]

    def __str__(self):
        return f"{self.name} {self.surname}"


class Book(models.Model):

    name = models.TextField(null=False, verbose_name='Имя')
    autor = models.ForeignKey("Autor", null=False, on_delete=models.CASCADE, verbose_name='Автор')
    description = models.TextField(null=False, verbose_name='Описание')
    publish_date = models.DateField(null=False, verbose_name='Дата публикации')

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        db_table = "books"
        ordering = ["autor", "publish_date"]

    def __str__(self):
        return str(self.name)
