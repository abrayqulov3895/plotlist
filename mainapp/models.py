from django.db import models

# Create your models here.
class ImagePlace(models.Model):
    title = models.CharField(max_length=200,null=True)
    placeImage = models.ImageField()

class ImageCategory(models.Model):
    title = models.CharField(max_length=200,null=True)
    categoryImage = models.ImageField()

class ImageCountry(models.Model):
    title = models.CharField(max_length=200,null=True)
    countryImage = models.ImageField()

class TypeContact(models.Model):
    logo = models.ImageField()
    title = models.CharField(max_length=200,null=True)
    link = models.URLField()
class Country(models.Model):
    title = models.CharField(max_length=200,null=True)
    body = models.TextField()
    language = models.CharField(max_length=150,null=True)
    materik_list = []
    currency = models.CharField(max_length=200,null=True)
    materik = models.CharField(max_length=200,choices=materik_list)

class City(models.Model):
    title = models.CharField(max_length=200,null=True)
    body = models.TextField()
    country = models.ForeignKey(Country,on_delete=models.CASCADE)

class Category(models.Model):
    title = models.CharField(max_length=200,null=True)
    logo = models.ImageField()
    body = models.TextField()
    image = models.ForeignKey(ImageCategory,on_delete=models.CASCADE)


class Place(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    price = models.IntegerField()
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    # r_count = models.
    author = models.CharField(max_length=120)
    created_date = models.DateTimeField()
    update_date = models.DateTimeField()
    Image = models.ForeignKey(ImagePlace,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.title

