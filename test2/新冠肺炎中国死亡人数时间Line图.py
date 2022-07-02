import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import workbook
import openpyxl
import xlwt
import datetime
import jieba
from pyecharts import options as opts
from pyecharts.charts import Bar   #导入柱状图包
from pyecharts.charts import Map  #导入地图
from pyecharts.charts import Line  #导入折线图
from pyecharts.globals import ThemeType
from pyecharts.globals import SymbolType
#from pyecharts.globals import Bar , Map , WordCloud, Page


def read_csv_excel():
    country_T_D_data = pd.read_csv(r'C:\\Users\\Bookcatring\\Desktop\\owid-covid-data.csv')
    China_data=country_T_D_data.loc[31791:32570]   #提取中国数据
    return China_data


if __name__ == '__main__':


    China_data=read_csv_excel()   # 中国的数据
    data_death=[]
    date1=[]
    death1=[]
    case1=[]
    #日期  死亡人数
    for date, death in zip(China_data['date'], China_data['total_deaths']):
        date1.append(date)
        death1.append(int(death))
        #data.append([date, int(death)])
    for case in  China_data['total_cases']:
        case1.append(int(case))
        #data.append([date, int(death)])
    # 年月日
    y=[]
    m=[]
    d=[]

    for i in range(len(date1)):
        date_list = date1[i].split("-")
        y = int(date_list[0])
        m = int(date_list[1])
        d = int(date_list[2])

    #datetime.datetime(y, m, d)



    L1 = (
        # Bar()
        Line()
            #.add_xaxis(datetime.datetime[y,m,d])
            .add_xaxis(date1)
            .add_yaxis("死亡人数", death1,label_opts=opts.LabelOpts(is_show=False),color='red')
            .add_yaxis("感染人数", case1, label_opts=opts.LabelOpts(is_show=False),color='blue')
            #.add_yaxis("日期", date_list)
            .set_global_opts(
            #xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),
            title_opts=opts.TitleOpts(title="新冠肺炎中国死亡人数"),
            brush_opts=opts.BrushOpts(),
            tooltip_opts=opts.TooltipOpts(
                is_show=True, trigger="axis", axis_pointer_type="shadow"
            ),

            datazoom_opts=[opts.DataZoomOpts()],   #滚动条

            )
            .set_series_opts(tooltip_opts=opts.TooltipOpts(is_show=True, trigger="item"))
    )

    # 生成bar图
    L1.render('C:\\Users\\Bookcatring\\Desktop\\新冠肺炎中国死亡人数Line图.html')  # 柱状图   图像展示

