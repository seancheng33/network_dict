## 项目的起因
这就是一个简单的字典的练习，用来练习python的GUI和做一个小小的字典的实例。<br>
目前是决定采用pyqt5来制作GUI的界面。<br>
字典的功能主要是提供英文查询中文的功能。

## 开发环境
win10 64 bit<br>
PyCharm 2019.3.4<br>
python3.6.2<br>

python的依赖库<br>
click         7.1.1         <br>
pip           19.0.3        <br>
PyQt5         5.13.0        <br>
PyQt5-sip     12.7.1        <br>
PyQt5-stubs   5.13.1.4      <br>
pyqt5-tools   5.13.0.1.5    <br>
python-dotenv 0.12.0        <br>
setuptools    40.8.0        <br>
<br>


## 项目结构
├─source<br>
│  └─icon.ico<br>
├─data.db3<br>
├─dict_main.py<br>
├─load_data.py<br>
├─main.py<br>
├─main.ui<br>
├─readme.md<br>
├─<br>
├─<br>


## 更新进度
2020年3月21日：<br>
* 创建了项目。并开始GUI的制作。<br>

2020年3月22日：<br>
* 修改了界面，改为全部内容可以再一个listview里面直接选取
* 添加了功能在listview里面选择item，可以查询到详情

2020年3月31日
* 字典的词组已经完善到M，尝试对搜索的结果进行一些美化，但是后来取消。
* 待整体完成词典后再进行比较深入到搜索结果美化

## 待处理事项
* comboBox的下拉内容需要增加英文简称的内容
* 美化查询结果和关于此程序