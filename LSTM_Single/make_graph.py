# load and plot dataset
from pandas import read_csv
from pandas import datetime
from matplotlib import pyplot
import streamlit as st


# 加载数据
def parser(x):
	return datetime.strptime(x, '%Y%m%d%H%M')
series = read_csv('data.csv',encoding='gbk', header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
# 显示开头部分行
print(series.head())

st.write("""
# My first app
Hello *world!*
""")
st.line_chart(series)

# 画图
series.plot()
# pyplot.legend("best")
pyplot.show()
