from django.urls import path
from .views import *

urlpatterns = [
    path('rank/<str:year>/', Rank),
    path('bubble/<str:year>/', Bubble),
    path('cross/<str:year>/', Cross),
    path('radar/<str:year>/<str:province>/',Radar),
    path('text/<str:year>/<str:province>/<str:name>/',Text),
    path('map/<str:year>/', Map),
    path('indicators', get_indicators),
]
