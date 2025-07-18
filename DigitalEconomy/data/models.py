from django.db import models


class DigitalEconomyIndicators(models.Model):
    region = models.CharField(primary_key=True, max_length=8, db_column='地区')
    year = models.CharField(max_length=6, db_column='年份')
    infrastructure = models.FloatField(db_column='基础设施')
    digital_industry = models.FloatField(db_column='数字产业')
    industry_integration = models.FloatField(db_column='产业融合')
    development_environment = models.FloatField(db_column='发展环境')

    class Meta:
        managed = False
        db_table = '数字经济发展指数指标汇总'
        unique_together = (('region', 'year'),)


class EconomicIndex(models.Model):
    region = models.CharField(primary_key=True, max_length=8,db_column='地区')
    year = models.CharField(max_length=6,db_column='年份')
    economic_index=models.FloatField(db_column='数字经济发展指数')

    class Meta:
        managed = False
        db_table = '数字经济发展指数'
        unique_together = (('region', 'year'),)


class GDP(models.Model):
    region = models.CharField(primary_key=True, max_length=8, db_column='地区')
    year = models.CharField(max_length=6, db_column='年份')
    gdp = models.FloatField(db_column='GDP')

    class Meta:
        managed = False
        db_table = '各省gdp'
        unique_together = (('region', 'year'),)

