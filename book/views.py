from django.shortcuts import render
from django.views import View
from .models import *
from .forms import *
from django.http import *
from django.forms import modelformset_factory
from django.contrib import messages


# Create your views here.


class GetBook(View):

    def get(self, request, isbn):
        book = Book.objects.get(pk=isbn)
        images = book.bookimage_set.all()
        authors = book.authors.all()
        return render(request, 'book/productInfo.html', {"book": book, "images": images, "authors": authors})


class AddBook(View):

    def get(self, request):
        ImageFormSet = modelformset_factory(BookImage, form=BookImageForm, extra=10)
        book_form = BookForm
        formset = ImageFormSet(queryset=BookImage.objects.none())
        return render(request, 'book/add_book.html', {'book_form': book_form, 'image_form': formset})

    def post(self, request):
        book_form = BookForm(request.POST)
        ImageFormSet = modelformset_factory(BookImage, form=BookImageForm, extra=10)
        formset = ImageFormSet(request.POST, request.FILES, queryset=BookImage.objects.none())
        if book_form.is_valid() and formset.is_valid():
            book = book_form.save()

            for form in formset.cleaned_data:
                if form:
                    print(form['src'])
                    src = form['src']
                    photo = BookImage(book=book, src=src)
                    photo.save()
            messages.success(request, "Lưu thành công")
        else:
            print(book_form.errors, formset.errors)
            messages.error(request, "Lưu không thành công")
        return HttpResponseRedirect('/book/addBook')


class AddPublisher(View):

    def get(self, request):
        publisher_form = PublisherForm
        return render(request, 'book/add_publisher.html', {'form': publisher_form})

    def post(self, request):
        publisher_form = PublisherForm(request.POST)
        if publisher_form.is_valid():
            publisher_form.save()
            messages.success(request, "Lưu thành công")
        else:
            print(publisher_form.errors)
            messages.error(request, "Lưu không thành công")
        return HttpResponseRedirect('/book/addBook')


class AddAuthor(View):

    def get(self, request):
        author_form = AuthorForm
        return render(request, 'book/add_author.html', {'form': author_form})

    def post(self, request):
        author_form = AuthorForm(request.POST)
        if author_form.is_valid():
            author_form.save()
            messages.success(request, "Lưu thành công")
        else:
            print(author_form.errors)
            messages.error(request, "Lưu không thành công")
        return HttpResponseRedirect('/book/addBook')


class AddCategory(View):

    def get(self, request):
        category_form = CategoryForm
        return render(request, 'book/add_category.html', {'form': category_form})

    def post(self, request):
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            messages.success(request, "Lưu thành công")
        else:
            print(category_form.errors)
            messages.error(request, "Lưu không thành công")
        return HttpResponseRedirect('/book/addBook')
