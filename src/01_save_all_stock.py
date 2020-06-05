import tushare as ts
import multiprocessing
import time


stock_c = 0
pro = ts.pro_api('75488f3d47c141820f7974e44cbefe70b0560d1d1488ff488657567f')

#获取股票公司列表
stocks_list = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
ser = stocks_list.iloc[:,0]                         #选择第一列
# print(stocks_list,type(ser1))


# ####单线程
# for i in ser:
#     stock_c = stock_c+1
#     print(i,stock_c/len(ser))                                     
#     stocks_num = pro.daily(ts_code = i)                
#     stocks_num.to_csv('../stock_data/'+i+'.csv')


####多线程
def get_stock_data(tcode):
    print(tcode)
    stocks_num = pro.daily(ts_code=tcode)   
    stocks_num.to_csv('../stock_data/'+tcode+'.csv')
    time.sleep(1) #每分钟500次访问限制

items = [x for x in ser]
from multiprocessing.dummy import Pool as ThreadPool
pool = ThreadPool()
pool.map(get_stock_data, items)
pool.close()
pool.join()