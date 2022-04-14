from django.db import models
from isbn_field import ISBNField

# Create your models here.


class Publisher(models.Model):
    name = models.CharField(blank=False, max_length=50)
    address = models.CharField(blank=True, max_length=256)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(blank=False, max_length=256)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    type = models.CharField(blank=False, max_length=50)

    def __str__(self):
        return self.type


class BookImage(models.Model):
    src = models.ImageField(upload_to='book/')
    book = models.ForeignKey('Book', on_delete=models.CASCADE)

    def __str__(self):
        return self.book.title


class Book(models.Model):
    isbn = ISBNField(primary_key=True)
    title = models.CharField(blank=False, max_length=256)
    description = models.TextField(blank=True)
    publicationDate = models.CharField(blank=False, max_length=50)
    numOfPages = models.IntegerField(blank=True)
    language = models.CharField(blank=True, max_length=25)
    dimensions = models.CharField(blank=True, max_length=50)
    weight = models.DecimalField(blank=True,max_digits=10, decimal_places=2)
    edition = models.CharField(blank=True, max_length=10)
    price = models.IntegerField()
    authors = models.ManyToManyField(Author)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class BookItem(models.Model):
    price = models.IntegerField()
    discount = models.DecimalField(max_digits=3, decimal_places=2)
    forSale = models.BooleanField()
    inventory = models.IntegerField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.book.title
