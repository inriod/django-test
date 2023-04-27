# Generated by Django 4.2 on 2023-04-27 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manage_books', '0006_book_published_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='published_date',
            new_name='Published_date',
        ),
        migrations.CreateModel(
            name='Book_Copy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='manage_books.book')),
            ],
        ),
    ]
