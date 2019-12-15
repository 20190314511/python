import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

np.random.seed(sum(map(ord,"aesthetics")))

import tushare as ts

def sinplot(dd,mxx):
    mxs =  max( dd.iloc[:,2])

    print(mxs,mxx)

    itemTotal= len(d.index)
    x =np.linspace(0,itemTotal-1,itemTotal)
    #x = np.linspace(d.iloc[itemTotal-1], d.iloc[0], itemTotal)
    plt.plot(x,(d.iloc[itemTotal - x -1]['close'])*mxx/mxs)

ds = ts.get_hist_data('sh')
mx = max( ds.iloc[:,2])

d = ts.get_hist_data('000027')
sinplot(d,mx)
d = ts.get_hist_data('000541')
sinplot(d,mx)
d = ts.get_hist_data('600256')
sinplot(d,mx)
d = ts.get_hist_data('600820')
sinplot(d,mx)

plt.show()

