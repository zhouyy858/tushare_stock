import pandas as pd  
import numpy as np
import talib as ta
from datetime import datetime,timedelta
import matplotlib.pyplot as plt
#正常显示画图时出现的中文和负号
from pylab import mpl
mpl.rcParams['font.sans-serif']=['SimHei']#设置字体
mpl.rcParams['axes.unicode_minus']=False #显示中文


#（1）当今天的收盘价，大于过去20个交易日中的最高价时，以收盘价买入；  
#（2）买入后，当收盘价小于过去10个交易日中的最低价时，以收盘价卖出。
def run_strategy(data):
    x1=data.close>data.up#判断当天是否上涨
    x2=data.close.shift(1)<data.up.shift(1)
    x=x1&x2
    y1=data.close<data.down
    y2=data.close.shift(1)>data.down.shift(1)
    y=y1&y2
    data.loc[x,'signal']='buy'
    data.loc[y,'signal']='sell'
    buy_date=(data[data.signal=='buy'].index).strftime('%Y%m%d')
    sell_date=(data[data.signal=='sell'].index).strftime('%Y%m%d')
    buy_close=data[data.signal=='buy'].close.round(2).tolist()
    sell_close=data[data.signal=='sell'].close.round(2).tolist()
    return (buy_date,buy_close,sell_date,sell_close)

def read_csv_data(data_path):
    csv_data = pd.read_csv(data_path) #读取csv文件
    csv_data = csv_data[::-1]   #安时间倒序
    return csv_data

if __name__ == "__main__":
    data = read_csv_data('../stock_data/000039.SZ.csv')
    #print(data[0:])
    for i in range(len(data)):
        run_strategy(data[i:i+1])
        #print(data[i:i+1])
    # for sline in data[1::]:
    #     print(sline)
    #     run_strategy(sline)

    # print(data)

