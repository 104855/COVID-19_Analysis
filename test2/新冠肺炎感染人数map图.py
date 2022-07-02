import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import workbook
import openpyxl
import xlwt
import jieba
from pyecharts import options as opts
from pyecharts.charts import Bar   #导入柱状图包
from pyecharts.charts import Map  #导入地图
from pyecharts.globals import ThemeType
from pyecharts.globals import SymbolType


def read_csv_excel():
    #country_T_D_data = pd.read_excel("C:\\Users\\Bookcatring\\Desktop\\1.xlsx",engine='openpyxl')                              #  国家   感染人数
    country_T_D_data = pd.read_csv(r'C:\\Users\\Bookcatring\\Desktop\\owid-covid-data.csv', sep=',', header='infer',nrows=167709, usecols=[2, 4])

    return country_T_D_data


if __name__ == '__main__':

    country_T_D_array=read_csv_excel()   # 国家的 总共和每天 感染人数
    #continent=[]       # 4个列表来存储4列不同的数据，分别是   国家  日期 总感染人数  每天感染人数

    data=[]
    locations=[]
    max_infect=-1
    for location,num in zip(country_T_D_array['location'],country_T_D_array['total_cases']):
        if location not in locations:  #如果是新的国家
            data.append([location,num])
            locations.append(location)
            max_infect=-1
        if location in locations:
            if(num>max_infect):
                max_infect=num
                data.pop()
                data.append([location,num])
        #data.append([location,date,num])
    print(data[0][0],data[1])


    map=(
        Map()
            #.add("感染人数",[list(location) for location in locations],"world")
            #.add("感染时间",[list(date_num) for date,num in date_lists,total_infect_list],"world")
            .add("感染人数(2020/2/24 ~ 2022/3/11)",data,"world")
            .set_global_opts(title_opts=opts.TitleOpts(title="全球新冠肺炎疫染人数图"),

            visualmap_opts=opts.VisualMapOpts(max_=80000000,min_=1000,is_piecewise=True

            ),      #excel表中数据的最大值
            #visualmap_opts=opts.VisualMapOpts(max_="2022/3/11")
            ).set_series_opts(label_opts=opts.LabelOpts(is_show=False))
         )
    map.render("C:\\Users\\Bookcatring\\Desktop\\感染人数map图.html")

