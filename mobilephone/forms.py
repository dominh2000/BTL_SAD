from django import forms
from .models import *


class PhoneForm(forms.ModelForm):
    class Meta:
        model = MobilePhone
        fields = ['name', 'designType', 'material', 'dimensions', 'weight', 'releaseDate', 'manufacturer', 'speaker',
                  'description', 'price', ]


class PhoneImageForm(forms.ModelForm):
    class Meta:
        model = PhoneImage
        fields = ['src', ]


class PhoneScreenForm(forms.ModelForm):
    class Meta:
        model = PhoneScreen
        fields = ['technology', 'resolution', 'diagonal', 'refreshRate', 'brightness', 'glass', ]


class RearCameraForm(forms.ModelForm):
    class Meta:
        model = RearCameras
        fields = ['rearResolution', 'flash', 'rearRecordingRes', 'rearFeatures', ]


class FrontCameraForm(forms.ModelForm):
    class Meta:
        model = FrontCamera
        fields = ['frontResolution', 'frontRecordingRes', 'frontFeatures', ]


class PhoneStorageForm(forms.ModelForm):
    class Meta:
        model = PhoneStorage
        fields = ['ram', 'internalMem', 'internalMemAvail', 'memoryCard', 'contacts', ]


class OsCpuGpuForm(forms.ModelForm):
    class Meta:
        model = OsCpuGpu
        fields = ['os', 'cpu', 'cpuDescription', 'gpu', ]


class PhoneConnectionsForm(forms.ModelForm):
    class Meta:
        model = PhoneConnections
        fields = ['cellularNetwork', 'sim', 'wifi', 'gps', 'bluetooth', 'charger', 'headphone', 'others', ]


class BatteryForm(forms.ModelForm):
    class Meta:
        model = Battery
        fields = ['capacity', 'type', 'maxWattage', 'providedWattage', 'technologies', ]


class UtilForm(forms.ModelForm):
    class Meta:
        model = Utilities
        fields = ['advancedSecurities', 'resistances', 'recorder', 'audioFormats', 'specialFeatures', 'videoFormats', ]


class CamFeatureForm(forms.ModelForm):
    class Meta:
        model = CameraFeature
        fields = ['feature', ]


class AudioFormatForm(forms.ModelForm):
    class Meta:
        model = AudioFormat
        fields = ['format', ]


class VideoFormatForm(forms.ModelForm):
    class Meta:
        model = VideoFormat
        fields = ['format', ]


class SpecialFeatForm(forms.ModelForm):
    class Meta:
        model = SpecialFeature
        fields = ['feature', ]


class RecordingResForm(forms.ModelForm):
    class Meta:
        model = RecordingResolution
        fields = ['recordResolution', ]


class WifiTechForm(forms.ModelForm):
    class Meta:
        model = WifiTech
        fields = ['tech', ]


class GpsTechForm(forms.ModelForm):
    class Meta:
        model = GpsTech
        fields = ['tech', ]


class BluetoothTechForm(forms.ModelForm):
    class Meta:
        model = BluetoothTech
        fields = ['tech', ]


class ChargerTechForm(forms.ModelForm):
    class Meta:
        model = ChargerTech
        fields = ['tech', ]


class HeadphoneTechForm(forms.ModelForm):
    class Meta:
        model = HeadphoneTech
        fields = ['tech', ]


class BatteryTechForm(forms.ModelForm):
    class Meta:
        model = BatteryTech
        fields = ['tech', ]
