from django.shortcuts import render
from django.views import View
from .models import *
from .forms import *
from django.http import *
from django.forms import modelformset_factory
from django.contrib import messages


# Create your views here.


class GetPhone(View):

    def get(self, request, phone_id):
        phone = MobilePhone.objects.get(pk=phone_id)
        images = phone.phoneimage_set.all()
        rearCam = phone.rearCameras
        frontCam = phone.frontCamera
        rearCamFeature = rearCam.rearFeatures.all()
        rearCamRecordingRes = rearCam.rearRecordingRes.all()
        frontCamFeature = frontCam.frontFeatures.all()
        frontCamRecordingRes = frontCam.frontRecordingRes.all()
        connections = phone.phoneConnections
        wifiTech = connections.wifi.all()
        gpsTech = connections.gps.all()
        bluetoothTech = connections.bluetooth.all()
        headphoneTech = connections.headphone.all()
        battery = phone.battery
        batteryTech = battery.technologies.all()
        utils = phone.utilities
        audioFormat = utils.audioFormats.all()
        specialFeature = utils.specialFeatures.all()
        videoFormat = utils.videoFormats.all()
        context = {"phone": phone, "images": images, "rearCamFeature": rearCamFeature,
                   "rearCamRecordingRes": rearCamRecordingRes,
                   "frontCamFeature": frontCamFeature, "frontCamRecordingRes": frontCamRecordingRes,
                   "wifiTech": wifiTech,
                   "gpsTech": gpsTech, "bluetoothTech": bluetoothTech, "headphoneTech": headphoneTech,
                   "batteryTech": batteryTech, "audioFormat": audioFormat, "specialFeature": specialFeature,
                   "videoFormat": videoFormat}
        return render(request, 'mobilephone/productInfo.html', context)


class AddPhone(View):

    def get(self, request):
        ImageFormSet = modelformset_factory(PhoneImage, form=PhoneImageForm, extra=15)
        formset = ImageFormSet(queryset=PhoneImage.objects.none())
        phone_form = PhoneForm
        screen_form = PhoneScreenForm
        rear_cam_form = RearCameraForm
        front_cam_form = FrontCameraForm
        storage_form = PhoneStorageForm
        os_form = OsCpuGpuForm
        connect_form = PhoneConnectionsForm
        battery_form = BatteryForm
        util_form = UtilForm
        context = {'phone_form': phone_form, 'img_form': formset, 'screen_form': screen_form,
                   'rear_cam_form': rear_cam_form,
                   'front_cam_form': front_cam_form, 'storage_form': storage_form, 'os_form': os_form,
                   'connect_form': connect_form,
                   'battery_form': battery_form, 'util_form': util_form}
        return render(request, 'mobilephone/add_phone.html', context)

    def post(self, request):
        phone_form = PhoneForm(request.POST)
        screen_form = PhoneScreenForm(request.POST)
        rear_cam_form = RearCameraForm(request.POST)
        front_cam_form = FrontCameraForm(request.POST)
        storage_form = PhoneStorageForm(request.POST)
        os_form = OsCpuGpuForm(request.POST)
        connect_form = PhoneConnectionsForm(request.POST)
        battery_form = BatteryForm(request.POST)
        util_form = UtilForm(request.POST)
        ImageFormSet = modelformset_factory(PhoneImage, form=PhoneImageForm, extra=15)
        formset = ImageFormSet(request.POST, request.FILES, queryset=PhoneImage.objects.none())

        if (phone_form.is_valid() and screen_form.is_valid() and rear_cam_form.is_valid() and front_cam_form.is_valid()
                and storage_form.is_valid() and os_form.is_valid() and connect_form.is_valid() and battery_form.is_valid()
                and util_form.is_valid() and formset.is_valid()):
            screen = screen_form.save()
            rear_cam = rear_cam_form.save()
            front_cam = front_cam_form.save()
            storage = storage_form.save()
            os = os_form.save()
            connect = connect_form.save()
            battery = battery_form.save()
            util = util_form.save()

            phone_form.instance.phoneScreen = screen
            phone_form.instance.rearCameras = rear_cam
            phone_form.instance.frontCamera = front_cam
            phone_form.instance.phoneStorage = storage
            phone_form.instance.osCpuGpu = os
            phone_form.instance.phoneConnections = connect
            phone_form.instance.battery = battery
            phone_form.instance.utilities = util
            phone = phone_form.save()

            for form in formset.cleaned_data:
                if form:
                    print(form['src'])
                    src = form['src']
                    photo = PhoneImage(mobilePhone=phone, src=src)
                    photo.save()
            messages.success(request, "Lưu thành công")
        else:
            print(phone_form.errors, screen_form.errors, rear_cam_form.errors, front_cam_form.errors,
                  storage_form.errors, os_form.errors, connect_form.errors, battery_form.errors, util_form.errors,
                  formset.errors)
            messages.error(request, "Lưu không thành công")
        return HttpResponseRedirect('/mobilephone/addPhone')


class AddCamFeature(View):

    def get(self, request):
        cam_feat_form = CamFeatureForm
        return render(request, 'mobilephone/add_cam_feature.html', {'form': cam_feat_form})

    def post(self, request):
        cam_feat_form = CamFeatureForm(request.POST)
        if cam_feat_form.is_valid():
            cam_feat_form.save()
            messages.success(request, "Lưu thành công")
        else:
            print(cam_feat_form.errors)
            messages.error(request, "Lưu không thành công")
        return HttpResponseRedirect('/mobilephone/addPhone')


class AddAudioFormat(View):

    def get(self, request):
        audio_format_form = AudioFormatForm
        return render(request, 'mobilephone/add_audio_format.html', {'form': audio_format_form})

    def post(self, request):
        audio_format_form = AudioFormatForm(request.POST)
        if audio_format_form.is_valid():
            audio_format_form.save()
            messages.success(request, "Lưu thành công")
        else:
            print(audio_format_form.errors)
            messages.error(request, "Lưu không thành công")
        return HttpResponseRedirect('/mobilephone/addPhone')


class AddVideoFormat(View):

    def get(self, request):
        video_format_form = VideoFormatForm
        return render(request, 'mobilephone/add_video_format.html', {'form': video_format_form})

    def post(self, request):
        video_format_form = VideoFormatForm(request.POST)
        if video_format_form.is_valid():
            video_format_form.save()
            messages.success(request, "Lưu thành công")
        else:
            print(video_format_form.errors)
            messages.error(request, "Lưu không thành công")
        return HttpResponseRedirect('/mobilephone/addPhone')


class AddSpecialFeat(View):

    def get(self, request):
        special_feat_form = SpecialFeatForm
        return render(request, 'mobilephone/add_special_feat.html', {'form': special_feat_form})

    def post(self, request):
        special_feat_form = SpecialFeatForm(request.POST)
        if special_feat_form.is_valid():
            special_feat_form.save()
            messages.success(request, "Lưu thành công")
        else:
            print(special_feat_form.errors)
            messages.error(request, "Lưu không thành công")
        return HttpResponseRedirect('/mobilephone/addPhone')


class AddRecordingRes(View):

    def get(self, request):
        record_res_form = RecordingResForm
        return render(request, 'mobilephone/add_recording_res.html', {'form': record_res_form})

    def post(self, request):
        record_res_form = RecordingResForm(request.POST)
        if record_res_form.is_valid():
            record_res_form.save()
            messages.success(request, "Lưu thành công")
        else:
            print(record_res_form.errors)
            messages.error(request, "Lưu không thành công")
        return HttpResponseRedirect('/mobilephone/addPhone')


class AddWifiTech(View):

    def get(self, request):
        wifi_form = WifiTechForm
        return render(request, 'mobilephone/add_wifi_tech.html', {'form': wifi_form})

    def post(self, request):
        wifi_form = WifiTechForm(request.POST)
        if wifi_form.is_valid():
            wifi_form.save()
            messages.success(request, "Lưu thành công")
        else:
            print(wifi_form.errors)
            messages.error(request, "Lưu không thành công")
        return HttpResponseRedirect('/mobilephone/addPhone')


class AddGpsTech(View):

    def get(self, request):
        gps_form = GpsTechForm
        return render(request, 'mobilephone/add_gps_tech.html', {'form': gps_form})

    def post(self, request):
        gps_form = GpsTechForm(request.POST)
        if gps_form.is_valid():
            gps_form.save()
            messages.success(request, "Lưu thành công")
        else:
            print(gps_form.errors)
            messages.error(request, "Lưu không thành công")
        return HttpResponseRedirect('/mobilephone/addPhone')


class AddBluetoothTech(View):

    def get(self, request):
        bluetooth_form = BluetoothTechForm
        return render(request, 'mobilephone/add_bluetooth_tech.html', {'form': bluetooth_form})

    def post(self, request):
        bluetooth_form = BluetoothTechForm(request.POST)
        if bluetooth_form.is_valid():
            bluetooth_form.save()
            messages.success(request, "Lưu thành công")
        else:
            print(bluetooth_form.errors)
            messages.error(request, "Lưu không thành công")
        return HttpResponseRedirect('/mobilephone/addPhone')


class AddChargerTech(View):

    def get(self, request):
        charger_form = ChargerTechForm
        return render(request, 'mobilephone/add_charger_tech.html', {'form': charger_form})

    def post(self, request):
        charger_form = ChargerTechForm(request.POST)
        if charger_form.is_valid():
            charger_form.save()
            messages.success(request, "Lưu thành công")
        else:
            print(charger_form.errors)
            messages.error(request, "Lưu không thành công")
        return HttpResponseRedirect('/mobilephone/addPhone')


class AddHeadphoneTech(View):

    def get(self, request):
        headphone_form = HeadphoneTechForm
        return render(request, 'mobilephone/add_headphone_tech.html', {'form': headphone_form})

    def post(self, request):
        headphone_form = HeadphoneTechForm(request.POST)
        if headphone_form.is_valid():
            headphone_form.save()
            messages.success(request, "Lưu thành công")
        else:
            print(headphone_form.errors)
            messages.error(request, "Lưu không thành công")
        return HttpResponseRedirect('/mobilephone/addPhone')


class AddBatteryTech(View):

    def get(self, request):
        battery_tech_form = BatteryTechForm
        return render(request, 'mobilephone/add_battery_tech.html', {'form': battery_tech_form})

    def post(self, request):
        battery_tech_form = BatteryTechForm(request.POST)
        if battery_tech_form.is_valid():
            battery_tech_form.save()
            messages.success(request, "Lưu thành công")
        else:
            print(battery_tech_form.errors)
            messages.error(request, "Lưu không thành công")
        return HttpResponseRedirect('/mobilephone/addPhone')
