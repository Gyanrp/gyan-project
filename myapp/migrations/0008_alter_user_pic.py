# Generated by Django 4.0.3 on 2022-03-27 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_user_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pic',
            field=models.ImageField(default='avtar.png', upload_to='Profile Pic'),
        ),
    ]
