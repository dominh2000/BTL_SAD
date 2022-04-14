from django.db import models

# Create your models here.


class PhoneScreen(models.Model):
    technology = models.CharField(max_length=100)
    resolution = models.CharField(max_length=100)
    diagonal = models.CharField(max_length=10)
    refreshRate = models.CharField(max_length=10)
    brightness = models.CharField(max_length=30)
    glass = models.CharField(max_length=50)


class CameraFeature(models.Model):
    feature = models.CharField(max_length=256)

    def __str__(self):
        return self.feature


class RecordingResolution(models.Model):
    recordResolution = models.CharField(max_length=100)

    def __str__(self):
        return self.recordResolution


class RearCameras(models.Model):
    rearResolution = models.CharField(max_length=100)
    flash = models.BooleanField(default=True)
    rearRecordingRes = models.ManyToManyField(RecordingResolution)
    rearFeatures = models.ManyToManyField(CameraFeature)


class FrontCamera(models.Model):
    frontResolution = models.CharField(max_length=100)
    frontRecordingRes = models.ManyToManyField(RecordingResolution)
    frontFeatures = models.ManyToManyField(CameraFeature)


class PhoneStorage(models.Model):
    ram = models.CharField(max_length=10)
    internalMem = models.CharField(max_length=10)
    internalMemAvail = models.CharField(max_length=10)
    memoryCard = models.CharField(max_length=100, default='')
    contacts = models.CharField(max_length=50)


class OsCpuGpu(models.Model):
    os = models.CharField(max_length=30)
    cpu = models.CharField(max_length=30)
    cpuDescription = models.CharField(max_length=256)
    gpu = models.CharField(max_length=30)


class WifiTech(models.Model):
    tech = models.CharField(max_length=100)

    def __str__(self):
        return self.tech


class GpsTech(models.Model):
    tech = models.CharField(max_length=100)

    def __str__(self):
        return self.tech


class BluetoothTech(models.Model):
    tech = models.CharField(max_length=100)

    def __str__(self):
        return self.tech


class ChargerTech(models.Model):
    tech = models.CharField(max_length=50)

    def __str__(self):
        return self.tech


class HeadphoneTech(models.Model):
    tech = models.CharField(max_length=50)

    def __str__(self):
        return self.tech


class PhoneConnections(models.Model):
    cellularNetwork = models.CharField(max_length=30)
    sim = models.CharField(max_length=256)
    wifi = models.ManyToManyField(WifiTech)
    gps = models.ManyToManyField(GpsTech)
    bluetooth = models.ManyToManyField(BluetoothTech)
    charger = models.ForeignKey(ChargerTech, on_delete=models.CASCADE)
    headphone = models.ManyToManyField(HeadphoneTech)
    others = models.CharField(max_length=256)


class BatteryTech(models.Model):
    tech = models.CharField(max_length=100)

    def __str__(self):
        return self.tech


class Battery(models.Model):
    capacity = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    maxWattage = models.CharField(max_length=10)
    providedWattage = models.CharField(max_length=10, default='')
    technologies = models.ManyToManyField(BatteryTech)


class AudioFormat(models.Model):
    format = models.CharField(max_length=25)

    def __str__(self):
        return self.format


class SpecialFeature(models.Model):
    feature = models.CharField(max_length=255)

    def __str__(self):
        return self.feature


class VideoFormat(models.Model):
    format = models.CharField(max_length=25)

    def __str__(self):
        return self.format


class Utilities(models.Model):
    advancedSecurities = models.CharField(max_length=256)
    resistances = models.CharField(max_length=50)
    recorder = models.CharField(max_length=50)
    audioFormats = models.ManyToManyField(AudioFormat)
    specialFeatures = models.ManyToManyField(SpecialFeature)
    videoFormats = models.ManyToManyField(VideoFormat)


class PhoneImage(models.Model):
    src = models.ImageField(upload_to='mobilephone/')
    mobilePhone = models.ForeignKey('MobilePhone', on_delete=models.CASCADE)

    def __str__(self):
        return self.mobilePhone.name


class MobilePhone(models.Model):
    name = models.CharField(max_length=30)
    designType = models.CharField(max_length=50)
    material = models.CharField(max_length=50)
    dimensions = models.CharField(max_length=50)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    releaseDate = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50)
    speaker = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    phoneScreen = models.OneToOneField(PhoneScreen, on_delete=models.CASCADE)
    rearCameras = models.OneToOneField(RearCameras, on_delete=models.CASCADE)
    phoneStorage = models.OneToOneField(PhoneStorage, on_delete=models.CASCADE)
    frontCamera = models.OneToOneField(FrontCamera, on_delete=models.CASCADE)
    phoneConnections = models.OneToOneField(PhoneConnections, on_delete=models.CASCADE)
    battery = models.OneToOneField(Battery, on_delete=models.CASCADE)
    utilities = models.OneToOneField(Utilities, on_delete=models.CASCADE)
    osCpuGpu = models.OneToOneField(OsCpuGpu, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class MobilePhoneItem(models.Model):
    price = models.IntegerField()
    discount = models.DecimalField(max_digits=3, decimal_places=2)
    forSale = models.BooleanField()
    inventory = models.IntegerField()
    mobilePhone = models.ForeignKey(MobilePhone, on_delete=models.CASCADE)

    def __str__(self):
        return self.mobilePhone.name
