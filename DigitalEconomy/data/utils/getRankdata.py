import json
import time
from .getDBdata import *


def getrankdata (year):
    index = list(getIndex())
    indexData = []
    # 根据年份分组并计算每个年份的最大值
    max_index_values = {}
    for i in index:
        key_year = i.year  # 假设这里可以获取到每个数据条目的年份
        if key_year not in max_index_values:
            max_index_values[key_year] = i.economic_index
        else:
            max_index_values[key_year] = max(max_index_values[key_year], i.economic_index)

    sorted_index = []
    for i in index:
        if i.year == year:
            i.economic_index = round((i.economic_index / max_index_values[i.year]) * 100, 1)
            sorted_index.append(i)

    sorted_index = sorted(sorted_index, key=lambda x: x.economic_index, reverse=True)

    # 增加序号字段并添加到indexData中
    for i, item in enumerate(sorted_index):
        indexData.append({
            'rank': i + 1,
            'region': item.region,
            'economic_index': item.economic_index
        })

    return indexData
