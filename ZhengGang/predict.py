from __future__ import print_function
import pandas as pd
import numpy as np
from scipy import  stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.api import qqplot

dta = [11481, 15692, 9380, 11804, 17953, 24012, 32666]
dta = np.array(dta, dtype=np.float)

# current situation graph
dta = pd.Series(dta)
# dta.index = pd.Index(sm.tsa.datetools.dates_from_range('2011', '2017'))
# fig = plt.figure(figsize=(12, 8))
# ax1= fig.add_subplot(111)

dta = pd.Series(dta)
dta.index = pd.Index(sm.tsa.datetools.dates_from_range('2011', '2017'))
dta.plot(figsize=(12, 8))
fig = plt.figure(figsize=(12, 8))
diff1= dta.diff(2)
fig = plt.figure(figsize=(12,8))
ax1=fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(dta,lags=6,ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(dta,lags=6,ax=ax2)
# plt.show()

# arma_mod30 = sm.tsa.ARMA(dta, (0,1)).fit()
# print(arma_mod30.aic,arma_mod30.bic,arma_mod30.hqic)
# arma_mod71 = sm.tsa.ARMA(dta,(7,1)).fit()
# print(arma_mod71.aic,arma_mod71.bic,arma_mod71.hqic)
arma_mod80 = sm.tsa.ARMA(dta, (2, 1)).fit()
# print(arma_mod80.aic,arma_mod80.bic,arma_mod80.hqic)
resid = arma_mod80.resid

fig = plt.figure(figsize=(12 ,8))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(resid.values.squeeze(), lags=6, ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(resid, lags=6, ax=ax2)
# plt.show()
# print(stats.normaltest(resid))
fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111)
fig = qqplot(resid, line='q', ax=ax, fit=True)
#plt.show()

# print(stats.normaltest(resid))
# fig = plt.figure(figsize=(12,8))
# ax = fig.add_subplot(111)
# fig = qqplot(resid, line='q', ax=ax, fit=True)
# plt.show()

r,q,p = sm.tsa.acf(resid.values.squeeze(), qstat=True)
data = np.c_[range(1, 7), r[1:], q, p]
table = pd.DataFrame(data, columns=['lag', "AC", "Q", "Prob(>Q)"])
print(table.set_index('lag'))

predict_dta = arma_mod80.predict('2018', '2027', dynamic=True)
print(predict_dta)


fig, ax = plt.subplots(figsize=(12, 8))
ax = dta.ix['2013':].plot(ax=ax)
fig = arma_mod80.plot_predict('2018', '2027', dynamic=True, ax=ax, plot_insample=False)
plt.show()


def draw_initial(dta):
       dta = pd.Series(dta)
       dta.index = pd.Index(sm.tsa.datetools.dates_from_range('2011', '2017'))
       dta.plot(figsize=(12, 8))
       plt.show()


dta = [408149, 473300, 171955, 165504, 498158, 163309, 592468, 762256, 237764, 531882]
dta= np.array(dta,dtype=np.float)
dta=pd.Series(dta)
dta.index = pd.Index(sm.tsa.datetools.dates_from_range('2018','2027'))
dta.plot(figsize=(12,8))
plt.show()

