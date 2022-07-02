import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import workbook
import openpyxl
import xlwt
import jieba
from pyecharts import options as opts
from pyecharts.charts import Bar   #导入柱状图包
from pyecharts.charts import Map
from pyecharts.globals import ThemeType
from pyecharts.globals import SymbolType
#from pyecharts.globals import Pie, Bar , Map , WordCloud, Page


def read_csv_excel():                                                                                                      #   国家    死亡人数
    country_Death = pd.read_csv(r'C:\\Users\\Bookcatring\\Desktop\\owid-covid-data.csv', sep=',', header='infer', nrows=167709,usecols=[2, 7])
    #country_Death.drop_duplicates(inplace=True)   #去重
    #print(country_Death)
    #country_Death['location']
    #country_Death=country_Death.tolist()

    #country_Death = country_Death.values[0::, 0::]  # 读取全部行，全部列
    #print(country_Death)
    return country_Death

def delete_same_value_row(country_D):
    country_D.duplicates(inplace=True)     # 删除一模一样的行
    #country__total_daily_infections.duplicates(subset=['列名','列名'])  #删除一样的列
    return country_D

if __name__ == '__main__':

    country_Death=read_csv_excel()   # 国家   死亡人数
    #country_Death=delete_same_value_row(country_Death)   # 去重
    data = []
    locations = []
    max_infect = -1

    for location, num in zip(country_Death['location'], country_Death['total_deaths']):
        if location not in locations:  # 如果是新的国家
            data.append([location, num])
            locations.append(location)
            max_infect = -1
        if location in locations:
            if (num > max_infect):
                max_infect = num
                data.pop()
                data.append([location, num])


    map = (
        Map()

            .add("死亡人数(2020/2/24 ~ 2022/3/11)", data, "world")

            .set_global_opts(title_opts=opts.TitleOpts(title="全球新冠肺炎死亡人数图"),
                             visualmap_opts=opts.VisualMapOpts(max_=970000, min_=0, is_piecewise=True),
                             )
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    )
    map.render("C:\\Users\\Bookcatring\\Desktop\\死亡人数map图.html")





