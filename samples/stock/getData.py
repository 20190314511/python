import tushare as ts
import pandas as pd
import time

ts.set_token('12bb779124f9988620a14ba03fca106fe22d8a241c3770ed2df29e83')
pro = ts.pro_api()

str_today =  time.strftime("%Y%m%d",time.localtime(time.time()))

# 填写股票代码和对应的数量
stock_code = ( 
    '600820.SH',        # 1
    '000541.SZ',        # 2
    '600256.SH',        # 3
    '000027.SZ',        # 4
    '002939.SZ',        # 5
    '601577.SH',        # 6
    '601138.SH'         # 7
     )
s = ( 
    207000,89850,13000,30000,500, 1000,500 )
slen = len(stock_code)

col = []
for i in range(0,slen) :
    col.append( stock_code[i]+':'+str(s[i]) )
col.append( 'total ' )
results = pd.DataFrame( columns=col )


d = []
for i in range(0, slen):
    n =  pro.daily( ts_code=stock_code[i], start_date='19000101', end_date=str_today)
    d.append( n.set_index('trade_date'))


j= 0
cold = [0,0,0,0,0,0,0,0,0,0,0]

for i in d[0].index :    
    c = cold 

    sum = 0
    for k in range(0,slen):
        try:
            c[k] = d[k].loc[i]['close']
        except KeyError:
            c[k] = cold[k]
        sum = sum + c[k]*s[k]
    j=j+1

    row = []
    for k in range(0,slen):
        row.append( c[k] )
    row.append( sum )

    results.loc[i] = row

    cold = c

filename = str_today+".csv"
results.to_csv( filename, sep=",")
print(results)




