# Generated by Django 4.2 on 2023-04-26 06:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('redMap', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BloodDonor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hometown', models.CharField(max_length=100)),
                ('province', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='BloodMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='redMap.blooddonor')),
            ],
        ),
        migrations.CreateModel(
            name='BloodPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='photos')),
                ('caption', models.CharField(blank=True, max_length=100, null=True)),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='redMap.blooddonor')),
            ],
        ),
        migrations.CreateModel(
            name='BloodRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('volume', models.FloatField()),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='redMap.blooddonor')),
            ],
        ),
        migrations.AlterModelOptions(
            name='redmapuser',
            options={'verbose_name': 'user', 'verbose_name_plural': 'user'},
        ),
        migrations.AlterField(
            model_name='redmapuser',
            name='email',
            field=models.EmailField(max_length=255, unique=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='redmapuser',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='phone_number'),
        ),
        migrations.DeleteModel(
            name='Donor',
        ),
        migrations.AddField(
            model_name='blooddonor',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='donor', to=settings.AUTH_USER_MODEL),
        ),
    ]
