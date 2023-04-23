from django.db import models
from redMap.models import RedMapUser

# Create your models here.

class Gift(models.Model):
    """礼物模型"""
    name = models.CharField(max_length=50, verbose_name='礼物名称')
    image = models.ImageField(upload_to='gifts/', verbose_name='礼物图片')
    description = models.TextField(verbose_name='礼物描述')

    class Meta:
        verbose_name = '礼物'
        verbose_name_plural = '礼物'

    def __str__(self):
        return self.name


class Message(models.Model):
    """漂流瓶留言模型"""
    content = models.TextField(verbose_name='留言内容')
    sender = models.ForeignKey(RedMapUser, on_delete=models.CASCADE, related_name='sent_messages', verbose_name='发送者')
    receiver = models.ForeignKey(RedMapUser, on_delete=models.CASCADE, related_name='received_messages', verbose_name='接收者')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '漂流瓶留言'
        verbose_name_plural = '漂流瓶留言'

    def __str__(self):
        return f'{self.sender.username} -> {self.receiver.username}: {self.content}'


class GiftRecord(models.Model):
    """礼物记录模型"""
    gift = models.ForeignKey(Gift, on_delete=models.CASCADE, verbose_name='礼物')
    sender = models.ForeignKey(RedMapUser, on_delete=models.CASCADE, related_name='sent_gifts', verbose_name='发送者')
    receiver = models.ForeignKey(RedMapUser, on_delete=models.CASCADE, related_name='received_gifts', verbose_name='接收者')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='留言')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '礼物记录'
        verbose_name_plural = '礼物记录'

    def __str__(self):
        return f'{self.sender.username} -> {self.receiver.username}: {self.gift.name}'
