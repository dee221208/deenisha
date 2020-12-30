# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 10:11:50 2020

@author: Deepan
"""
import glob
import pandas as pd
from win32com.client import Dispatch
xl = Dispatch('Excel.Application')
files = glob.glob(r'C:\Users\Deepan\Desktop\Screener Scrapping\*xlsm*')
files
df = pd.DataFrame()
df_summary = pd.DataFrame()

#bse_indus=pd.read_csv(r'C:\Users\Deepan\Desktop\Screener Scrapping\Equity.csv')
#bse_indus=bse_indus.drop(['Security Code', 'Security Id', 'Status', 'Group', 'Face Value', 'ISIN No', 'Instrument'], axis = 1)

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

Best=['Better','BestBuy']

for f in files:
    wb = xl.Workbooks.Open(f)
    print("Working on file :",f)
    wb.RefreshAll()  
    wb.Close(True)
    data = pd.read_excel(f, 'Python')
    data_summary = pd.read_excel(f, 'Python_Summary')
    #df_merge_difkey = pd.merge(data, bse_indus, left_on='COM_NM', right_on='SECURITY_NAME')
    #df_merge_difkey_summary = pd.merge(data_summary, bse_indus, left_on='COM_NM', right_on='SECURITY_NAME')
    df = df.append(data)
    df_summary = df_summary.append(data_summary)
df.head(4)
df.to_excel(r'C:\Users\Deepan\Desktop\Screener Scrapping\Screener_scrap_output.xls', index = False)

#Applying filter on df_summary
df_copy=df_summary.copy()

df_summary=df_summary[df_summary['Score'] > 0.55]
df_summary=df_summary[df_summary['Common_Size'] > 57]
df_summary=df_summary[df_summary['Avg_Net_prof'] > 0.07]
#df_summary =df_summary[df_summary['Current'].str.contains('Be',na=False)]
df_summary =df_summary[df_summary['Current'].str.contains('Be',na=False)| df_summary['Prev'].str.contains('Be',na=False)]

df_summary.to_excel(r'C:\Users\Deepan\Desktop\Screener Scrapping\Screener_scrap_Summary.xls', index = False) 

print ("Completed all the reports")

xl.Workbooks.Open(r'C:\Users\Deepan\Desktop\Screener Scrapping\Screener_scrap_Summary.xls')