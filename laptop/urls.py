from django.urls import path
from .views import *

app_name = 'laptop'
urlpatterns = [
    path('get/<int:laptop_id>/', GetLaptop.as_view(), name='get_laptop'),
    path('addLaptop/', AddLaptop.as_view(), name='add_laptop'),
]