from django.db import models

# Create your models here.


class ClothesImage(models.Model):
    src = models.ImageField(upload_to='clothes')
    clothes = models.ForeignKey('Clothes', on_delete=models.CASCADE)

    def __str__(self):
        return self.clothes.name


class Clothes(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=20)
    color = models.CharField(max_length=10)
    releaseDate = models.CharField(max_length=50)
    material = models.CharField(max_length=20)
    department = models.CharField(max_length=10)
    size = models.CharField(max_length=5)
    sizeCountry = models.CharField(max_length=10)
    washingType = models.CharField(max_length=10)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    fitType = models.CharField(max_length=10)
    closureType = models.CharField(max_length=10)
    dimensions = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class TShirt(Clothes):
    tagFree = models.BooleanField()
    layFlat = models.BooleanField()
    sleeveHem = models.CharField(max_length=10)
    moistureWicking = models.BooleanField()
    tapedNeck = models.BooleanField()
    bottomHem = models.CharField(max_length=10)


class Jeans(Clothes):
    waist = models.CharField(max_length=10)
    frontRise = models.CharField(max_length=10)
    backRise = models.CharField(max_length=10)
    upperThigh = models.CharField(max_length=10)
    inseam = models.CharField(max_length=10)
    legOpening = models.CharField(max_length=10)
    pocketNumber = models.IntegerField()


class Shorts(Clothes):
    pocketNumber = models.IntegerField()
    moistureWicking = models.BooleanField()
    breathable = models.BooleanField()
    type = models.CharField(max_length=10)
    inseam = models.CharField(max_length=10)
    outseam = models.CharField(max_length=10)


class ClothesItem(models.Model):
    price = models.IntegerField()
    discount = models.DecimalField(max_digits=3, decimal_places=2)
    forSale = models.BooleanField()
    inventory = models.IntegerField()
    clothes = models.ForeignKey(Clothes, on_delete=models.CASCADE)

    def __str__(self):
        return self.clothes.name
