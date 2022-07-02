import os, sys
from imageio import imread
import wordcloud
import jieba
import wordcloud
import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def Generate_wordcloud(txt):
    exclude = {'我们', '你们', '他们', '它们', '因为', '因而', '所以', '如果', '那么', '的','等','等等','和','了','与',
               '如此', '只是', '但是', '就是', '这是', '那是', '而是', '而且', '虽然','或','哦','奥','并','并且','非',
               '这些', '有些', '然后', '已经', '于是', '一种', '一个', '一样', '时候','在','对','为','天','企业','、',
               '没有', '什么', '这样', '这种', '这里', '不会', '一些', '这个', '仍然', '不是','应','二','如','=',

               }
    mk = np.array(Image.open("D:\\大三下\\课程设计三\\表格\\中国地图2.jpg"))
    #mk = np.array(Image.open("D:\\大三下\\课程设计三\\表格\\中国地图.png"))
    w=wordcloud.WordCloud( collocations=False,

                           width=800,height=600,background_color="white",
                           font_path="msyh.ttc",
                           stopwords=exclude,mask=mk

                           )
    #w = wordcloud.WordCloud(collocations=False, width=800, height=600, background_color="white", font_path="SimHei.ttf",mode='RGBA',
                            #stopwords=exclude, mask=mk)

    txt1=" ".join(jieba.lcut(txt))
    #mk=cv2.imread("D:\\大三下\\课程设计三\\表格\\肺部图片.png")
    #mk = np.array(Image.open("D:\\大三下\\课程设计三\\表格\\肺部图片.png"))
    #mk =   imread('D:\\大三下\\课程设计三\\表格\\肺部图片.png')
   # w = wordcloud.WordCloud(mask=mk)
    w.generate(txt1)
    w.to_file('C:\\Users\\Bookcatring\\Desktop\\中国政策词云图.png')


def read_file(file_list):
    txt=""
    print("文件个数:",len(file_list))
    for file in file_list:
        file=str(file)
        with open(file, encoding='utf-8') as file_obj:
            contents = file_obj.read()
            f=contents.rstrip()
            #print(type(f))
            txt=txt+f   #txt.join(f)
    #print("txt内容:\n")
    #print(txt)
    return txt

path_read = []    #存储所有文件名字
def check_if_dir(file_path):   #记录所有文件名
    temp_list = os.listdir(file_path)  #

    if os.path.isfile(file_path + '/' + temp_list[0]):  # 此处直接判断list中第一项是不是文件
        for temp_list_each in temp_list:
            temp_path = file_path + '/' + temp_list_each
            if os.path.splitext(temp_path)[-1] == '.txt':
                path_read.append(temp_path)
            else:
                continue
    else:
        for temp_list_each in temp_list:
            check_if_dir(file_path + '/' + temp_list_each)  # loop traversal



if __name__ == '__main__':

    path = "D:\\大三下\\课程设计三\\表格\\china_policy\\"
    check_if_dir(path)
    #print(path_read)
    #print(type(path_read))
    txt=read_file(path_read)
    Generate_wordcloud(txt)