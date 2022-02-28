# Generated by Django 3.2.8 on 2021-12-26 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Address (Street address, City, State/Region, Country, Postal Code)'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(blank=True, default='', verbose_name='Date of Birth'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_tin',
            field=models.PositiveIntegerField(blank=True, default='', verbose_name='Taxpayer Identification Number'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='tax_country',
            field=models.CharField(blank=True, default='', max_length=80, verbose_name='Tax country'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='tax_state',
            field=models.CharField(blank=True, default='', max_length=80, verbose_name='Tax State (tax state for US persons only)'),
        ),
    ]
