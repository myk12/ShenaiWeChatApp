# Generated by Django 4.2 on 2023-05-03 11:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('loveRelay', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bottle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_random', models.BooleanField(default=False)),
                ('is_sent', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterModelOptions(
            name='gift',
            options={},
        ),
        migrations.AlterModelOptions(
            name='message',
            options={},
        ),
        migrations.RemoveField(
            model_name='message',
            name='created_at',
        ),
        migrations.AddField(
            model_name='gift',
            name='price',
            field=models.FloatField(default=0, verbose_name='单价'),
        ),
        migrations.AddField(
            model_name='gift',
            name='remain_num',
            field=models.IntegerField(default=0, verbose_name='余量'),
        ),
        migrations.AlterField(
            model_name='gift',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='gift',
            name='image',
            field=models.ImageField(upload_to='gifts/'),
        ),
        migrations.AlterField(
            model_name='gift',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='message',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='GiftRecord',
        ),
        migrations.AddField(
            model_name='bottle',
            name='gift',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loveRelay.gift'),
        ),
        migrations.AddField(
            model_name='bottle',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loveRelay.message'),
        ),
        migrations.AddField(
            model_name='bottle',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_bottles', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bottle',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_bottles', to=settings.AUTH_USER_MODEL),
        ),
    ]
