from django.urls import path
from .views import *

app_name = 'laptop'
urlpatterns = [
    path('get/<int:laptop_id>/', GetLaptop.as_view(), name='get_laptop'),
    path('addLaptop/', AddLaptop.as_view(), name='add_laptop'),
    path('addScreenTech/', AddScreenTech.as_view(), name='add_screen_tech'),
    path('addSoundTech/', AddSoundTech.as_view(), name='add_sound_tech'),
    path('addPhysicalInterface/', AddPhysicalInterface.as_view(), name='add_physical_interface'),
    path('addWirelessTech/', AddWirelessTech.as_view(), name='add_wireless_tech'),
    path('addOtherFeat/', AddOtherFeatures.as_view(), name='add_other_feat'),
]