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
    data_summary = pd.read_excel(f, 'Features')
    data_summary_curent = pd.read_excel(f, 'Current_Feature')
    data_summary_single = pd.read_excel(f, 'SingleCompany')
    #df_merge_difkey = pd.merge(data, bse_indus, left_on='COM_NM', right_on='SECURITY_NAME')
    df_merge_difkey_summary = pd.merge(data_summary, bse_indus, left_on='COM_NM', right_on='SECURITY_NAME')
    df_merge_difkey_summary_curr = pd.merge(data_summary_curent, bse_indus, left_on='COM_NM', right_on='SECURITY_NAME')
    df_merge_difkey_summary_sing = pd.merge(data_summary_single, bse_indus, left_on='COM_NM', right_on='SECURITY_NAME')
    #df = df.append(df_merge_difkey)
    df_summary = df_summary.append(df_merge_difkey_summary)
    df_summary_curr = df_summary_curr.append(df_merge_difkey_summary_curr)
    df_summary_sing = df_summary_sing.append(df_merge_difkey_summary_sing)
#df_summary.head(4)
#df.to_excel(r'C:\Users\Deepan\Documents\GitHub\deenisha\screener_model_building\All_Companies_Dataset.xls', index = False)
df_summary=df_summary.drop(['SECURITY_NAME'],axis=1)
df_summary.to_excel(r'C:\Users\Deepan\Documents\GitHub\deenisha\screener_model_building\All_Companies_Dataset.xls', index = False)

df_summary_curr=df_summary_curr.drop(['SECURITY_NAME'],axis=1)
df_summary_curr.to_excel(r'C:\Users\Deepan\Documents\GitHub\deenisha\screener_model_building\All_Companies_current_Dataset.xls', index = False)

df_summary_sing=df_summary_sing.drop(['SECURITY_NAME'],axis=1)
df_summary_sing.to_excel(r'C:\Users\Deepan\Documents\GitHub\deenisha\screener_model_building\All_Companies_single_Dataset.xls', index = False) 

print ("Completed all the reports")