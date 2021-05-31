from tkinter import *
import pandas as pd
import yahoo_fin.stock_info as si
import math

pd.set_option('display.max_columns',100)
pd.set_option('display.max_rows', 100)

nse_500=pd.read_csv(r"C:\Users\Deepan\Documents\GitHub\deenisha\ind_nifty500list.csv")

##################################################
#			Declaration
###################################################

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
base_validation=0
selected_list=[]
val_ebit_to_net_prof=0

def my_stock_price(stock_nm):

    #stock_nm="DMART.NS"
    
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
        #print ("notfound")
        short_debt = revenue
        short_debt = short_debt.replace(short_debt, 0)
    
        
    if "longTermDebt" in balance_sheet_df:
        long_debt=balance_sheet_df['longTermDebt']
    else:
        long_debt = revenue
        long_debt = long_debt.replace(long_debt, 0)
    
    total_debt=short_debt+long_debt
	
	
    ebit=income_statement_df['ebit'].sort_index()
    net_prof_sort=income_statement_df['netIncomeApplicableToCommonShares'].sort_index()
    
    ebit_to_net_prof=(ebit/net_prof_sort)
    avg_ebit_to_net_prof=ebit_to_net_prof.mean()
	
	
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
        
    if CCFO_to_CNPAT > 0.75:
        ccflo_to_cnpat_score=1
    else:
        ccflo_to_cnpat_score=0
        
    if total_debt_mean < total_rev_mean_20_pct or total_debt_grw <=(rev_simple - (rev_simple*(10/100))) or total_debt_grw <0 :
        debt_score=1
    else:
        debt_score=0
		
    latest_ebit_to_net_prof = float(ebit_to_net_prof.iloc[-1])
    if latest_ebit_to_net_prof >= (avg_ebit_to_net_prof - (avg_ebit_to_net_prof*15/100)):
        val_ebit_to_net_prof=1
    else:
        val_ebit_to_net_prof=0
    #stock_nm="NESTLEIND.NS"
    stock_stats = si.get_stats(stock_nm)
    opm=float(stock_stats[stock_stats.Attribute=='Profit Margin'].Value.item().replace('%', ''))
    book_per_share=float(stock_stats[stock_stats.Attribute=='Book Value Per Share (mrq)'].Value.item())

    if isinstance(stock_stats[stock_stats.Attribute=='% Held by Insiders 1'].Value.item(), str):
        promoter_hold=float(stock_stats[stock_stats.Attribute=='% Held by Insiders 1'].Value.item().replace('%', ''))
    elif math.isnan(stock_stats[stock_stats.Attribute=='% Held by Insiders 1'].Value.item()):
        promoter_hold=46
    else:
        promoter_hold=float(stock_stats[stock_stats.Attribute=='% Held by Insiders 1'].Value.item().replace('%', ''))
    
    if isinstance(stock_stats[stock_stats.Attribute=='Return on Equity (ttm)'].Value.item(), str):
        roe=float(stock_stats[stock_stats.Attribute=='Return on Equity (ttm)'].Value.item().replace('%', ''))
    elif math.isnan(stock_stats[stock_stats.Attribute=='Return on Equity (ttm)'].Value.item()):
        roe=10
    else:
        roe=float(stock_stats[stock_stats.Attribute=='Return on Equity (ttm)'].Value.item().replace('%', ''))
    eps=float(stock_stats[stock_stats.Attribute=='Diluted EPS (ttm)'].Value.item())   
    
    if opm >=0 and book_per_share>=0 and promoter_hold>=45 and roe>=10 and eps>=0 :
        #print(stock_nm,opm,book_per_share,promoter_hold,roe,eps)
        base_validation=1
    else:
        base_validation=0

    total_score=(rev_score+pat_score+nprof_score+avg_rec_score+roe_score+avg_prof_cap_emp_score+cfo_score+cfo_gt_10_score+ccflo_to_cnpat_score+debt_score+val_ebit_to_net_prof)
    
    if total_score >=9 and base_validation>0 :
        print (stock_nm, "Good For Investment" , total_score)
        selected_list.append(stock_nm)
    else:
        print (stock_nm,"failed")
#stock_list=["NESTLEIND.NS"]         
#stock_list=["3MINDIA.NS","ABB.NS","POWERINDIA.NS","ACC.NS","AIAENG.NS","APLAPOLLO.NS","AUBANK.NS","AARTIDRUGS.NS","AARTIIND.NS","AAVAS.NS","ABBOTINDIA.NS","ADANIENT.NS","ADANIGREEN.NS","ADANIPORTS.NS","ATGL.NS","ADANITRANS.NS","ABCAPITAL.NS","ABFRL.NS","ADVENZYMES.NS","AEGISCHEM.NS","AJANTPHARM.NS","AKZOINDIA.NS","ALEMBICLTD.NS","APLLTD.NS","ALKEM.NS","ALKYLAMINE.NS","ALOKINDS.NS","AMARAJABAT.NS","AMBER.NS","AMBUJACEM.NS","APOLLOHOSP.NS","APOLLOTYRE.NS","ASHOKLEY.NS","ASHOKA.NS","ASIANPAINT.NS","ASTERDM.NS","ASTRAZEN.NS","ASTRAL.NS","ATUL.NS","AUROPHARMA.NS","AVANTIFEED.NS","DMART.NS","AXISBANK.NS","BASF.NS","BEML.NS","BSE.NS","BAJAJ-AUTO.NS","BAJAJCON.NS","BAJAJELEC.NS","BAJFINANCE.NS","BAJAJFINSV.NS","BAJAJHLDNG.NS","BALKRISIND.NS","BALMLAWRIE.NS","BALRAMCHIN.NS","BANDHANBNK.NS","BANKBARODA.NS","BANKINDIA.NS","MAHABANK.NS","BATAINDIA.NS","BAYERCROP.NS","BERGEPAINT.NS","BDL.NS","BEL.NS","BHARATFORG.NS","BHEL.NS","BPCL.NS","BHARATRAS.NS","BHARTIARTL.NS","BIOCON.NS","BIRLACORPN.NS","BSOFT.NS"]

#stock_list=["BLISSGVS.NS","BLUEDART.NS","BLUESTARCO.NS","BBTC.NS","BOMDYEING.NS","BOSCHLTD.NS","BRIGADE.NS","BRITANNIA.NS","CARERATING.NS","CCL.NS","CESC.NS","CRISIL.NS","CSBBANK.NS","CADILAHC.NS","CANFINHOME.NS","CANBK.NS","CAPLIPOINT.NS","CGCL.NS","CARBORUNIV.NS","CASTROLIND.NS","CEATLTD.NS","CENTRALBK.NS","CDSL.NS","CENTURYPLY.NS","CENTURYTEX.NS","CERA.NS","CHALET.NS","CHAMBLFERT.NS","CHENNPETRO.NS","CHOLAHLDNG.NS","CHOLAFIN.NS","CIPLA.NS","CUB.NS","COALINDIA.NS","COCHINSHIP.NS","COFORGE.NS","COLPAL.NS"]
            
            
#stock_list=["CONCOR.NS","COROMANDEL.NS","CREDITACC.NS","CROMPTON.NS","CUMMINSIND.NS","CYIENT.NS","DBCORP.NS","DCBBANK.NS","DCMSHRIRAM.NS","DLF.NS","DABUR.NS","DALBHARAT.NS","DEEPAKNTR.NS","DELTACORP.NS","DHANI.NS","DHANUKA.NS","DBL.NS","DISHTV.NS","DCAL.NS","DIVISLAB.NS","DIXON.NS","LALPATHLAB.NS","DRREDDY.NS","EIDPARRY.NS","EIHOTEL.NS","EPL.NS","ESABINDIA.NS","EDELWEISS.NS","EICHERMOT.NS","ELGIEQUIP.NS","EMAMILTD.NS","ENDURANCE.NS","ENGINERSIN.NS","EQUITAS.NS","ERIS.NS","ESCORTS.NS","EXIDEIND.NS","FDC.NS","FEDERALBNK.NS","FINEORG.NS","FINCABLES.NS","FINPIPE.NS","FSL.NS","FORTIS.NS","FCONSUMER.NS","FRETAIL.NS","GAIL.NS","GEPIL.NS","GHCL.NS","GMMPFAUDLR.NS","GMRINFRA.NS","GALAXYSURF.NS","GRSE.NS","GARFIBRES.NS","GICRE.NS","GILLETTE.NS","GLAXO.NS","GLENMARK.NS","GODFRYPHLP.NS","GODREJAGRO.NS","GODREJCP.NS","GODREJIND.NS","GODREJPROP.NS","GRANULES.NS","GRAPHITE.NS","GRASIM.NS","GESHIP.NS","GREAVESCOT.NS","GRINDWELL.NS","GUJALKALI.NS","GAEL.NS"]

#stock_list=["FLUOROCHEM.NS","GUJGASLTD.NS","GMDCLTD.NS","GNFC.NS","GPPL.NS","GSFC.NS","GSPL.NS","GULFOILLUB.NS","HEG.NS","HCLTECH.NS","HDFCAMC.NS","HDFCBANK.NS","HDFCLIFE.NS","HFCL.NS","HATHWAY.NS","HATSUN.NS","HAVELLS.NS","HEIDELBERG.NS","HERITGFOOD.NS","HEROMOTOCO.NS","HSCL.NS","HINDALCO.NS","HAL.NS","HINDCOPPER.NS","HINDPETRO.NS","HINDUNILVR.NS","HINDZINC.NS","HONAUT.NS","HUDCO.NS","HDFC.NS","HUHTAMAKI.NS","ICICIBANK.NS","ICICIGI.NS","ICICIPRULI.NS","ISEC.NS","ICRA.NS","IDBI.NS","IDFCFIRSTB.NS","IDFC.NS","IFBIND.NS","IIFL.NS","IIFLWAM.NS","IOLCP.NS","IRB.NS","IRCON.NS","ITC.NS","ITI.NS","INDIACEM.NS","IBULHSGFIN.NS","IBREALEST.NS","INDIANB.NS","IEX.NS","INDHOTEL.NS","IOC.NS","IOB.NS","IRCTC.NS","INDOCO.NS","IGL.NS","INDUSTOWER.NS","INDUSINDBK.NS","NAUKRI.NS","INFY.NS","INGERRAND.NS","INOXLEISUR.NS","INDIGO.NS","IPCALAB.NS","JBCHEPHARM.NS","JKCEMENT.NS","JKLAKSHMI.NS","JKPAPER.NS","JKTYRE.NS","JMFINANCIL.NS","JSWENERGY.NS","JSWSTEEL.NS","JTEKTINDIA.NS","JAGRAN.NS","JAICORPLTD.NS","J&KBANK.NS","JAMNAAUTO.NS","JINDALSAW.NS","JSLHISAR.NS","JSL.NS","JINDALSTEL.NS","JCHAC.NS","JUBLFOOD.NS","JUSTDIAL.NS","JYOTHYLAB.NS","KEI.NS","KNRCON.NS","KRBL.NS","KSB.NS","KAJARIACER.NS","KALPATPOWR.NS","KANSAINER.NS","KTKBANK.NS","KARURVYSYA.NS","KSCL.NS","KEC.NS","KOLTEPATIL.NS","KOTAKBANK.NS","L&TFH.NS","LTTS.NS","LICHSGFIN.NS","LAOPALA.NS","LAXMIMACH.NS","LTI.NS","LT.NS","LAURUSLABS.NS","LEMONTREE.NS","LINDEINDIA.NS","LUPIN.NS","LUXIND.NS","MASFIN.NS","MMTC.NS","MOIL.NS","MRF.NS","MGL.NS","MAHSCOOTER.NS","MAHSEAMLES.NS","M&MFIN.NS","M&M.NS","MAHINDCIE.NS","MHRIL.NS","MAHLOG.NS","MANAPPURAM.NS","MRPL.NS","MARICO.NS","MARUTI.NS","MFSL.NS","METROPOLIS.NS","MINDTREE.NS","MINDACORP.NS","MINDAIND.NS","MIDHANI.NS","MOTHERSUMI.NS","MOTILALOFS.NS","MPHASIS.NS","MCX.NS","MUTHOOTFIN.NS","NATCOPHARM.NS","NBCC.NS","NCC.NS","NESCO.NS","NHPC.NS","NLCINDIA.NS","NMDC.NS","NOCIL.NS","NTPC.NS","NH.NS","NATIONALUM.NS","NFL.NS","NAVINFLUOR.NS","NAVNETEDUL.NS","NESTLEIND.NS","NETWORK18.NS","NILKAMAL.NS","NAM-INDIA.NS","OBEROIRLTY.NS","ONGC.NS","OIL.NS","OMAXE.NS","OFSS.NS","ORIENTCEM.NS","ORIENTELEC.NS","ORIENTREF.NS","PIIND.NS","PNBHOUSING.NS","PNCINFRA.NS","PSPPROJECT.NS","PTC.NS","PVR.NS","PAGEIND.NS","PERSISTENT.NS","PETRONET.NS","PFIZER.NS","PHILIPCARB.NS","PHOENIXLTD.NS","PIDILITIND.NS","PEL.NS","POLYMED.NS","POLYCAB.NS","POLYPLEX.NS","PFC.NS","POWERGRID.NS","PRAJIND.NS","PRESTIGE.NS","PRSMJOHNSN.NS","PGHL.NS","PGHH.NS","PNB.NS","QUESS.NS","RBLBANK.NS","RECLTD.NS","RITES.NS","RADICO.NS","RVNL.NS","RAIN.NS","RAJESHEXPO.NS","RALLIS.NS","RCF.NS","RATNAMANI.NS","RAYMOND.NS","REDINGTON.NS","RELAXO.NS","RELIANCE.NS","SBICARD.NS","SBILIFE.NS","SIS.NS","SJVN.NS","SKFINDIA.NS","SRF.NS","SANOFI.NS","SCHAEFFLER.NS","SCHNEIDER.NS"]

#stock_list=["SEQUENT.NS","SFL.NS","SHILPAMED.NS","SCI.NS","SHOPERSTOP.NS","SHREECEM.NS","SHRIRAMCIT.NS","SRTRANSFIN.NS","SIEMENS.NS","SOBHA.NS","SOLARINDS.NS","SOLARA.NS","SONATSOFTW.NS","SOUTHBANK.NS","SPICEJET.NS","STARCEMENT.NS","SBIN.NS","SAIL.NS","SWSOLAR.NS","STLTECH.NS","STAR.NS","SUDARSCHEM.NS","SUMICHEM.NS","SPARC.NS","SUNPHARMA.NS","SUNTV.NS","SUNDARMFIN.NS","SUNDRMFAST.NS","SUNTECK.NS","SUPRAJIT.NS","SUPREMEIND.NS","SUPPETRO.NS","SUVENPHAR.NS","SUZLON.NS","SWANENERGY.NS","SWARAJENG.NS","SYMPHONY.NS","SYNGENE.NS","TCIEXP.NS","TCNSBRANDS.NS"]

#stock_list=["TTKPRESTIG.NS","TVTODAY.NS","TV18BRDCST.NS","TVSMOTOR.NS","TASTYBITE.NS","TATACHEM.NS","TATACOFFEE.NS","TATACOMM.NS","TCS.NS","TATACONSUM.NS","TATAELXSI.NS","TATAINVEST.NS","TATAMTRDVR.NS","TATAMOTORS.NS","TATAPOWER.NS","TATASTLBSL.NS","TATASTEEL.NS","TEAMLEASE.NS","TECHM.NS","NIACL.NS","RAMCOCEM.NS","THERMAX.NS","THYROCARE.NS","TIMKEN.NS","TITAN.NS","TORNTPHARM.NS","TORNTPOWER.NS","TRENT.NS","TRIDENT.NS","TIINDIA.NS","UCOBANK.NS","UFLEX.NS","UPL.NS","UJJIVAN.NS","UJJIVANSFB.NS","ULTRACEMCO.NS","UNIONBANK.NS","UBL.NS","MCDOWELL-N.NS","VGUARD.NS","VMART.NS","VIPIND.NS","VRLLOG.NS","VSTIND.NS","VAIBHAVGBL.NS","VAKRANGEE.NS","VTL.NS","VARROC.NS","VBL.NS","VENKEYS.NS","VINATIORGA.NS"]

  
my_stock_price(e1.get())
 
master = Tk()
myText=StringVar()
Label(master, text="Enter stock code").grid(row=0, sticky=W)
Label(master, text="Second").grid(row=1, sticky=W)
Label(master, text="Result:").grid(row=3, sticky=W)
result=Label(master, text="", textvariable=myText).grid(row=3,column=1, sticky=W)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

b = Button(master, text="Calculate", command=my_stock_price)
b.grid(row=0, column=2,columnspan=2, rowspan=2,sticky=W+E+N+S, padx=5, pady=5)


mainloop()
