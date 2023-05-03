from django.db import models
from django.contrib.auth.models import AbstractUser
from redMap.models import RedMapUser

# Create your models here.
class Question(models.Model):
    CATEGORY_CHOICES = (
        ('computer', '计算机基础知识'),
        ('blood', '献血基础知识'),
        ('party', '基础党史'),
    )
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=20, verbose_name='问题分类')
    text = models.TextField(verbose_name='问题内容')
    option_a = models.CharField(max_length=255, verbose_name='选项A', blank=True)
    option_b = models.CharField(max_length=255, verbose_name='选项B', blank=True)
    option_c = models.CharField(max_length=255, verbose_name='选项C', blank=True)
    option_d = models.CharField(max_length=255, verbose_name='选项D', blank=True)
    answer = models.CharField(max_length=1, choices=(('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')), verbose_name='正确答案')

class Record(models.Model):
    user = models.ForeignKey(RedMapUser, on_delete=models.CASCADE, verbose_name='用户')
    date = models.DateField(verbose_name='日期', auto_now=True)
    score = models.IntegerField(verbose_name='分数')

class Profile(models.Model):
    user = models.OneToOneField(RedMapUser, on_delete=models.CASCADE, verbose_name='用户')
    blood_bags = models.IntegerField(verbose_name='血包容量', default=0)
    last_quiz_date = models.DateField(verbose_name='最后一次答题日期', null=True, blank=True)

