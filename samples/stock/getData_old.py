import tushare as ts
import pandas as pd

results = pd.DataFrame( columns=['600820','000541','600256','000027','sh','total'])

s = (4, 207000,89850,13000,30000,1000)

d1 = ts.get_hist_data( '600820' )
d2 = ts.get_hist_data( '000541')
d3 = ts.get_hist_data( '600256')
d4 = ts.get_hist_data( '000027') 
d5 = ts.get_hist_data( 'sh')

d = (s[0], d1,d2,d3,d4)
dateindex = d5.index
j= 0
cold = [s[0],0,0,0,0]
for i in dateindex :    
    c = cold 
    #[ s[0], d1.loc[i]['close'], d2.loc[i]['close'],d3.loc[i]['close'],d4.loc[i]['close']] #,d5.loc[i]['close'])
    #print(j+1, i, hisdata.loc[i]['close'], sep=' ', end='\n') #, hisdata.iloc[i]['close'], sep=' ', end='\n' )
    sum = 0
    for k in range(1,s[0]+1):
        try:
            c[k] = d[k].loc[i]['close']
        except KeyError:
            c[k] = cold[k]
        sum = sum + c[k]*s[k]
    j=j+1
    #print("debug", s, '\n',c,'\n')
    results.loc[i] = [c[1], c[2],c[3],c[4], d5.loc[i]['close'], sum ]
    #print( repr(j).rjust(3), i, \
    #    repr(c[1]).rjust(6), \
    #    repr(c[2]).rjust(6), \
    #    repr(c[3]).rjust(6), \
    #    repr(c[4]).rjust(6), \
    #    "%10.2f" % d5.loc[i]['close'], "%12.2f" % sum)
    #repr(d5.loc[i]['close']).rjust(8), sum )
    cold = c

    results.to_csv( "abc1031.csv", sep=",")
print(results)




