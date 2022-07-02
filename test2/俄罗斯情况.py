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
    Russia_data=country_T_D_data.loc[124782:125552]   #提取俄罗斯数据
    return Russia_data


if __name__ == '__main__':


    Russia_data=read_csv_excel()   # 中国的数据
    #print(Russia_data)

    date1=[]             # 时间  x轴
    stringency_index1=[]    #政策严格度指数
    total_vaccinations=[]    #疫苗接种
    icu_patients=[]       # 某一天重症监护病房 (ICU) 中的 COVID-19 患者人数
    hosp_patients=[]      #某一天住院的COVID - 19患者人数
    total_tests=[]    #total_tests	COVID-19 的总测试
    total_cases=[]    #总感染人数
    #日期  接种疫苗总数
    for date, total_vaccinations1 in zip(Russia_data['date'], Russia_data['total_vaccinations']):
        date1.append(date)
        total_vaccinations.append(total_vaccinations1)

    for case in  Russia_data['stringency_index']:
        stringency_index1.append(case)
    for icu_patients1 in Russia_data['icu_patients']:
        icu_patients.append(icu_patients1)
    for hosp_patients1 in Russia_data['hosp_patients']:
        hosp_patients.append(hosp_patients1)
    for total_tests1 in Russia_data['total_tests']:
        total_tests.append(total_tests1)

    total_deaths = []  # 死于 COVID-19 的总死亡人数。包括可能的死亡人数。
    for total_death in Russia_data['total_deaths']:
        total_deaths.append(total_death)

    total_cases = []  # 总感染人数
    for case in Russia_data['total_cases']:
        total_cases.append(int(case))

    cd = []  # 死亡人数 /感染人数
    for i in range(len(total_deaths)):
        cd1 = float((total_deaths[i]) / (total_cases[i]))
        cd.append(cd1)
    L1 = (
        # Bar()
        Line()
            #.add_xaxis(datetime.datetime[y,m,d])
            .add_xaxis(date1)
            .add_yaxis("政策回应严格度指数", stringency_index1,label_opts=opts.LabelOpts(is_show=False))
            .add_yaxis("疫苗接种人数", total_vaccinations, label_opts=opts.LabelOpts(is_show=False))
            .add_yaxis("当天ICU人数", icu_patients, label_opts=opts.LabelOpts(is_show=False))
            #add_yaxis("患者总人数", hosp_patients, label_opts=opts.LabelOpts(is_show=False))
            .add_yaxis("总测试人数", total_tests, label_opts=opts.LabelOpts(is_show=False))
            .add_yaxis("死亡人数", total_deaths, label_opts=opts.LabelOpts(is_show=False))
            .add_yaxis("感染人数", total_cases, label_opts=opts.LabelOpts(is_show=False))
            .add_yaxis("死亡/感染(比例)", cd, label_opts=opts.LabelOpts(is_show=False))
            #.add_yaxis("日期", date_list)
            .set_global_opts(
            #xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),
            title_opts=opts.TitleOpts(title="俄罗斯"),
            # brush_opts=opts.BrushOpts(),
            # tooltip_opts=opts.TooltipOpts(
            #     is_show=True, trigger="axis", axis_pointer_type="shadow"
            # ),

            datazoom_opts=[opts.DataZoomOpts()],   #滚动条

            )
            .set_series_opts(tooltip_opts=opts.TooltipOpts(is_show=True, trigger="item"))
    )

      # 生成bar图
    L1.render('C:\\Users\\Bookcatring\\Desktop\\俄罗斯情况Line图.html')  # 柱状图   图像展示
