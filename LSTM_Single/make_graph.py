# load and plot dataset
from pandas import read_csv
from pandas import datetime
from matplotlib import pyplot
import streamlit as st


# 加载数据
def parser(x):
    return datetime.strptime(x, '%Y%m%d%H%M')


series = read_csv('LSTM_Single/data.csv', encoding='gbk', header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
# 显示开头部分行
print(series.head())

st.write("""
# 交通大数据课程大作业
137号路段原始数据
""")
st.line_chart(series)

# 画图
series.plot()
# pyplot.legend("best")
pyplot.show()
