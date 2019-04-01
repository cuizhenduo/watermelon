# Generated by Django 2.0.4 on 2018-11-12 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyse', '0005_auto_20181112_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantrange',
            name='ChengshuTimeH',
            field=models.DecimalField(decimal_places=0, max_digits=18, verbose_name='成熟期高'),
        ),
        migrations.AlterField(
            model_name='plantrange',
            name='ChengshuTimeL',
            field=models.DecimalField(decimal_places=0, max_digits=18, verbose_name='成熟期低'),
        ),
        migrations.AlterField(
            model_name='plantrange',
            name='HuanmiaoTimeH',
            field=models.DecimalField(decimal_places=0, max_digits=18, verbose_name='缓苗期高'),
        ),
        migrations.AlterField(
            model_name='plantrange',
            name='HuanmiaoTimeL',
            field=models.DecimalField(decimal_places=0, max_digits=18, verbose_name='缓苗期低'),
        ),
        migrations.AlterField(
            model_name='plantrange',
            name='PengguaTimeH',
            field=models.DecimalField(decimal_places=0, max_digits=18, verbose_name='澎瓜期高'),
        ),
        migrations.AlterField(
            model_name='plantrange',
            name='PengguaTimeL',
            field=models.DecimalField(decimal_places=0, max_digits=18, verbose_name='澎瓜期低'),
        ),
        migrations.AlterField(
            model_name='plantrange',
            name='ShenmanTimeH',
            field=models.DecimalField(decimal_places=0, max_digits=18, verbose_name='伸蔓期高'),
        ),
        migrations.AlterField(
            model_name='plantrange',
            name='ShenmanTimeL',
            field=models.DecimalField(decimal_places=0, max_digits=18, verbose_name='伸蔓期低'),
        ),
        migrations.AlterField(
            model_name='plantrange',
            name='ZuoguoTimeH',
            field=models.DecimalField(decimal_places=0, max_digits=18, verbose_name='坐果期高'),
        ),
        migrations.AlterField(
            model_name='plantrange',
            name='ZuoguoTimeL',
            field=models.DecimalField(decimal_places=0, max_digits=18, verbose_name='坐果期低'),
        ),
    ]
