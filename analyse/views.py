from django.shortcuts import render_to_response, render, redirect
from .models import HisData,PlantData,PlantRange
from django.http import HttpResponseRedirect,HttpResponse
import json
import datetime
# Create your views here.
def his_data(req):
    # 初始化
    response = []  #光照
    datetime = []  #日期
    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = HisData.objects.all()
    for var in list:
        response.append(float(var.Light_intensity))
        datetime.append(str(var.Time))
    return render_to_response("his_data.html",{'list':list,'lux': json.dumps(response),'dtime': json.dumps(datetime)})

def test_chart(req):
    return render_to_response("test.html")

def rect(req):
    if req.POST:
        #各个时期的日期
        Season = req.POST['season']
        HuanmiaoTimeS = req.POST['HuanmiaoTimeS']
        HuanmiaoTimeE = req.POST['HuanmiaoTimeE']
        ShenmanTimeS = req.POST['ShenmanTimeS']
        ShenmanTimeE = req.POST['ShenmanTimeE']
        ZuoguoTimeS = req.POST['ZuoguoTimeS']
        ZuoguoTimeE = req.POST['ZuoguoTimeE']
        PengguaTimeS = req.POST['PengguaTimeS']
        PengguaTimeE = req.POST['PengguaTimeE']
        ChengshuTimeS = req.POST['ChengshuTimeS']
        ChengshuTimeE = req.POST['ChengshuTimeE']
        test1 = PlantData.objects.get(id=1)
        test1.Season = Season
        test1.HuanmiaoTimeS = HuanmiaoTimeS
        test1.HuanmiaoTimeE = HuanmiaoTimeE
        test1.ShenmanTimeS = ShenmanTimeS
        test1.ShenmanTimeE = ShenmanTimeE
        test1.ZuoguoTimeS = ZuoguoTimeS
        test1.ZuoguoTimeE = ZuoguoTimeE
        test1.PengguaTimeS = PengguaTimeS
        test1.PengguaTimeE = PengguaTimeE
        test1.ChengshuTimeS = ChengshuTimeS
        test1.ChengshuTimeE = ChengshuTimeE
        test1.save()
        #光照强度
        LHuanmiaoTimeH = req.POST['LHuanmiaoTimeH']
        LHuanmiaoTimeL = req.POST['LHuanmiaoTimeL']
        LShenmanTimeH = req.POST['LShenmanTimeH']
        LShenmanTimeL = req.POST['LShenmanTimeL']
        LZuoguoTimeH = req.POST['LZuoguoTimeH']
        LZuoguoTimeL = req.POST['LZuoguoTimeL']
        LPengguaTimeH = req.POST['LPengguaTimeH']
        LPengguaTimeL = req.POST['LPengguaTimeL']
        LChengshuTimeH = req.POST['LChengshuTimeH']
        LChengshuTimeL = req.POST['LChengshuTimeL']
        testlight = PlantRange.objects.get(id=1)
        testlight.HuanmiaoTimeH = LHuanmiaoTimeH
        testlight.HuanmiaoTimeL = LHuanmiaoTimeL
        testlight.ShenmanTimeH = LShenmanTimeH
        testlight.ShenmanTimeL = LShenmanTimeL
        testlight.ZuoguoTimeH = LZuoguoTimeH
        testlight.ZuoguoTimeL = LZuoguoTimeL
        testlight.PengguaTimeH = LPengguaTimeH
        testlight.PengguaTimeL = LPengguaTimeL
        testlight.ChengshuTimeH = LChengshuTimeH
        testlight.ChengshuTimeL = LChengshuTimeL
        testlight.save()
        #空气温度
        ATHuanmiaoTimeH = req.POST['ATHuanmiaoTimeH']
        ATHuanmiaoTimeL = req.POST['ATHuanmiaoTimeL']
        ATShenmanTimeH = req.POST['ATShenmanTimeH']
        ATShenmanTimeL = req.POST['ATShenmanTimeL']
        ATZuoguoTimeH = req.POST['ATZuoguoTimeH']
        ATZuoguoTimeL = req.POST['ATZuoguoTimeL']
        ATPengguaTimeH = req.POST['ATPengguaTimeH']
        ATPengguaTimeL = req.POST['ATPengguaTimeL']
        ATChengshuTimeH = req.POST['ATChengshuTimeH']
        ATChengshuTimeL = req.POST['ATChengshuTimeL']
        testat = PlantRange.objects.get(id=2)
        testat.HuanmiaoTimeH = ATHuanmiaoTimeH
        testat.HuanmiaoTimeL = ATHuanmiaoTimeL
        testat.ShenmanTimeH = ATShenmanTimeH
        testat.ShenmanTimeL = ATShenmanTimeL
        testat.ZuoguoTimeH = ATZuoguoTimeH
        testat.ZuoguoTimeL = ATZuoguoTimeL
        testat.PengguaTimeH = ATPengguaTimeH
        testat.PengguaTimeL = ATPengguaTimeL
        testat.ChengshuTimeH = ATChengshuTimeH
        testat.ChengshuTimeL = ATChengshuTimeL
        testat.save()
        #空气湿度
        AHHuanmiaoTimeH = req.POST['AHHuanmiaoTimeH']
        AHHuanmiaoTimeL = req.POST['AHHuanmiaoTimeL']
        AHShenmanTimeH = req.POST['AHShenmanTimeH']
        AHShenmanTimeL = req.POST['AHShenmanTimeL']
        AHZuoguoTimeH = req.POST['AHZuoguoTimeH']
        AHZuoguoTimeL = req.POST['AHZuoguoTimeL']
        AHPengguaTimeH = req.POST['AHPengguaTimeH']
        AHPengguaTimeL = req.POST['AHPengguaTimeL']
        AHChengshuTimeH = req.POST['AHChengshuTimeH']
        AHChengshuTimeL = req.POST['AHChengshuTimeL']
        testah = PlantRange.objects.get(id=3)
        testah.HuanmiaoTimeH = AHHuanmiaoTimeH
        testah.HuanmiaoTimeL = AHHuanmiaoTimeL
        testah.ShenmanTimeH = AHShenmanTimeH
        testah.ShenmanTimeL = AHShenmanTimeL
        testah.ZuoguoTimeH = AHZuoguoTimeH
        testah.ZuoguoTimeL = AHZuoguoTimeL
        testah.PengguaTimeH = AHPengguaTimeH
        testah.PengguaTimeL = AHPengguaTimeL
        testah.ChengshuTimeH = AHChengshuTimeH
        testah.ChengshuTimeL = AHChengshuTimeL
        testah.save()
        #土壤水分
        SMHuanmiaoTimeH = req.POST['SMHuanmiaoTimeH']
        SMHuanmiaoTimeL = req.POST['SMHuanmiaoTimeL']
        SMShenmanTimeH = req.POST['SMShenmanTimeH']
        SMShenmanTimeL = req.POST['SMShenmanTimeL']
        SMZuoguoTimeH = req.POST['SMZuoguoTimeH']
        SMZuoguoTimeL = req.POST['SMZuoguoTimeL']
        SMPengguaTimeH = req.POST['SMPengguaTimeH']
        SMPengguaTimeL = req.POST['SMPengguaTimeL']
        SMChengshuTimeH = req.POST['SMChengshuTimeH']
        SMChengshuTimeL = req.POST['SMChengshuTimeL']
        testsm = PlantRange.objects.get(id=4)
        testsm.HuanmiaoTimeH = SMHuanmiaoTimeH
        testsm.HuanmiaoTimeL = SMHuanmiaoTimeL
        testsm.ShenmanTimeH = SMShenmanTimeH
        testsm.ShenmanTimeL = SMShenmanTimeL
        testsm.ZuoguoTimeH = SMZuoguoTimeH
        testsm.ZuoguoTimeL = SMZuoguoTimeL
        testsm.PengguaTimeH = SMPengguaTimeH
        testsm.PengguaTimeL = SMPengguaTimeL
        testsm.ChengshuTimeH = SMChengshuTimeH
        testsm.ChengshuTimeL = SMChengshuTimeL
        testsm.save()
        #土壤温度
        STHuanmiaoTimeH = req.POST['STHuanmiaoTimeH']
        STHuanmiaoTimeL = req.POST['STHuanmiaoTimeL']
        STShenmanTimeH = req.POST['STShenmanTimeH']
        STShenmanTimeL = req.POST['STShenmanTimeL']
        STZuoguoTimeH = req.POST['STZuoguoTimeH']
        STZuoguoTimeL = req.POST['STZuoguoTimeL']
        STPengguaTimeH = req.POST['STPengguaTimeH']
        STPengguaTimeL = req.POST['STPengguaTimeL']
        STChengshuTimeH = req.POST['STChengshuTimeH']
        STChengshuTimeL = req.POST['STChengshuTimeL']
        testst = PlantRange.objects.get(id=5)
        testst.HuanmiaoTimeH = STHuanmiaoTimeH
        testst.HuanmiaoTimeL = STHuanmiaoTimeL
        testst.ShenmanTimeH = STShenmanTimeH
        testst.ShenmanTimeL = STShenmanTimeL
        testst.ZuoguoTimeH = STZuoguoTimeH
        testst.ZuoguoTimeL = STZuoguoTimeL
        testst.PengguaTimeH = STPengguaTimeH
        testst.PengguaTimeL = STPengguaTimeL
        testst.ChengshuTimeH = STChengshuTimeH
        testst.ChengshuTimeL = STChengshuTimeL
        testst.save()
    return HttpResponseRedirect('/plant/')


def plant_data(req):#西瓜季节及各数据
    response = PlantData.objects.filter(id=1)
    list = PlantRange.objects.all()
    return render_to_response("plant_data.html",{'res':response[0],'light':list[0],'airtem':list[1],'airhum':list[2],'soilmoi':list[3],'soiltem':list[4]})

def reset_value(req):
    response = PlantData.objects.filter(id=1)
    list = PlantRange.objects.all()
    res = []
    light = []
    airtem = []
    airhum = []
    soilmoi = []
    soiltem = []
    res.append(str(response[0].Season))
    res.append(str(response[0].HuanmiaoTimeS))
    res.append(str(response[0].HuanmiaoTimeE))
    res.append(str(response[0].ShenmanTimeS))
    res.append(str(response[0].ShenmanTimeE))
    res.append(str(response[0].ZuoguoTimeS))
    res.append(str(response[0].ZuoguoTimeE))
    res.append(str(response[0].PengguaTimeS))
    res.append(str(response[0].PengguaTimeE))
    res.append(str(response[0].ChengshuTimeS))
    res.append(str(response[0].ChengshuTimeE))
    light.append(str(list[0].DataKind))
    light.append(float(list[0].HuanmiaoTimeH))
    light.append(float(list[0].HuanmiaoTimeL))
    light.append(float(list[0].ShenmanTimeH))
    light.append(float(list[0].ShenmanTimeL))
    light.append(float(list[0].ZuoguoTimeH))
    light.append(float(list[0].ZuoguoTimeL))
    light.append(float(list[0].PengguaTimeH))
    light.append(float(list[0].PengguaTimeL))
    light.append(float(list[0].ChengshuTimeH))
    light.append(float(list[0].ChengshuTimeL))
    airtem.append(str(list[1].DataKind))
    airtem.append(float(list[1].HuanmiaoTimeH))
    airtem.append(float(list[1].HuanmiaoTimeL))
    airtem.append(float(list[1].ShenmanTimeH))
    airtem.append(float(list[1].ShenmanTimeL))
    airtem.append(float(list[1].ZuoguoTimeH))
    airtem.append(float(list[1].ZuoguoTimeL))
    airtem.append(float(list[1].PengguaTimeH))
    airtem.append(float(list[1].PengguaTimeL))
    airtem.append(float(list[1].ChengshuTimeH))
    airtem.append(float(list[1].ChengshuTimeL))
    airhum.append(str(list[2].DataKind))
    airhum.append(float(list[2].HuanmiaoTimeH))
    airhum.append(float(list[2].HuanmiaoTimeL))
    airhum.append(float(list[2].ShenmanTimeH))
    airhum.append(float(list[2].ShenmanTimeL))
    airhum.append(float(list[2].ZuoguoTimeH))
    airhum.append(float(list[2].ZuoguoTimeL))
    airhum.append(float(list[2].PengguaTimeH))
    airhum.append(float(list[2].PengguaTimeL))
    airhum.append(float(list[2].ChengshuTimeH))
    airhum.append(float(list[2].ChengshuTimeL))
    soilmoi.append(str(list[3].DataKind))
    soilmoi.append(float(list[3].HuanmiaoTimeH))
    soilmoi.append(float(list[3].HuanmiaoTimeL))
    soilmoi.append(float(list[3].ShenmanTimeH))
    soilmoi.append(float(list[3].ShenmanTimeL))
    soilmoi.append(float(list[3].ZuoguoTimeH))
    soilmoi.append(float(list[3].ZuoguoTimeL))
    soilmoi.append(float(list[3].PengguaTimeH))
    soilmoi.append(float(list[3].PengguaTimeL))
    soilmoi.append(float(list[3].ChengshuTimeH))
    soilmoi.append(float(list[3].ChengshuTimeL))
    soiltem.append(str(list[4].DataKind))
    soiltem.append(float(list[4].HuanmiaoTimeH))
    soiltem.append(float(list[4].HuanmiaoTimeL))
    soiltem.append(float(list[4].ShenmanTimeH))
    soiltem.append(float(list[4].ShenmanTimeL))
    soiltem.append(float(list[4].ZuoguoTimeH))
    soiltem.append(float(list[4].ZuoguoTimeL))
    soiltem.append(float(list[4].PengguaTimeH))
    soiltem.append(float(list[4].PengguaTimeL))
    soiltem.append(float(list[4].ChengshuTimeH))
    soiltem.append(float(list[4].ChengshuTimeL))
    jsobj = {'res': res,'light':light,'airtem':airtem,'airhum':airhum,'soilmoi':soilmoi,'soiltem':soiltem}
    jsdata = json.dumps(jsobj)
    return HttpResponse(jsdata)

def js_date(req):  #年
    response = []  # 光照和日期
    list = HisData.objects.all()
    for var in list:
        s = str(var.Time)
        response.append([s,float(var.Light_intensity)])
    jsobj = {'datelight':response}
    jsdata = json.dumps(jsobj)
    return HttpResponse(jsdata)

def js_date_month(req):  #月
    if req.is_ajax():
        year = req.POST.get('year')
        month = req.POST.get('month')
        kind = req.POST.get('kind')
    if kind == '光照':
        response = []  # 光照和日期
        if int(month)==12:
            end_date = datetime.date(year=int(year), month=12, day=31)
        else:
            end_date = datetime.date(year=int(year), month=int(month) + 1, day=1)
        start_date = datetime.date(year=int(year),month=int(month),day=1)
        list =HisData.objects.filter(Time__range=(start_date, end_date))
        for var in list:
            s = str(var.Time)
            response.append([s,float(var.Light_intensity)])
        jsobj = {'datelight':response}
        jsdata = json.dumps(jsobj)
        return HttpResponse(jsdata)
    if kind == '空气温度':
        response = []  # 光照和日期
        if int(month)==12:
            end_date = datetime.date(year=int(year), month=12, day=31)
        else:
            end_date = datetime.date(year=int(year), month=int(month) + 1, day=1)
        start_date = datetime.date(year=int(year),month=int(month),day=1)
        list =HisData.objects.filter(Time__range=(start_date, end_date))
        for var in list:
            s = str(var.Time)
            response.append([s,float(var.Air_temperature)])
        jsobj = {'datelight':response}
        jsdata = json.dumps(jsobj)
        return HttpResponse(jsdata)
    if kind == '空气湿度':
        response = []  # 光照和日期
        if int(month)==12:
            end_date = datetime.date(year=int(year), month=12, day=31)
        else:
            end_date = datetime.date(year=int(year), month=int(month) + 1, day=1)
        start_date = datetime.date(year=int(year),month=int(month),day=1)
        list =HisData.objects.filter(Time__range=(start_date, end_date))
        for var in list:
            s = str(var.Time)
            response.append([s,float(var.Air_humidity)])
        jsobj = {'datelight':response}
        jsdata = json.dumps(jsobj)
        return HttpResponse(jsdata)
    if kind == '土壤水分':
        response = []  # 光照和日期
        if int(month)==12:
            end_date = datetime.date(year=int(year), month=12, day=31)
        else:
            end_date = datetime.date(year=int(year), month=int(month) + 1, day=1)
        start_date = datetime.date(year=int(year),month=int(month),day=1)
        list =HisData.objects.filter(Time__range=(start_date, end_date))
        for var in list:
            s = str(var.Time)
            response.append([s,float(var.Soil_moisture)])
        jsobj = {'datelight':response}
        jsdata = json.dumps(jsobj)
        return HttpResponse(jsdata)
    if kind == '土壤温度':
        response = []  # 光照和日期
        if int(month)==12:
            end_date = datetime.date(year=int(year), month=12, day=31)
        else:
            end_date = datetime.date(year=int(year), month=int(month) + 1, day=1)
        start_date = datetime.date(year=int(year),month=int(month),day=1)
        list =HisData.objects.filter(Time__range=(start_date, end_date))
        for var in list:
            s = str(var.Time)
            response.append([s,float(var.Soil_temperature)])
        jsobj = {'datelight':response}
        jsdata = json.dumps(jsobj)
        return HttpResponse(jsdata)

def tem_date(req):
    response = []  # 空气温度和日期
    list = HisData.objects.all()
    for var in list:
        s = str(var.Time)
        response.append([s,float(var.Air_temperature)])
    jsobj = {'datelight':response}
    jsdata = json.dumps(jsobj)
    return HttpResponse(jsdata)

def hum_date(req):
    response = []  # 空气湿度和日期
    list = HisData.objects.all()
    for var in list:
        s = str(var.Time)
        response.append([s,float(var.Air_humidity)])
    jsobj = {'datelight':response}
    jsdata = json.dumps(jsobj)
    return HttpResponse(jsdata)

def soilmoi_date(req):
    response = []  # 土壤水分和日期
    list = HisData.objects.all()
    for var in list:
        s = str(var.Time)
        response.append([s,float(var.Soil_moisture)])
    jsobj = {'datelight':response}
    jsdata = json.dumps(jsobj)
    return HttpResponse(jsdata)

def soiltem_date(req):
    response = []  # 土壤温度和日期
    list = HisData.objects.all()
    for var in list:
        s = str(var.Time)
        response.append([s,float(var.Soil_temperature)])
    jsobj = {'datelight':response}
    jsdata = json.dumps(jsobj)
    return HttpResponse(jsdata)

def reset(req):
    response = PlantData.objects.filter(id=1)
    list = PlantRange.objects.all()
    season = str(response[0].Season)
    HuanmiaoTimeS = str(response[0].HuanmiaoTimeS)
    HuanmiaoTimeE = str(response[0].HuanmiaoTimeE)
    ShenmanTimeS = str(response[0].ShenmanTimeS)
    ShenmanTimeE = str(response[0].ShenmanTimeE)
    ZuoguoTimeS = str(response[0].ZuoguoTimeS)
    ZuoguoTimeE = str(response[0].ZuoguoTimeE)
    PengguaTimeS = str(response[0].PengguaTimeS)
    PengguaTimeE = str(response[0].PengguaTimeE)
    ChengshuTimeS = str(response[0].ChengshuTimeS)
    ChengshuTimeE = str(response[0].ChengshuTimeE)
    return render_to_response("reset.html",{'season':season,'HuanmiaoTimeS':HuanmiaoTimeS,'HuanmiaoTimeE':HuanmiaoTimeE,
                                            'ShenmanTimeS':ShenmanTimeS,'ShenmanTimeE': ShenmanTimeE,
                                            'ZuoguoTimeS':ZuoguoTimeS,'ZuoguoTimeE':ZuoguoTimeE,
                                            'PengguaTimeS': PengguaTimeS,'PengguaTimeE':PengguaTimeE,
                                            'ChengshuTimeS': ChengshuTimeS,'ChengshuTimeE':ChengshuTimeE,
                                            'light':list[0],'airtem':list[1],'airhum':list[2],'soilmoi':list[3],'soiltem':list[4]})