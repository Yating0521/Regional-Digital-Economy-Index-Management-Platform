import json
import time
from .getDBdata import *


def getcrossdata(year):
    index = list(getIndex())
    gdp = list(getGDP())
    with open('./digital_economy/src/utils/china.json', 'r', encoding='utf-8') as f:
        jsonData = json.load(f)
    crossData = []
    for i in index:
        for feature in jsonData['features']:
            if feature['properties']['name'] in i.region:
                i.region = feature['properties']['name']

    # 根据年份分组并计算每个年份的最大值
    max_index_values = {}
    for i in index:
        key_year = i.year  # 假设这里可以获取到每个数据条目的年份
        if key_year not in max_index_values:
            max_index_values[key_year] = i.economic_index
        else:
            max_index_values[key_year] = max(max_index_values[key_year], i.economic_index)

    # 根据每个数据条目的年份对其进行除法运算
    for i in index:
        if i.year == year:
            i.economic_index = round((i.economic_index / max_index_values[i.year]) * 100, 1)
    for i in index:
        for j in gdp:
            if i.year == year and i.year == j.year and i.region == j.region:
                crossData.append({
                    'name': i.region,
                    'value': [j.gdp, i.economic_index]
                })

    return crossData
