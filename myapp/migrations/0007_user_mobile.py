# Generated by Django 4.0.3 on 2022-03-26 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_rename_users_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='mobile',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
