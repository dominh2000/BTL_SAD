from django.db import models

# Create your models here.


class ShoesImage(models.Model):
    src = models.ImageField(upload_to='shoes/')
    shoes = models.ForeignKey('Shoes', on_delete=models.CASCADE)

    def __str__(self):
        return self.shoes.name


class Shoes(models.Model):
    name = models.CharField(max_length=50)
    size = models.DecimalField(max_digits=3, decimal_places=1)
    sizeCountry = models.CharField(max_length=10)
    brand = models.CharField(max_length=10)
    color = models.CharField(max_length=10)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    releaseDate = models.CharField(max_length=50)
    department = models.CharField(max_length=10)
    upperMaterial = models.CharField(max_length=20)
    soleMaterial = models.CharField(max_length=20)
    liningMaterial = models.CharField(max_length=20)
    dimensions = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Sneaker(Shoes):
    nightReflect = models.BooleanField(default=True)
    heelHeight = models.CharField(max_length=10)


class BusinessShoes(Shoes):
    heelHeight = models.CharField(max_length=10)
    heelMeasure = models.CharField(max_length=10)


class RunningShoes(Shoes):
    nightReflect = models.BooleanField(default=True)
    durability = models.CharField(max_length=10)
    shockAbsorb = models.BooleanField(default=True)
    ventilation = models.CharField(max_length=10)
    ankleSupport = models.BooleanField(default=True)


class ShoesItem(models.Model):
    price = models.IntegerField()
    discount = models.DecimalField(max_digits=3, decimal_places=2)
    forSale = models.BooleanField()
    inventory = models.IntegerField()
    shoes = models.ForeignKey(Shoes, on_delete=models.CASCADE)

    def __str__(self):
        return self.shoes.name
