# Generated by Django 3.2.8 on 2021-12-28 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0005_alter_profile_birth_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='imagen',
            field=models.ImageField(default='default.jpeg', upload_to='profile_pics'),
        ),
    ]