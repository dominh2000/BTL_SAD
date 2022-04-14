from django.db import models

# Create your models here.


class LaptopImage(models.Model):
    src = models.ImageField(upload_to='laptop/')
    laptop = models.ForeignKey('Laptop', on_delete=models.CASCADE)

    def __str__(self):
        return self.laptop.name


class Dimensions(models.Model):
    dimensions = models.CharField(max_length=256)
    weight = models.DecimalField(max_digits=4, decimal_places=2)
    material = models.CharField(max_length=100, default='')


class PhysicalInterface(models.Model):
    interface = models.CharField(max_length=256)

    def __str__(self):
        return self.interface


class WirelessTech(models.Model):
    tech = models.CharField(max_length=50)

    def __str__(self):
        return self.tech


class OtherFeatures(models.Model):
    feature = models.CharField(max_length=100)

    def __str__(self):
        return self.feature


class LaptopInterfaces(models.Model):
    wirelessConnection = models.ManyToManyField(WirelessTech)
    webcam = models.CharField(max_length=100)
    otherFeat = models.ManyToManyField(OtherFeatures)
    memoryCard = models.CharField(max_length=50, default='Micro SD')
    keyboardLight = models.BooleanField(default=False)
    interfaces = models.ManyToManyField(PhysicalInterface)


class SoundTech(models.Model):
    tech = models.CharField(max_length=100)

    def __str__(self):
        return self.tech


class AudioVideo(models.Model):
    gpu = models.CharField(max_length=256)
    soundTechnologies = models.ManyToManyField(SoundTech)


class ScreenTechnology(models.Model):
    tech = models.CharField(max_length=100)

    def __str__(self):
        return self.tech


class LaptopScreen(models.Model):
    diagonal = models.CharField(max_length=10)
    resolution = models.CharField(max_length=20)
    refreshRate = models.CharField(max_length=10)
    touchable = models.BooleanField(default=False)
    technology = models.ManyToManyField(ScreenTechnology)


class LaptopStorage(models.Model):
    ramSize = models.CharField(max_length=10)
    ramType = models.CharField(max_length=100)
    busRamSpeed = models.CharField(max_length=10)
    maxSize = models.CharField(max_length=50)
    secondary = models.CharField(max_length=256)


class Cpu(models.Model):
    cpuName = models.CharField(primary_key=True, max_length=20)
    family = models.CharField(max_length=10, default='')
    cores = models.IntegerField()
    threads = models.IntegerField()
    baseSpeed = models.CharField(max_length=20)
    maxSpeed = models.CharField(max_length=10)
    l3Cache = models.CharField(max_length=30)
    manufacturer = models.CharField(max_length=10)

    def __str__(self):
        return self.cpuName


class Laptop(models.Model):
    name = models.CharField(max_length=100)
    batteryCapacity = models.CharField(max_length=50)
    os = models.CharField(max_length=50)
    bundledSoftwares = models.CharField(max_length=256, default='')
    releaseDate = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    cpu = models.ForeignKey(Cpu, on_delete=models.CASCADE)
    laptopStorage = models.OneToOneField(LaptopStorage, on_delete=models.CASCADE)
    laptopScreen = models.OneToOneField(LaptopScreen, on_delete=models.CASCADE)
    audioVideo = models.OneToOneField(AudioVideo, on_delete=models.CASCADE)
    laptopInterfaces = models.OneToOneField(LaptopInterfaces, on_delete=models.CASCADE)
    dimensions = models.OneToOneField(Dimensions, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class LaptopItem(models.Model):
    price = models.IntegerField()
    discount = models.DecimalField(max_digits=3, decimal_places=2)
    forSale = models.BooleanField()
    inventory = models.IntegerField()
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE)

    def __str__(self):
        return self.laptop.name
