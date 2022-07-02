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
#from pyecharts.globals import Bar , Map , WordCloud, Page


def read_csv_excel():
    country_T_D_data = pd.read_excel("C:\\Users\\Bookcatring\\Desktop\\1.xlsx",engine='openpyxl')
    return country_T_D_data


if __name__ == '__main__':


    country_T_D_array=read_csv_excel()   # 国家  日期  感染人数
    country=[]
    infect=[]
    data = []
    locations = []
    max_infect = -1
    for location, num in zip(country_T_D_array['location'], country_T_D_array['total_cases']):
        if location not in locations:  # 如果是新的国家
            data.append([location, num])
            locations.append(location)
            max_infect = -1
        if location in locations:
            if (num > max_infect):
                max_infect = num
                data.pop()
                data.append([location, num])

    for i in range(len(data)):
        for j in range(len(data[i])):
            if j==0:
                country.append(data[i][j])
            if j==1:
                infect.append(data[i][j])


    print(country)
    print("人数",infect)
    bar = (
        # Bar()
        Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
            .add_xaxis(country)
            .add_yaxis("感染人数", infect,category_gap="50%")
            #.add_yaxis("日期", date_list)
            .set_global_opts(
            #xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),
            title_opts=opts.TitleOpts(title="全球新冠肺炎感染bar图"),
            brush_opts=opts.BrushOpts(),
            #datazoom_opts==opts.DataZoomOpts(),   #滚动条

        )
    )

    # 生成bar图
    bar.render('C:\\Users\\Bookcatring\\Desktop\\感染人数bar图.html')  # 柱状图   图像展示

    # country_list = []
    # date_list = []
    # total_infect_list = []
    #
    # print(type(country_T_D_array))
    # # writer=pd.ExcelWriter('C:\\Users\\Bookcatring\\Desktop\\country_time_num.xlsx')
    #
    # # country_T_D_array.to_excel("C:\\Users\\Bookcatring\\Desktop\\2.xls")
    # data=[]

    # for location in country_T_D_array['location']:
    #     if location not in country_list:
    #         country_list.append(location)
    #
    # #print("国家：",country_list)
    # for date,infect in country_T_D_array['date'],country_T_D_array['total_cases']:
    #     date_list.append(date)
    #print("日期：",date_list)
    #for infect in country_T_D_array['total_cases']:
     #   total_infect_list.append(infect)

    # print(country_T_D_array.value_counts().items())
'''
    bar=(
        #Bar()
        Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        .add_xaxis(["国家",country_list])
        .add_yaxis("感染人数",total_infect_list)
        .add_yaxis("日期",date_list)
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),
            title_opts=opts.TitleOpts(title="全球新冠肺炎感染bar图"),
            brush_opts=opts.BrushOpts(),
            #datazoom_opts==opts.DataZoomOpts(),   #滚动条


        )
    )

    #生成bar图
    bar.render('C:\\Users\\Bookcatring\\Desktop\\bar图.html')   #柱状图   图像展示

'''