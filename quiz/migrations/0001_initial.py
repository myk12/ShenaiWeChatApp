# Generated by Django 4.2 on 2023-04-21 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('computer', '计算机基础'), ('blood', '献血基础'), ('party', '基础党史')], max_length=50, verbose_name='题目类别')),
                ('text', models.CharField(max_length=255, verbose_name='问题')),
                ('option1', models.CharField(max_length=255, verbose_name='选项1')),
                ('option2', models.CharField(max_length=255, verbose_name='选项2')),
                ('option3', models.CharField(max_length=255, verbose_name='选项3')),
                ('option4', models.CharField(max_length=255, verbose_name='选项4')),
                ('answer', models.IntegerField(choices=[(1, '选项1'), (2, '选项2'), (3, '选项3'), (4, '选项4')], verbose_name='答案')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='用户名')),
                ('energy', models.IntegerField(default=0, verbose_name='能量值')),
            ],
        ),
    ]
