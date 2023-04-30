# Generated by Django 4.2 on 2023-04-30 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_remove_user_birth_date_remove_user_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='autor_birth_date',
        ),
        migrations.RemoveField(
            model_name='user',
            name='autor_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='autor_surname',
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='Name', max_length=100, verbose_name='Имя писателя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='Surname', max_length=100, verbose_name='Фамилия писателя'),
        ),
    ]
