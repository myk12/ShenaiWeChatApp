from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.

class RedMapUser(AbstractUser):
    phone = models.CharField(max_length=20, verbose_name='手机号码')
    email = models.EmailField(max_length=255, unique=True, verbose_name='邮箱')

    class Meta:
        db_table = 'user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

class Donor(models.Model):
    GENDER_CHOICES = (
        ('M', '男性'),
        ('F', '女性'),
    )

    STATUS_CHOICES = (
        ('A', '待审核'),
        ('P', '审核通过'),
        ('F', '审核失败'),
    )

    user = models.ForeignKey(RedMapUser, on_delete=models.CASCADE, verbose_name='用户ID')
    name = models.CharField(max_length=20, verbose_name='姓名')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name='性别')
    age = models.IntegerField(verbose_name='年龄')
    photo = models.ImageField(upload_to='donor_photos/', verbose_name='照片')
    location = models.CharField(max_length=50, verbose_name='所在地区')
    center = models.CharField(max_length=50, verbose_name='献血中心')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='A', verbose_name='献血状态')
    times = models.IntegerField(default=0, verbose_name='献血次数')
    last_time = models.DateTimeField(default=timezone.now, verbose_name='上次献血时间')

    class Meta:
        db_table = 'donor'
        verbose_name = '献血者'
        verbose_name_plural = verbose_name
