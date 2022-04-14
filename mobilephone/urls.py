from django.urls import path
from .views import *

app_name = 'mobile_phone'
urlpatterns = [
    path('get/<int:phone_id>/', GetPhone.as_view(), name='get_phone'),
    path('addPhone/', AddPhone.as_view(), name='add_phone'),
    path('addCamFeat/', AddCamFeature.as_view(), name='add_cam_feat'),
    path('addVideoFormat/', AddVideoFormat.as_view(), name='add_video_format'),
    path('addAudioFormat/', AddAudioFormat.as_view(), name='add_audio_format'),
    path('addSpecialFeat/', AddSpecialFeat.as_view(), name='add_special_feat'),
    path('addRecordingRes/', AddRecordingRes.as_view(), name='add_recording_res'),
    path('addWifiTech/', AddWifiTech.as_view(), name='add_wifi_tech'),
    path('addGpsTech/', AddGpsTech.as_view(), name='add_gps_tech'),
    path('addBluetoothTech/', AddBluetoothTech.as_view(), name='add_bluetooth_tech'),
    path('addChargerTech/', AddChargerTech.as_view(), name='add_charger_tech'),
    path('addHeadphoneTech/', AddHeadphoneTech.as_view(), name='add_headphone_tech'),
    path('addBatteryTech/', AddBatteryTech.as_view(), name='add_battery_tech'),
]
