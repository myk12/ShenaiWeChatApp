from django.db import models
from django.contrib.auth.models import AbstractUser
from redMap.models import RedMapUser

# Create your models here.

class Question(models.Model):
    """
    问题模型
    """
    category_choices = [
        ('computer', '计算机基础'),
        ('blood', '献血基础'),
        ('party', '基础党史'),
    ]
    category = models.CharField(choices=category_choices, max_length=50, verbose_name="题目类别")
    text = models.CharField(max_length=255, verbose_name='问题')
    option1 = models.CharField(max_length=255, verbose_name='选项1')
    option2 = models.CharField(max_length=255, verbose_name='选项2')
    option3 = models.CharField(max_length=255, verbose_name='选项3')
    option4 = models.CharField(max_length=255, verbose_name='选项4')
    answer = models.IntegerField(choices=((1, '选项1'), (2, '选项2'), (3, '选项3'), (4, '选项4')), verbose_name='答案')

    def __str__(self):
        return self.text

class UserInfo(models.Model):
    user = models.ForeignKey(RedMapUser, on_delete=models.CASCADE, verbose_name='用户ID')
    energy = models.IntegerField(default=0, verbose_name='能量值')

    def __str__(self):
        return self.name

