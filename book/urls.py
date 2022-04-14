from django.urls import path
from .views import *

app_name = 'book'
urlpatterns = [
    path('get/<str:isbn>/', GetBook.as_view(), name='get_book'),
    path('addBook/', AddBook.as_view(), name='add_book'),
    path('addAuthor/', AddAuthor.as_view(), name='add_author'),
    path('addPublisher/', AddPublisher.as_view(), name='add_publisher'),
    path('addCategory/', AddCategory.as_view(), name='add_category'),
]