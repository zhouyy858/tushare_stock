import tushare as ts

pro = ts.pro_api('75488f3d47c141820f7974e44cbefe70b0560d1d1488ff488657567f')

#获取股票公司列表
data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')

for i=[0, data.size]

df = pro.daily(ts_code='000001.SZ', start_date='20180701', end_date='20180718')
print(data)