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
    China_data = pd.read_csv(r'D:\\大三下\\课程设计三\\表格\\gmjj\\GDP.csv')
    #print(China_data)
    China_data=China_data.loc[  [0,4,8,12,16,20,24,28,32,36,40,44,48,52,56,60] ]   #提取中国GDP 数据

    return China_data


if __name__ == '__main__':
    ChinaGDP_data=read_csv_excel()   # 中国的数据
    Quater1=[]             # 季度  时间  x轴
    GDP_Absolute1=[]    #国内生产总值绝对值
    GDP_YOY1=[]    #国内生产总值同比增长

    #季度     国内生产总值   国内生产总值同比增长
    for Quater in  ChinaGDP_data['Quater']:
        # Quater = Quater.replace("第1季度", "第1季度")
        # Quater=Quater.replace("第1-2季度", "第1_2季度")
        # Quater = Quater.replace("第1-3季度", "第1_3季度")
        #Quater = Quater.replace("第1-4季度", "第1_4季度")
        #if "第1-4季度" in Quater:
        #print(Quater)
        Quater1.append(Quater)

    for GDP_Absolute in  ChinaGDP_data['GDP_Absolute']:
        GDP_Absolute1.append(GDP_Absolute)
    for GDP_YOY in ChinaGDP_data['GDP_YOY']:
        GDP_YOY=GDP_YOY.replace("%","")
        GDP_YOY1.append(GDP_YOY)


    L1 = (
        #Line(init_opts=opts.InitOpts(bg_color='royalblue')) #背景颜色设置
        Line()  # 背景颜色设置
            .add_xaxis(Quater1)
            .add_yaxis("国内生产总值", GDP_Absolute1, label_opts=opts.LabelOpts(is_show=False), color='red')
            #.add_yaxis("国内生产总值同比增长", GDP_YOY, label_opts=opts.LabelOpts(is_show=False),color='blue')
            .set_global_opts(
            title_opts=opts.TitleOpts(title="中国GDP(单位:亿元)"),
            brush_opts=opts.BrushOpts(),
            tooltip_opts=opts.TooltipOpts(
                is_show=True, trigger="axis", axis_pointer_type="shadow"
            ),
            datazoom_opts=[opts.DataZoomOpts()],   #滚动条
            )
            .set_series_opts(tooltip_opts=opts.TooltipOpts(is_show=True, trigger="item"))
    )
    L1.render('C:\\Users\\Bookcatring\\Desktop\\中国GDP的Line图.html')  # 柱状图   图像展示

