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

bse_indus=pd.read_csv(r'C:\Users\Deepan\Desktop\Screener Scrapping\Equity.csv')
bse_indus=bse_indus.drop(['Security Code', 'Security Id', 'Status', 'Group', 'Face Value', 'ISIN No', 'Instrument'], axis = 1)


for f in files:
    wb = xl.Workbooks.Open(f)
    print("Working on file :",f)
    wb.RefreshAll()  
    wb.Close(True)
    data = pd.read_excel(f, 'Python')
    data_summary = pd.read_excel(f, 'Python_Summary')
    df_merge_difkey = pd.merge(data, bse_indus, left_on='COM_NM', right_on='SECURITY_NAME')
    df_merge_difkey_summary = pd.merge(data_summary, bse_indus, left_on='COM_NM', right_on='SECURITY_NAME')
    df = df.append(df_merge_difkey)
    df_summary = df_summary.append(df_merge_difkey_summary)
df.head(4)
df.to_excel(r'C:\Users\Deepan\Desktop\Screener Scrapping\Screener_scrap_output.xls', index = False)
df_summary.to_excel(r'C:\Users\Deepan\Desktop\Screener Scrapping\Screener_scrap_Summary.xls', index = False) 

print ("Completed all the reports")