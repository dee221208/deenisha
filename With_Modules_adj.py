import pandas as pd
import yahoo_fin.stock_info as si

pd.set_option('display.max_columns',100)
pd.set_option('display.max_rows', 100)

def final_print(stock_nm,opm,book_per_share,promoter_hold,roe,eps,cmp,avg_price):
    print (stock_nm,opm,book_per_share,promoter_hold,roe,eps,cmp,avg_price)
    
def resonable_valuation (stock_nm,opm,book_per_share,promoter_hold,roe,eps):
    #print("stock name is 2 ",stock_nm)
    #print("opm is pass 2 ",opm)
    stock_nm="ACC.NS"
    stock_stats = si.get_stats(stock_nm)
    low_52=float(stock_stats[stock_stats.Attribute=='52 Week Low 3'].Value.item())
    dma_200=float(stock_stats[stock_stats.Attribute=='200-Day Moving Average 3'].Value.item())
    #print("low",low_52)
    #print("200dma",dma_200)
    avg_price=(low_52+dma_200)/2
    cmp=si.get_live_price(stock_nm)
    
    final_print (stock_nm,opm,book_per_share,promoter_hold,roe,eps,cmp,avg_price)
    
    #if cmp <= (avg_price + avg_price* (20/100)):
        #final_print(stock_nm,opm,avg_price,cmp)
    #else:
        #print("cmp is " ,cmp,"avg",avg_price )
  
def opm_book_val_promoter_hold_roe_eps(stock_nm):
    #print("stock name is 1 ",stock_nm)
    #stock_nm="ACC.NS"
    stock_stats = si.get_stats(stock_nm)
    opm=float(stock_stats[stock_stats.Attribute=='Profit Margin'].Value.item().replace('%', ''))
    book_per_share=float(stock_stats[stock_stats.Attribute=='Book Value Per Share (mrq)'].Value.item())
    promoter_hold=float(stock_stats[stock_stats.Attribute=='% Held by Insiders 1'].Value.item().replace('%', ''))
    roe=float(stock_stats[stock_stats.Attribute=='Return on Equity (ttm)'].Value.item().replace('%', ''))
    eps=float(stock_stats[stock_stats.Attribute=='Diluted EPS (ttm)'].Value.item())   
    
    if opm >=0 and book_per_share>=0 and promoter_hold>=45 and roe>=10 and eps>=0 :
        resonable_valuation(stock_nm,opm,book_per_share,promoter_hold,roe,eps)
        #print("opm is pass",opm)
        #print("stock_nm is pass",stock_nm)
    #else:
        #print("opm is ",opm)
        
        
    
stock_list=["ACC.NS"]
for stock in range(0,len(stock_list)):
    opm_book_val_promoter_hold_roe_eps(stock_list[stock])
    

    
