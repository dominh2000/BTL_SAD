from django.db import models

# Create your models here.


class ElectronicsImage(models.Model):
    src = models.ImageField(upload_to='electronics')
    electronics = models.ForeignKey('Electronics', on_delete=models.CASCADE)

    def __str__(self):
        return self.electronics.name


class Electronics(models.Model):
    name = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=20)
    releaseDate = models.CharField(max_length=50)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    dimensions = models.CharField(max_length=100)
    color = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Hairdryer(Electronics):
    hairType = models.CharField(max_length=10)
    wattage = models.CharField(max_length=10)
    voltage = models.CharField(max_length=10)
    speedSettings = models.IntegerField()
    heatSettings = models.IntegerField()


class ElectronicsItem(models.Model):
    price = models.IntegerField()
    discount = models.DecimalField(max_digits=3, decimal_places=2)
    forSale = models.BooleanField()
    inventory = models.IntegerField()
    electronics = models.ForeignKey(Electronics, on_delete=models.CASCADE)

    def __str__(self):
        return self.electronics.name