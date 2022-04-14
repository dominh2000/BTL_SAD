from django import forms
from .models import *


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['isbn', 'title', 'description', 'publicationDate', 'numOfPages',
                  'language', 'dimensions', 'weight', 'edition', 'price', 'authors', 'category', 'publisher', ]


class BookImageForm(forms.ModelForm):

    class Meta:
        model = BookImage
        fields = ['src', ]


class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ['name', 'bio', ]


class PublisherForm(forms.ModelForm):

    class Meta:
        model = Publisher
        fields = ['name', 'address', ]


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['type', ]
