"""watermelon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from analyse.views import his_data,test_chart,js_date,tem_date,hum_date,soilmoi_date,soiltem_date,js_date_month,plant_data,reset,reset_value,rect

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^hisdata/$',his_data),
    url(r'^test/$',test_chart),
    url(r'^datetime/$',js_date),
    url(r'^airtemtime/$',tem_date),
    url(r'^airhumtime/$',hum_date),
    url(r'^soilmoitime/$',soilmoi_date),
    url(r'^soiltemtime/$',soiltem_date),
    url(r'^montime/$',js_date_month),
    url(r'^plant/$',plant_data),
    url(r'^reset/$',reset),
    url(r'^resetvalue/$',reset_value),
    url(r'^rect/$',rect),
]

