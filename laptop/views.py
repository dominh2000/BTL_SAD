from django.shortcuts import render
from django.views import View
from .models import *
from .forms import *
from django.http import *
from django.forms import modelformset_factory
from django.contrib import messages


# Create your views here.


class GetLaptop(View):

    def get(self, request, laptop_id):
        laptop = Laptop.objects.get(pk=laptop_id)
        images = laptop.laptopimage_set.all()
        screen = laptop.laptopScreen
        screenTech = screen.technology.all()
        audioVideo = laptop.audioVideo
        soundTech = audioVideo.soundTechnologies.all()
        laptopInterfaces = laptop.laptopInterfaces
        wirelessTech = laptopInterfaces.wirelessConnection.all()
        otherFeat = laptopInterfaces.otherFeat.all()
        interfaces = laptopInterfaces.interfaces.all()
        context = {"laptop": laptop, "images": images, "screenTech": screenTech, "soundTech": soundTech,
                   "wirelessTech": wirelessTech, "otherFeat": otherFeat, "interfaces": interfaces}
        return render(request, 'laptop/productInfo.html', context)


class AddLaptop(View):

    def get(self, request):
        ImageFormSet = modelformset_factory(LaptopImage, form=LaptopImageForm, extra=15)
        formset = ImageFormSet(queryset=LaptopImage.objects.none())
        laptop_form = LaptopForm
        dimensions_form = DimensionsForm
        interfaces_form = LaptopInterfacesForm
        audio_video_form = AudioVideoForm
        screen_form = LaptopScreenForm
        storage_form = LaptopStorageForm
        cpu_form = CpuForm
        context = {'laptop_form': laptop_form, 'img_form': formset, 'dimensions_form': dimensions_form,
                   'interfaces_form': interfaces_form, 'audio_video_form': audio_video_form,
                   'screen_form': screen_form, 'storage_form': storage_form, 'cpu_form': cpu_form}
        return render(request, 'laptop/add_laptop.html', context)