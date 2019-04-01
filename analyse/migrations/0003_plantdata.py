# Generated by Django 2.0.4 on 2018-11-12 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyse', '0002_auto_20181105_1600'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlantData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Season', models.CharField(max_length=32, verbose_name='西瓜季节')),
                ('HuanmiaoTimeS', models.DateField(verbose_name='缓苗期始')),
                ('HuanmiaoTimeE', models.DateField(verbose_name='缓苗期终')),
                ('ShenmanTimeS', models.DateField(verbose_name='伸蔓期始')),
                ('ShenmanTimeE', models.DateField(verbose_name='伸蔓期终')),
                ('ZuoguoTimeS', models.DateField(verbose_name='坐果期始')),
                ('ZuoguoTimeE', models.DateField(verbose_name='坐果期终')),
                ('PengguaTimeS', models.DateField(verbose_name='澎瓜期始')),
                ('PengguaTimeE', models.DateField(verbose_name='澎瓜期终')),
                ('ChengshuTimeS', models.DateField(verbose_name='成熟期始')),
                ('ChengshuTimeE', models.DateField(verbose_name='成熟期终')),
            ],
            options={
                'verbose_name': '西瓜季节',
                'verbose_name_plural': '西瓜季节',
            },
        ),
    ]