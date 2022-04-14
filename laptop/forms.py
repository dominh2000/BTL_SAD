from django import forms
from .models import *


class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = ['name', 'batteryCapacity', 'os', 'bundledSoftwares', 'releaseDate', 'manufacturer',
                  'description', 'price', ]


class LaptopImageForm(forms.ModelForm):
    class Meta:
        model = LaptopImage
        fields = ['src', ]


class DimensionsForm(forms.ModelForm):
    class Meta:
        model = Dimensions
        fields = ['dimensions', 'weight', 'material', ]


class PhysicalInterfaceForm(forms.ModelForm):
    class Meta:
        model = PhysicalInterface
        fields = ['interface', ]


class WirelessTechForm(forms.ModelForm):
    class Meta:
        model = WirelessTech
        fields = ['tech', ]


class OtherFeaturesForm(forms.ModelForm):
    class Meta:
        model = OtherFeatures
        fields = ['feature', ]


class LaptopInterfacesForm(forms.ModelForm):
    class Meta:
        model = LaptopInterfaces
        fields = ['wirelessConnection', 'webcam', 'otherFeat', 'memoryCard', 'keyboardLight', 'interfaces', ]


class SoundTechForm(forms.ModelForm):
    class Meta:
        model = SoundTech
        fields = ['tech', ]


class AudioVideoForm(forms.ModelForm):
    class Meta:
        model = AudioVideo
        fields = ['gpu', 'soundTechnologies', ]


class ScreenTechnologyForm(forms.ModelForm):
    class Meta:
        model = ScreenTechnology
        fields = ['tech', ]


class LaptopScreenForm(forms.ModelForm):
    class Meta:
        model = LaptopScreen
        fields = ['diagonal', 'resolution', 'refreshRate', 'touchable', 'technology', ]


class LaptopStorageForm(forms.ModelForm):
    class Meta:
        model = LaptopStorage
        fields = ['ramSize', 'ramType', 'busRamSpeed', 'maxSize', 'secondary', ]


class CpuForm(forms.ModelForm):
    class Meta:
        model = Cpu
        fields = ['cpuName', 'family', 'cores', 'threads', 'baseSpeed', 'maxSpeed', 'l3Cache', 'manufacturer', ]
