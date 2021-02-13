# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 23:39:10 2021

@author: Deepan
"""

import pandas_datareader as web
import numpy as np
import pandas as pd
from datetime import date, timedelta
import datetime
end = datetime.datetime.today()
start = datetime.date(end.year-8,9,1)

def my_stock_price(stock_nm):
    #stock_nm="3MINDIA.NS"
    data=web.get_data_yahoo(stock_nm,start,interval='d')
    data['Date'] = data.index
    #data.info()
    #data.describe()
    data['year']=pd.DatetimeIndex(data['Date']).year
    print(stock_nm,data['year'].min())
        
stock_list=["AARTIDRUGS.NS","AARTIIND.NS","ADANIGREEN.NS","ADANITRANS.NS","AFFLE.NS","AIAENG.NS","AKZOINDIA.NS","ALKYLAMINE.NS","ASIANPAINT.NS","ASTRAL.NS","ATGL.NS","ATUL.NS","BAJFINANCE.NS","BERGEPAINT.NS","BHARATRAS.NS","BRITANNIA.NS","CHAMBLFERT.NS","CHOLAFIN.NS","COFORGE.NS","CROMPTON.NS","DABUR.NS","DIXON.NS","DMART.NS","FINEORG.NS","GARFIBRES.NS","GMMPFAUDLR.NS","GODREJPROP.NS","GRSE.NS","HAVELLS.NS","HDFC.NS","HDFCBANK.NS","HDFCLIFE.NS","HEIDELBERG.NS","HINDUNILVR.NS","HINDZINC.NS","HONAUT.NS","HUHTAMAKI.NS","ICICIGI.NS","ICICIPRULI.NS","IGL.NS","INDIAMART.NS","INDUSTOWER.NS","INFY.NS","IRCTC.NS","KANSAINER.NS","KOTAKBANK.NS","LTI.NS","LTTS.NS","MANAPPURAM.NS","MARICO.NS","METROPOLIS.NS","MIDHANI.NS","MUTHOOTFIN.NS","NAUKRI.NS","NAVINFLUOR.NS","ORIENTELEC.NS","PGHL.NS","PHOENIXLTD.NS","PIDILITIND.NS","PIIND.NS","POLYCAB.NS","POLYPLEX.NS","POWERGRID.NS","POWERINDIA.NS","RAMCOCEM.NS","RATNAMANI.NS","RELAXO.NS","RELIANCE.NS","SANOFI.NS","SBICARD.NS","SOLARA.NS","SONATSOFTW.NS","SRF.NS","STLTECH.NS","SUMICHEM.NS","SUPREMEIND.NS","SUVENPHAR.NS","SYNGENE.NS","TASTYBITE.NS","TATACONSUM.NS","TATAINVEST.NS","TCIEXP.NS","TCS.NS","TIINDIA.NS","TITAN.NS","TORNTPOWER.NS","TRENT.NS","VBL.NS","VINATIORGA.NS","VOLTAS.NS","WESTLIFE.NS","WHIRLPOOL.NS","WIPRO.NS"]
    
for stock in range(0,len(stock_list)):
    my_stock_price(stock_list[stock])