from django.db import models

class Author(models.Model):
    Name = models.CharField(max_length=100)

    def __str__(self):
        return self.Name
    
    class Meta:
        ordering = ['Name']
        verbose_name = "Author"
        verbose_name_plural = "Authors"

class Book(models.Model):
    Title = models.CharField(max_length=100)
    Author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    Published_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.Title} by {self.Author}"
    
    class Meta:
        ordering = ['-Published_date']
        verbose_name = "Book"
        verbose_name_plural = "Books"
    
    

class BookCopy(models.Model):
    CONDITIONS = [
        ('G', 'Good'),
        ('F', 'Fair'),
        ('P', 'Poor')
    ]
    Book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    ISBN = models.CharField(max_length=17, null=True)
    Condition = models.CharField(choices=CONDITIONS, max_length=10, null=True)
    Available = models.BooleanField(default=True, null=True)

    def __str__(self):
        return f"{self.ISBN} - {self.Book.Title}"

    class Meta:
        ordering = ['ISBN']
        verbose_name = "Copy of a Book"
        verbose_name_plural="Copies of Books"