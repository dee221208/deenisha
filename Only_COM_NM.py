# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 10:45:19 2021

@author: Deepan
"""
import glob
import pandas as pd
from win32com.client import Dispatch
xl = Dispatch('Excel.Application')
files = glob.glob(r'C:\Users\Deepan\Documents\GitHub\deenisha\screener_model_building\as_of_02_01_2021\*.xlsx*')
files
df = pd.DataFrame()
df_summary = pd.DataFrame()
df_summary_curr = pd.DataFrame()
df_summary_sing = pd.DataFrame()

bse_indus=pd.read_csv(r'C:\Users\Deepan\Documents\GitHub\deenisha\screener_model_building\Equity.csv')
bse_indus=bse_indus.drop(['Security Code', 'Security Id', 'Status', 'Group', 'Face Value', 'ISIN No', 'Instrument'], axis = 1)


for f in files:
    wb = xl.Workbooks.Open(f)
    print("Working on file :",f)
    wb.RefreshAll()  
    wb.Close(True)
    #data = pd.read_excel(f, 'Python')
    data_summary_curent = pd.read_excel(f, 'Current_Feature')
    COM_NM=data_summary_curent['COM_NM']

   
    df_summary_curr = df_summary_curr.append(COM_NM)

df_summary_curr.to_excel(r'C:\Users\Deepan\Documents\GitHub\deenisha\screener_model_building\NAMES.xls', index = False)

print ("Completed all the reports")