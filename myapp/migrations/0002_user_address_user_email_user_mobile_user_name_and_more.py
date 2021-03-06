# Generated by Django 4.0.3 on 2022-03-14 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='user',
            name='mobile',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='pic',
            field=models.FileField(default='avtar.png', null=True, upload_to='Profile Pic'),
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(default='Doctor', max_length=50, null=True),
        ),
    ]
