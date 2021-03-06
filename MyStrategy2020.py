import pandas as pd
import yahoo_fin.stock_info as si

pd.set_option('display.max_columns',100)
pd.set_option('display.max_rows', 100)



nse_500=pd.read_csv(r"C:\Users\Deepan\Documents\GitHub\deenisha\ind_nifty500list.csv")


df = pd.DataFrame()
screener_plus="stock_nm,buy_price_gap_pct"

def my_stock_rank(stock_nm):
    #print(stock_nm)
    stock_nm="NESTLEIND.NS"
    stock_stats = si.get_stats(stock_nm)
    low_52=float(stock_stats[stock_stats.Attribute=='52 Week Low 3'].Value.item())
    dma_200=float(stock_stats[stock_stats.Attribute=='200-Day Moving Average 3'].Value.item())
    avg_price=(low_52+dma_200)/2
    cmp=si.get_live_price(stock_nm)
    buy_price_gap=((cmp-avg_price)/avg_price) * 100
    #print (buy_price_gap)
    curr_row=stock_nm+','+ str(round(buy_price_gap,2))
    print (curr_row)
    #df = df.append(curr_row)
    
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
    revenue.sort_index()
    end_value = float(revenue.iloc[0])
    mcap=stock_stats[stock_stats.Attribute=='Market Cap (intraday) 5'].Value.item()
    
    if mcap.find("T") == -1:
        print("No 'is' here!")
    else:
        print("Found 'is' in the string.")
 


stock_list=["RENUKA.NS","NESTLEIND.NS"]
for stock in range(0,len(stock_list)):
    my_stock_rank(stock_list[stock])
    
    
    stock_stats = si.get_stats("NESTLEIND.NS")