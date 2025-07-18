import json
import time
from .getDBdata import *


def getbubbledata(year):
    index = list(getIndex())
    with open('./digital_economy/src/utils/china.json', 'r', encoding='utf-8') as f:
        jsonData = json.load(f)
    bubbleData = []

    # 根据年份分组并计算每个年份的最大值
    max_index_values = {}
    for i in index:
        key_year = i.year  # 假设这里可以获取到每个数据条目的年份
        if key_year not in max_index_values:
            max_index_values[key_year] = i.economic_index
        else:
            max_index_values[key_year] = max(max_index_values[key_year], i.economic_index)

    for i in index:
        for feature in jsonData['features']:
            if feature['properties']['name'] in i.region:
                i.region = feature['properties']['name']

    # 根据每个数据条目的年份对其进行除法运算
    for i in index:
        if i.year == year:
            i.economic_index = round((i.economic_index / max_index_values[i.year]) * 100, 1)
            area_index=GetAreaLevel(i.region)
            bubbleData.append({
                'name': i.region,
                'value': [area_index,i.economic_index]
            })

    return bubbleData

def GetAreaLevel(region):
    first_areas = ['北京', '上海', '江苏', '福建', '浙江', '天津', '广东']
    second_areas = ['内蒙古', '湖北', '重庆', '山东', '陕西', '安徽', '湖南', '新疆']
    third_areas = ['山西', '海南', '宁夏', '辽宁', '四川', '江西', '西藏', '云南']
    other_areas = ['青海', '河南', '河北', '吉林', '贵州', '广西', '黑龙江', '甘肃', '澳门', '香港', '台湾']
    if region in first_areas:
        return 0
    elif region in second_areas:
        return 1
    elif region in third_areas:
        return 2
    elif region in other_areas:
        return 3
