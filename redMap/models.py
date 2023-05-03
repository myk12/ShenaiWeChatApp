from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.

class RedMapUser(AbstractUser):
    phone = models.CharField(max_length=20, verbose_name='phone_number')
    email = models.EmailField(max_length=255, unique=True, verbose_name='email')

    class Meta:
        db_table = 'user'
        verbose_name = 'user'
        verbose_name_plural = verbose_name
 
class BloodDonor(models.Model):
    user = models.OneToOneField(RedMapUser, on_delete=models.CASCADE, related_name='donor')
    hometown = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

class BloodRecord(models.Model):
    donor = models.ForeignKey(BloodDonor, on_delete=models.CASCADE, related_name='records')
    datetime = models.DateTimeField(auto_now_add=True)
    volume = models.FloatField()

class BloodPhoto(models.Model):
    donor = models.ForeignKey(BloodDonor, on_delete=models.CASCADE, related_name='photos')
    photo = models.ImageField(upload_to='photos')
    caption = models.CharField(max_length=100, blank=True, null=True)

class BloodMessage(models.Model):
    donor = models.ForeignKey(BloodDonor, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
