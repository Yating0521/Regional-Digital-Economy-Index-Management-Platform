import json
import time
from .getDBdata import *


def gettextdata(year, province, name):
    indicators = list(getIndicators())
    index = list(getIndex())
    textData = ""
    with open('./digital_economy/src/utils/china.json', 'r', encoding='utf-8') as f:
        jsonData = json.load(f)
    for i in indicators:
        for feature in jsonData['features']:
            if feature['properties']['name'] in i.region:
                i.region = feature['properties']['name']
    for j in index:
        for feature in jsonData['features']:
            if feature['properties']['name'] in j.region:
                j.region = feature['properties']['name']

    # 根据年份分组并计算每个年份的最大值
    max_index_values = {}
    max_infrastructure_values = {}
    max_digital_industry_values = {}
    max_industry_integration_values = {}
    max_development_environment_values = {}
    for i in index:
        key_year = i.year  # 假设这里可以获取到每个数据条目的年份
        if key_year not in max_index_values:
            max_index_values[key_year] = i.economic_index
        else:
            max_index_values[key_year] = max(max_index_values[key_year], i.economic_index)

    for j in indicators:
        key_year = j.year  # 假设这里可以获取到每个数据条目的年份
        if key_year not in max_infrastructure_values:
            max_infrastructure_values[key_year] = j.infrastructure
        else:
            max_infrastructure_values[key_year] = max(max_infrastructure_values[key_year], j.infrastructure)
        if key_year not in max_digital_industry_values:
            max_digital_industry_values[key_year] = j.digital_industry
        else:
            max_digital_industry_values[key_year] = max(max_digital_industry_values[key_year], j.digital_industry)
        if key_year not in max_industry_integration_values:
            max_industry_integration_values[key_year] = j.industry_integration
        else:
            max_industry_integration_values[key_year] = max(max_industry_integration_values[key_year],
                                                            j.industry_integration)
        if key_year not in max_development_environment_values:
            max_development_environment_values[key_year] = j.development_environment
        else:
            max_development_environment_values[key_year] = max(max_development_environment_values[key_year],
                                                               j.development_environment)

    for i in index:
        if i.year == year and i.region == province:
            for j in indicators:
                if i.year == j.year and i.region == j.region:
                    i.economic_index = round((i.economic_index / max_index_values[i.year]) * 100, 1)
                    j.infrastructure = round((j.infrastructure / max_infrastructure_values[i.year]) * 100, 1)
                    j.digital_industry = round((j.digital_industry / max_digital_industry_values[i.year]) * 100, 1)
                    j.industry_integration = round(
                        (j.industry_integration / max_industry_integration_values[i.year]) * 100, 1)
                    j.development_environment = round(
                        (j.development_environment / max_development_environment_values[i.year]) * 100, 1)
                    if name == '数字经济发展指数':
                        textData = i.economic_index
                    elif name == '基础设施指数':
                        textData = j.infrastructure
                    elif name == '数字产业指数':
                        textData = j.digital_industry
                    elif name == '产业融合指数':
                        textData = j.industry_integration
                    elif name == '发展环境指数':
                        textData=j.development_environment

    return textData
