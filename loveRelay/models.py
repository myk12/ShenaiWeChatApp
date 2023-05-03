from django.db import models
from django.utils import timezone
from redMap.models import RedMapUser
from datetime import datetime

# Create your models here.

class Gift(models.Model):
    name = models.CharField(max_length=50)
    remain_num = models.IntegerField(verbose_name='余量', default=0)
    price = models.FloatField(verbose_name='单价', default=0)
    image = models.ImageField(upload_to='gifts/')
    description = models.TextField()

    def __str__(self):
        return self.name


class Message(models.Model):
    content = models.TextField()
    sender = models.ForeignKey(RedMapUser, on_delete=models.CASCADE)
    receiver = models.ForeignKey(RedMapUser, on_delete=models.CASCADE, related_name='received_messages')
    #timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender.username} to {self.receiver.username}: {self.content}'


class Bottle(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    gift = models.ForeignKey(Gift, on_delete=models.CASCADE)
    is_random = models.BooleanField(default=False)
    is_sent = models.BooleanField(default=False)
    sender = models.ForeignKey(RedMapUser, on_delete=models.CASCADE, related_name='sent_bottles')
    receiver = models.ForeignKey(RedMapUser, on_delete=models.CASCADE, related_name='received_bottles')
    #timestamp = models.DateTimeField(auto_now_add=True, default=timezone.now)

    def __str__(self):
        return f'{self.sender.username} to {self.receiver.username}: {self.message.content} ({self.gift.name})'