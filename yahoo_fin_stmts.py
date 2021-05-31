import pandas as pd
import yahoo_fin.stock_info as si

pd.set_option('display.max_columns',100)
pd.set_option('display.max_rows', 100)

nse_500=pd.read_csv(r"C:\Users\Deepan\Documents\GitHub\deenisha\ind_nifty500list.csv")

rev_score=0
pat_score=0
nprof_score=0
avg_rec_score=0
roe_score=0
avg_prof_cap_emp_score=0
cfo_score=0
cfo_gt_10_score=0
ccflo_to_cnpat_score=0
debt_score=0




#def my_stock_price(stock_nm):

stock_nm="TCS.NS"

income_statement = si.get_income_statement(stock_nm)
balance_sheet = si.get_balance_sheet(stock_nm)
cash_flow_statement = si.get_cash_flow(stock_nm)



income_statement.fillna(0, inplace=True)
income_statement=income_statement.div(10000000).astype(int)

balance_sheet.fillna(0, inplace=True)
balance_sheet=balance_sheet.div(10000000).astype(int)

cash_flow_statement.fillna(0, inplace=True)
cash_flow_statement=cash_flow_statement.div(10000000).astype(int)

income_statement_df=income_statement.transpose()
balance_sheet_df=balance_sheet.transpose()
cash_flow_statement_df=cash_flow_statement.transpose()

revenue=income_statement_df['totalRevenue']
pat=income_statement_df['incomeBeforeTax']
nprof=income_statement_df['netIncomeFromContinuingOps']

if "netReceivables" in balance_sheet_df:
    avg_recei=balance_sheet_df['netReceivables'].mean()
    avg_recei_latest=balance_sheet_df['netReceivables']
else:
    print ("notfound")
    avg_recei_df = revenue
    avg_recei_df = avg_recei_df.replace(avg_recei_df, 0)
    avg_recei=avg_recei_df.mean()
    avg_recei_latest=avg_recei_df

#avg_recei=balance_sheet_df['netReceivables'].mean()
avg_rev_20_pct=(income_statement_df['totalRevenue'].mean()*(20/100))
#avg_recei_latest=balance_sheet_df['netReceivables']

tot_share_hold=balance_sheet_df['totalStockholderEquity'].sort_index()
net_income=income_statement_df['netIncome'].sort_index()

roe=(net_income/tot_share_hold)*100
roe_mean=roe.mean()


np_share_hold=income_statement_df['netIncomeApplicableToCommonShares'].sort_index()
prof_cap_emp=(np_share_hold/tot_share_hold)*100
avg_prof_cap_emp=prof_cap_emp.mean()

cfo=cash_flow_statement_df['totalCashFromOperatingActivities']
CCFO=cfo.sum()
CNPAT=income_statement_df['netIncomeApplicableToCommonShares'].sum()
CCFO_to_CNPAT=round(CCFO/CNPAT,2)

if "shortLongTermDebt" in balance_sheet_df:
    short_debt=balance_sheet_df['shortLongTermDebt']
else:
    print ("notfound")
    short_debt = revenue
    short_debt = short_debt.replace(short_debt, 0)

    
if "longTermDebt" in balance_sheet_df:
    long_debt=balance_sheet_df['longTermDebt']
else:
    long_debt = revenue
    long_debt = long_debt.replace(long_debt, 0)

total_debt=short_debt+long_debt
# sorting.......................

revenue.sort_index()
pat.sort_index()
nprof.sort_index()
avg_recei_latest.sort_index()
cfo.sort_index()
total_debt.sort_index()


""" Values updates"""

end_value = float(revenue.iloc[0])
start_value = float(revenue.iloc[-1])
num_periods = len(revenue)

if end_value < 0:
    end_value=0.001
else:
    end_value=end_value
    
if start_value <= 0:
    start_value=0.001
else:
    start_value=start_value

if start_value == end_value:
    rev_grw=0
else:
    rev_grw=((end_value / start_value) ** (1 / (num_periods )) - 1)*100

 
end_value = float(pat.iloc[0])
start_value = float(pat.iloc[-1])
num_periods = len(pat)

if end_value < 0:
    end_value=0.001
else:
    end_value=end_value
    
if start_value <= 0:
    start_value=0.001
else:
    start_value=start_value
    
if start_value == end_value:
    pat_grw=0
else:
    pat_grw=((end_value / start_value) ** (1 / (num_periods )) - 1)*100


end_value = float(nprof.iloc[0])
start_value = float(nprof.iloc[-1])
num_periods = len(nprof)

if end_value < 0:
    end_value=0.001
else:
    end_value=end_value
    
if start_value <= 0:
    start_value=0.001
else:
    start_value=start_value
if start_value == end_value:
    nprof_grw=0
else:
    nprof_grw=((end_value / start_value) ** (1 / (num_periods )) - 1)*100



end_value = float(nprof.iloc[0])
start_value = float(nprof.iloc[-1])
num_periods = len(nprof)

if end_value < 0:
    end_value=0.001
else:
    end_value=end_value
    
if start_value <= 0:
    start_value=0.001
else:
    start_value=start_value

if start_value == end_value:
    nprof_grw=0
else:
    nprof_grw=((end_value / start_value) ** (1 / (num_periods )) - 1)*100


end_value = float(avg_recei_latest.iloc[0])
start_value = float(avg_recei_latest.iloc[-1])
num_periods = len(avg_recei_latest)

if end_value < 0:
    end_value=0.001
else:
    end_value=end_value
    
if start_value <= 0:
    start_value=0.001
else:
    start_value=start_value

if start_value == end_value:
    avg_recei_grw=0
else:
    avg_recei_grw=((end_value / start_value) ** (1 / (num_periods )) - 1)*100

latest_roe = float(roe.iloc[-1])

end_value = float(cfo.iloc[0])
start_value = float(cfo.iloc[-1])
num_periods = len(cfo)

if end_value < 0:
    end_value=0.001
else:
    end_value=end_value
    
if start_value <= 0:
    start_value=0.001
else:
    start_value=start_value
if start_value == end_value:
    cfo_grw=0
else:
    cfo_grw=((end_value / start_value) ** (1 / (num_periods )) - 1)*100





end_value = float(total_debt.iloc[0])
start_value = float(total_debt.iloc[-1])
num_periods = len(total_debt)

if start_value == 0:
    start_value=0.01
else:
    start_value=start_value
    
if start_value == end_value:
    total_debt_grw=0
else:
    total_debt_grw=((end_value / start_value) ** (1 / (num_periods )) - 1)*100



total_debt_mean=total_debt.mean()
total_rev_mean=revenue.mean()
total_rev_mean_20_pct=total_rev_mean*(20/100)

""" Values updates"""

rev_simple=rev_grw-(rev_grw*(5/100))

if rev_simple > 8:
    rev_score=1
else:
    rev_score=0
    
if pat_grw > (rev_simple - (rev_simple*(10/100))):
    pat_score=1
else:
    pat_score=0
    
if nprof_grw > (rev_simple - (rev_simple*(10/100))):
    nprof_score=1
else:
    nprof_score=0
    
if avg_recei < avg_rev_20_pct or avg_recei_grw <=(rev_simple - (rev_simple*(9/100))):
    avg_rec_score=1
else:
    avg_rec_score=0
    
if latest_roe > (roe_mean - (roe_mean*(10/100))):
    roe_score=1
else:
    roe_score=0
    
if avg_prof_cap_emp > 15 :
    avg_prof_cap_emp_score=1
else:
    avg_prof_cap_emp_score=0
    
if cfo_grw > (rev_simple - (rev_simple*(10/100))):
    cfo_score=1
else:
    cfo_score=0
    
if cfo_grw > 10:
    cfo_gt_10_score=1
else:
    cfo_gt_10_score=0
    
if CCFO_to_CNPAT > 0.8:
    ccflo_to_cnpat_score=1
else:
    ccflo_to_cnpat_score=0
    
if total_debt_mean < total_rev_mean_20_pct or total_debt_grw <=(rev_simple - (rev_simple*(10/100))) or total_debt_grw <0 :
    debt_score=1
else:
    debt_score=0
   
   



if (rev_score+pat_score+nprof_score+avg_rec_score+roe_score+avg_prof_cap_emp_score+cfo_score+cfo_gt_10_score+ccflo_to_cnpat_score+debt_score) >=8 :
    print (stock_nm, "Good For Investment")
    
else:
    print (stock_nm, "Please skip")
    
    
