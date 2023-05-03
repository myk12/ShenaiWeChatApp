# Generated by Django 4.2 on 2023-04-23 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='礼物名称')),
                ('image', models.ImageField(upload_to='gifts/', verbose_name='礼物图片')),
                ('description', models.TextField(verbose_name='礼物描述')),
            ],
            options={
                'verbose_name': '礼物',
                'verbose_name_plural': '礼物',
            },
        ),
        migrations.CreateModel(
            name='GiftRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '礼物记录',
                'verbose_name_plural': '礼物记录',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='留言内容')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '漂流瓶留言',
                'verbose_name_plural': '漂流瓶留言',
            },
        ),
    ]