from data.models import *


def getIndicators():
    return DigitalEconomyIndicators.objects.all()


def getIndex():
    return EconomicIndex.objects.all()

def getGDP():
    return GDP.objects.all()
