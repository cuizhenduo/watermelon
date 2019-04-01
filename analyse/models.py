# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class HisData(models.Model):
    Light_intensity = models.DecimalField('光照强度（单位lux）',max_digits=18, decimal_places=13)
    Air_temperature = models.DecimalField('空气温度//℃',max_digits=18, decimal_places=13)
    Air_humidity = models.DecimalField('空气湿度//%', max_digits=18, decimal_places=13)
    Soil_moisture = models.DecimalField('土壤水分//vol%', max_digits=18, decimal_places=13)
    Soil_temperature = models.DecimalField('土壤温度//℃', max_digits=18, decimal_places=13)
    Time = models.DateTimeField('时间', auto_now=True)
    class Meta:
        verbose_name = '数据'
        verbose_name_plural = '数据'
    def __unicode__(self):
        return self.Time

class PlantRange(models.Model):
    DataKind = models.CharField('数据类型',max_length=32)
    HuanmiaoTimeH = models.DecimalField('缓苗期高', max_digits=18, decimal_places=0)
    HuanmiaoTimeL = models.DecimalField('缓苗期低', max_digits=18, decimal_places=0)
    ShenmanTimeH = models.DecimalField('伸蔓期高', max_digits=18, decimal_places=0)
    ShenmanTimeL = models.DecimalField('伸蔓期低', max_digits=18, decimal_places=0)
    ZuoguoTimeH = models.DecimalField('坐果期高', max_digits=18, decimal_places=0)
    ZuoguoTimeL = models.DecimalField('坐果期低', max_digits=18, decimal_places=0)
    PengguaTimeH = models.DecimalField('澎瓜期高', max_digits=18, decimal_places=0)
    PengguaTimeL = models.DecimalField('澎瓜期低', max_digits=18, decimal_places=0)
    ChengshuTimeH = models.DecimalField('成熟期高', max_digits=18, decimal_places=0)
    ChengshuTimeL = models.DecimalField('成熟期低', max_digits=18, decimal_places=0)

    class Meta:
        verbose_name = '数据类型'
        verbose_name_plural = '数据类型'
    def __unicode__(self):
        return self.DataKind

class PlantData(models.Model):
    Season = models.CharField('西瓜季节',max_length=32)
    HuanmiaoTimeS = models.DateField('缓苗期始', auto_now=False)
    HuanmiaoTimeE = models.DateField('缓苗期终', auto_now=False)
    ShenmanTimeS = models.DateField('伸蔓期始', auto_now=False)
    ShenmanTimeE = models.DateField('伸蔓期终', auto_now=False)
    ZuoguoTimeS = models.DateField('坐果期始', auto_now=False)
    ZuoguoTimeE = models.DateField('坐果期终', auto_now=False)
    PengguaTimeS = models.DateField('澎瓜期始', auto_now=False)
    PengguaTimeE = models.DateField('澎瓜期终', auto_now=False)
    ChengshuTimeS = models.DateField('成熟期始', auto_now=False)
    ChengshuTimeE = models.DateField('成熟期终', auto_now=False)

    class Meta:
        verbose_name = '西瓜季节'
        verbose_name_plural = '西瓜季节'
    def __unicode__(self):
        return self.Season