from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    phone = models.CharField(max_length=255, null=True, blank=True)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'


class Categories(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Amenities(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Apartments(models.Model):
    sts = (
        ('sale', 'sale'),
        ('rent', 'rent'),
    )
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='apart_user')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='apart_cat')
    address = models.CharField(max_length=255)
    status = models.CharField(choices=sts, max_length=4, default='rent')
    area = models.SmallIntegerField(default=0)
    rooms = models.SmallIntegerField(default=0)
    bathrooms = models.SmallIntegerField(default=0)
    bedrooms = models.SmallIntegerField(default=0)
    garages = models.SmallIntegerField(default=0)
    floor = models.SmallIntegerField(default=0)
    building_floor = models.SmallIntegerField(default=0)
    description = models.TextField(max_length=900)
    amenities = models.ManyToManyField(Amenities,blank=True)

    def __str__(self):
        return self.address


class PicturesOfApart(models.Model):
    apartment = models.ForeignKey(Apartments, on_delete=models.CASCADE, related_name='pic_apart')
    image = models.ImageField(upload_to='picture')

    def __str__(self):
        return str(self.apartment)