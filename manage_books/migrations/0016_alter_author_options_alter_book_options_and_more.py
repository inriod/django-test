# Generated by Django 4.2 on 2023-04-27 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manage_books', '0015_alter_author_options_alter_book_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['Name']},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['-Published_date']},
        ),
        migrations.AlterModelOptions(
            name='bookcopy',
            options={'ordering': ['ISBN']},
        ),
    ]
