import tushare as ts
import pandas as pd
import time

k = ( '600820', '000541','600256','000027','002939','601577','601138' )
s = ( 207000,89850,13000,30000,500, 1000,500 )
slen = len(k)

col = []
for i in range(0,slen) :
    col.append( k[i]+':'+str(s[i]) )
col.append( 'sh' )
col.append( 'total ' )
results = pd.DataFrame( columns=col )

d = []
for i in range(0, slen):
    d.append( ts.get_hist_data(k[i]))

d.append( ts.get_hist_data('sh') )

j= 0
cold = [0,0,0,0,0,0,0,0,0,0,0]

for i in d[slen].index :    
    c = cold 
    #[ s[0], d1.loc[i]['close'], d2.loc[i]['close'],d3.loc[i]['close'],d4.loc[i]['close']] #,d5.loc[i]['close'])
    #print(j+1, i, hisdata.loc[i]['close'], sep=' ', end='\n') #, hisdata.iloc[i]['close'], sep=' ', end='\n' )
    sum = 0
    for k in range(0,slen):
        try:
            c[k] = d[k].loc[i]['close']
        except KeyError:
            c[k] = cold[k]
        sum = sum + c[k]*s[k]
    j=j+1
    #print("debug", s, '\n',c,'\n')

    row = []
    for k in range(0,slen):
        row.append( c[k] )
    row.append( d[slen].loc[i]['close'])
    row.append( sum )

    results.loc[i] = row
    #print( repr(j).rjust(3), i, \
    #    repr(c[1]).rjust(6), \
    #    repr(c[2]).rjust(6), \
    #    repr(c[3]).rjust(6), \
    #    repr(c[4]).rjust(6), \
    #    "%10.2f" % d5.loc[i]['close'], "%12.2f" % sum)
    #repr(d5.loc[i]['close']).rjust(8), sum )
    cold = c

filename = time.strftime("%Y%m%d",time.localtime(time.time()))+".csv"
results.to_csv( filename, sep=",")
print(results)




