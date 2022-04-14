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

    def post(self, request):
        laptop_form = LaptopForm(request.POST)
        dimensions_form = DimensionsForm(request.POST)
        interfaces_form = LaptopInterfacesForm(request.POST)
        audio_video_form = AudioVideoForm(request.POST)
        screen_form = LaptopScreenForm(request.POST)
        storage_form = LaptopStorageForm(request.POST)
        cpu_form = CpuForm(request.POST)
        ImageFormSet = modelformset_factory(LaptopImage, form=LaptopImageForm, extra=15)
        formset = ImageFormSet(request.POST, request.FILES, queryset=LaptopImage.objects.none())

        if (laptop_form.is_valid() and dimensions_form.is_valid() and interfaces_form.is_valid()
        and audio_video_form.is_valid() and screen_form.is_valid() and storage_form.is_valid()
        and cpu_form.is_valid() and formset.is_valid()):
            dimensions = dimensions_form.save()
            interfaces = interfaces_form.save()
            audio_video = audio_video_form.save()
            screen = screen_form.save()
            storage = storage_form.save()
            cpu = cpu_form.save()

            laptop_form.instance.cpu = cpu
            laptop_form.instance.laptopStorage = storage
            laptop_form.instance.laptopScreen = screen
            laptop_form.instance.audioVideo = audio_video
            laptop_form.instance.laptopInterfaces = interfaces
            laptop_form.instance.dimensions = dimensions
            laptop = laptop_form.save()

            for form in formset.cleaned_data:
                if form:
                    print(form['src'])
                    src = form['src']
                    photo = LaptopImage(laptop=laptop, src=src)
                    photo.save()
            messages.success(request, "Lưu thành công")
        else:
            print(laptop_form.errors, dimensions_form.errors, interfaces_form.errors, audio_video_form.errors,
                  screen_form.errors, storage_form.errors, cpu_form.errors, formset.errors)
            messages.error(request, "Lưu không thành công")
        return HttpResponseRedirect('/laptop/addLaptop')


class AddScreenTech(View):

    def get(self, request):
        screen_tech_form = ScreenTechnologyForm
        return render(request, 'laptop/add_screen_tech.html', {'form': screen_tech_form})

    def post(self, request):
        screen_tech_form = ScreenTechnologyForm(request.POST)
        if screen_tech_form.is_valid():
            screen_tech_form.save()
            messages.success(request, "Lưu thành công")
        else:
            print(screen_tech_form.errors)
            messages.error(request, "Lưu không thành công")
        return HttpResponseRedirect('/laptop/addLaptop')


class AddSoundTech(View):

    def get(self, request):
        sound_tech_form = SoundTechForm
        return render(request, 'laptop/add_sound_tech.html', {'form': sound_tech_form})

    def post(self, request):
        sound_tech_form = SoundTechForm(request.POST)
        if sound_tech_form.is_valid():
            sound_tech_form.save()
            messages.success(request, "Lưu thành công")
        else:
            print(sound_tech_form.errors)
            messages.error(request, "Lưu không thành công")
        return HttpResponseRedirect('/laptop/addLaptop')


class AddPhysicalInterface(View):

    def get(self, request):
        physical_interface_form = PhysicalInterfaceForm
        return render(request, 'laptop/add_physical_interface.html', {'form': physical_interface_form})

    def post(self, request):
        physical_interface_form = PhysicalInterfaceForm(request.POST)
        if physical_interface_form.is_valid():
            physical_interface_form.save()
            messages.success(request, "Lưu thành công")
        else:
            print(physical_interface_form.errors)
            messages.error(request, "Lưu không thành công")
        return HttpResponseRedirect('/laptop/addLaptop')


class AddWirelessTech(View):

    def get(self, request):
        wireless_tech_form = WirelessTechForm
        return render(request, 'laptop/add_wireless_tech.html', {'form': wireless_tech_form})

    def post(self, request):
        wireless_tech_form = WirelessTechForm(request.POST)
        if wireless_tech_form.is_valid():
            wireless_tech_form.save()
            messages.success(request, "Lưu thành công")
        else:
            print(wireless_tech_form.errors)
            messages.error(request, "Lưu không thành công")
        return HttpResponseRedirect('/laptop/addLaptop')


class AddOtherFeatures(View):

    def get(self, request):
        other_feat_form = OtherFeaturesForm
        return render(request, 'laptop/add_other_feat.html', {'form': other_feat_form})

    def post(self, request):
        other_feat_form = OtherFeaturesForm(request.POST)
        if other_feat_form.is_valid():
            other_feat_form.save()
            messages.success(request, "Lưu thành công")
        else:
            print(other_feat_form.errors)
            messages.error(request, "Lưu không thành công")
        return HttpResponseRedirect('/laptop/addLaptop')