# Generated by Django 4.2 on 2023-04-30 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_remove_user_autor_birth_date_remove_user_autor_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
    ]
