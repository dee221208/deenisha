import pandas_datareader as web
import numpy as np
import pandas as pd
from datetime import date, timedelta
import datetime
end = datetime.datetime.today()
start = datetime.date(end.year-8,9,1)

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

"""
	Fetch historical stock price of the given security
	Add date column to the index and Year to the data set. Remove unncessary columns
	Rolling 200 days
	Calculate max price for each year. Expectation is each year's price should surpass previous year's high. 
	Arrange values in the list based on year vs sorted based on prices. When both same, stock keep raising previous year high.	
	
"""


bse_list=pd.read_csv(r"C:\Users\Deepan\Documents\GitHub\deenisha\bse_list_stocks.csv",index_col=False)
bse_list_sec_code=bse_list.drop(['Issuer Name','Security Name','Status', 'Group', 'Face Value', 'ISIN No', 'Industry', 'Instrument'],axis=1)
bse_list_sec_code.to_csv('BSE.csv', index=False)

import csv
with open('BSE.csv') as f:
    stock_dict = dict(filter(None, csv.reader(f)))
    
###################################################
## LIST VALUES

my_stock_price_step1_pass_list=[]
my_stock_price_step1_fail_list=[]

###################################################



###################################################
###NSE LIST

mcap_list=pd.read_csv(r"C:\Users\Deepan\Documents\GitHub\deenisha\MCAP.csv")
mcap_list_set=mcap_list.values.tolist()
mcap_list = [item for sublist in mcap_list_set for item in sublist]
stock_list=[]
for i in range(0,len(mcap_list)):
    try:
        #print (mcap_list[i])
        first_char=mcap_list[i][0:1]
        #print (first_char)
        first_char_series = pd.Series(first_char)
        if first_char_series.str.contains("1|2|3|4|5|6|7|8|9").bool():
            new_nm=stock_dict[mcap_list[i]]+".BO"
            #new_nm=mcap_list[i]+".BO"
        else:
            new_nm=mcap_list[i]+".NS"
    except (IOError, KeyError):
        none
    #new_nm=mcap_list[i]+".NS"
    stock_list.append(new_nm)
    
###################################################

def my_stock_price_step1(stock_nm):
    #stock_nm="HDFCBANK.NS"
    data=web.get_data_yahoo(stock_nm,start,interval='d')
    data['Date'] = data.index
    #data.info()
    #data.describe()
    data['year']=pd.DatetimeIndex(data['Date']).year
    data=data.drop(['High', 'Low', 'Open','Close','Volume'], axis = 1) 
    pd.set_option('display.max_columns',None)
    pd.set_option('display.max_rows', data.shape[0]+1) 
    #data
    #data['year']=pd.DatetimeIndex(data['Date']).year
    #long_rolling = data.rolling(window=100).mean()
    ema_200 = data.ewm(span=200, adjust=False).mean()
    #ema_200.info()
    ema_200['year_round']=ema_200['year'].round(0).astype(int)
    ema_200=ema_200.drop(['year'],axis=1)
    
    final=ema_200.groupby('year_round')['Adj Close'].max()
    final.to_frame()
    final_list=final.tolist()
    
    final_list_copy=final_list.copy()
    
    LIST=final_list
    NON_SORT_LIST=final_list_copy
    
    NON_SORT_LIST.sort()
    
    
    if LIST == NON_SORT_LIST:
        print(stock_nm,"Qualifies")
        my_stock_price_step1_pass_list.append(stock_nm)
    else:
        print(stock_nm," *** Not-Qualifies")
        my_stock_price_step1_fail_list.append(stock_nm)
  
        
def is_price_available(stock_nm):
    try:
        #counter=counter+1
        #print("Working on {}.{}").format(counter,stock_nm)
        print("Working on",stock_nm)
        web.get_data_yahoo(stock_nm,start,interval='d')
        my_stock_price_step1(stock_nm)
    except (IOError, KeyError):
        None
        
###################################################
#FUNCTION CALL
        
         
#for stock in range(0,len(stock_list)):
#    my_stock_price_step1(stock_list[stock])

#counter=0
    
for stock in range(0,len(stock_list)):
    is_price_available(stock_list[stock])
    

    
###################################################


    
###################################################
## LIST DISPLAY
    
print("Passed list:: ", my_stock_price_step1_pass_list)
print("Failed list:: ",my_stock_price_step1_fail_list)
###################################################


df = pd.DataFrame(my_stock_price_step1_pass_list, columns=["colummn"])
df.to_csv('list.csv', index=False )