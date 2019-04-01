# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
# Register your models here.
from analyse.models import PlantRange,PlantData

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('DataKind',)

class dataAdmin(admin.ModelAdmin):
    list_display = ('Season',)
admin.site.register(PlantData,dataAdmin)

admin.site.register(PlantRange,ArticleAdmin)
class MyAdminSite(admin.AdminSite):
    site_header = '设施西瓜远程监控系统'  # 此处设置页面显示标题
    site_title = '西瓜'  # 此处设置页面头部标题


admin_site = MyAdminSite(name='management')
admin.site.site_header = '设施西瓜远程监控系统'
admin.site.site_title = '西瓜'