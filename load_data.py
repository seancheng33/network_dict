'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2020/3/22
@Program      : 读取数据的功能
'''

import sqlite3

def load_list():
    # 建立一个空的list
    namelist = []
    # 连接数据文件，读取里面的英文单词或词组的内容
    with sqlite3.connect("data.db3") as datacon:
        datalist = datacon.execute("select en_full from network;")
        # 将读取到的内容添加到list中
        for item in datalist:
            namelist.append(item[0])
    # 返回这个列表的内容
    return namelist

def load_word_detail(keyword):
    # 连接数据文件，读取里面的英文单词或词组的内容
    with sqlite3.connect("data.db3") as datacon:
        detailList = []
        detail = datacon.execute("select * from network where en_full='"+keyword+"';")
        for item in detail:
            detailList.append(item[1:])
    # 返回这个内容
    return detailList