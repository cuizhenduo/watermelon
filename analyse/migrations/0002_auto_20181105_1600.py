# Generated by Django 2.0.4 on 2018-11-05 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyse', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hisdata',
            name='Air_humidity',
            field=models.DecimalField(decimal_places=13, max_digits=18, verbose_name='空气湿度//℃'),
        ),
        migrations.AlterField(
            model_name='hisdata',
            name='Air_temperature',
            field=models.DecimalField(decimal_places=13, max_digits=18, verbose_name='空气温度//℃'),
        ),
        migrations.AlterField(
            model_name='hisdata',
            name='Light_intensity',
            field=models.DecimalField(decimal_places=13, max_digits=18, verbose_name='光照强度（单位lux）'),
        ),
        migrations.AlterField(
            model_name='hisdata',
            name='Soil_moisture',
            field=models.DecimalField(decimal_places=13, max_digits=18, verbose_name='土壤水分//℃'),
        ),
        migrations.AlterField(
            model_name='hisdata',
            name='Soil_temperature',
            field=models.DecimalField(decimal_places=13, max_digits=18, verbose_name='土壤温度//℃'),
        ),
    ]
