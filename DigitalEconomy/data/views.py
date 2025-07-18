from django.http import JsonResponse
from .utils import getRankdata, getRadardata, getMapdata, getBubbledata, getCrossdata, getTextdata,getDBdata


def Rank(request,year):
    if request.method == 'GET':
        rankData=getRankdata.getrankdata(year)
        return JsonResponse({
            'rankData': rankData
        })

def Radar(request, year, province):
    if request.method == 'GET':
        radarData = getRadardata.getradardata(year, province)
        return JsonResponse({
            'radarData': radarData
        })


def Map(request,year):
    if request.method == 'GET':
        mapData=getMapdata.getmapdata(year)
        return JsonResponse({
            'mapData': mapData
        })

def Bubble(request,year):
    if request.method == 'GET':
        bubbleData=getBubbledata.getbubbledata(year)
        return JsonResponse({
            'bubbleData': bubbleData
        })

def Cross(request,year):
    if request.method == 'GET':
        crossData=getCrossdata.getcrossdata(year)
        return JsonResponse({
            'crossData': crossData
        })

def Text(request,year,province,name):
    if request.method == 'GET':
        textData=getTextdata.gettextdata(year,province,name)
        return JsonResponse({
            'textData': textData
        })

def get_indicators(request):
    data = getDBdata.getIndicators()
    indicators = [{'year': i.year, 'region': i.region,'infrastructure':i.infrastructure,'digital_industry':i.digital_industry,'industry_integration':i.industry_integration,'development_environment':i.development_environment} for i in data]
    return JsonResponse(indicators, safe=False)


