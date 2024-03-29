import pandas_datareader as web
import numpy as np
import pandas as pd
from datetime import date, timedelta
import datetime
end = datetime.datetime.today()
start = datetime.date(end.year-6,9,1)

 

def my_stock_price(stock_nm):
	df=web.get_data_yahoo(stock_nm,start,interval='m')
	#df.columns
	df=df.drop(['High', 'Low', 'Open','Close','Volume'], axis = 1) 
	pd.set_option('display.max_columns',None)
	sp500=df.copy()
	Total_row=int(sp500['Adj Close'].count())
	sp500["ALL_TIME_HIGH"] = np.nan
	sp500["ALL_TIME_LOW"] = np.nan

	for val in range(0,Total_row):
		sp500['ALL_TIME_HIGH'][val]=sp500['Adj Close'].iloc[0:val+1].max()
		sp500['ALL_TIME_LOW'][val]=sp500['Adj Close'].iloc[0:val+1].min()
		#print(sp500)
		
	for val in range(0,Total_row):
		sp500['ALL_TIME_LOW']=sp500['Adj Close'].iloc[0:val].min()
		#print(sp500)

	sp500['TTM High'] = sp500['Adj Close'].rolling(window=11).max()
	sp500['TTM Low'] = sp500['Adj Close'].rolling(window=11).min()
	sp500['TTM High_adj'] = sp500['TTM High']*0.08+sp500['TTM High']
	sp500['TTM Low_adj'] = sp500['TTM Low']*0.05+sp500['TTM Low']
	sp500['TTM_TRIM_HIGH'] = np.where(sp500['Adj Close']>=sp500['TTM High_adj'], 'TRUE', 'FALSE')
	sp500['TTM_TRIM_LOW'] = np.where(sp500['Adj Close']<=sp500['TTM Low_adj'], 'TRUE', 'FALSE')
	sp500['TTM_TRIM_VAL'] = np.where(sp500['Adj Close']>=sp500['TTM High'], sp500['Adj Close'], 0)
	sp500['TTM_LOW_VAL'] = np.where(sp500['Adj Close']<=sp500['TTM Low'], sp500['Adj Close'], 0)
	sp500['ALL_TIME_HIGH_FLAG'] = np.where(sp500['Adj Close']>=sp500['ALL_TIME_HIGH'], 1, 0)
	sp500['ALL_TIME_LOW_FLAG'] = np.where(sp500['Adj Close']<=sp500['ALL_TIME_LOW'], 1, 0)
	
	sp500.dropna().head(111)
	upper_bound=int(sp500['TTM High'].count()*0.7)
	lower_bound=int(sp500['TTM High'].count()*0.3)

	first_half_high=sp500['TTM_TRIM_VAL'].head(upper_bound).max()
	second_half_high=sp500['TTM_TRIM_VAL'].tail(lower_bound).max()

	if first_half_high <= second_half_high:
		hitting_high="PASS"
	else:
		hitting_high="FAIL"
		
	#print (hitting_high)

	#=IF(MAX(J13:J47)<=IF(MAX(J48:J97)=0,MAX(J13:J47),MAX(J48:J97)),"Pass","Fail")

	first_half_low=sp500['TTM_LOW_VAL'].head(upper_bound).max()
	second_half_low=sp500['TTM_LOW_VAL'].tail(lower_bound).max()

	if (first_half_low)== np.NAN:
		hitting_low="PASS"
	elif int(first_half_low)==0:
		hitting_low="PASS"
	elif first_half_low <= second_half_low:
		hitting_low="PASS"
	else:
		hitting_low="FAIL"
	

	sp500_all_high=sp500.tail(22)
	recent_all_high=sp500_all_high['ALL_TIME_HIGH_FLAG'].sum()
	
	sp500_all_low=sp500.tail(22)
	recent_all_low=sp500_all_low['ALL_TIME_LOW_FLAG'].sum()
	
	#print("recent_all_high",recent_all_high)
	
	if recent_all_high >= 2:
		recent_all_high_status="PASS"
	else:
		recent_all_high_status="FAIL"
    
	#print("recent_all_high_status",recent_all_high_status)
	
	#print("recent_all_low",recent_all_low)
	if (recent_all_low)== 0:
		recent_all_low=1
	#print("recent_all_low",recent_all_low)
	if (recent_all_high/recent_all_low) >= 2:
		all_time_high_to_low="PASS"
	else:
		all_time_high_to_low="FAIL"
        
	#print("recent_all_low",recent_all_low)
	#print("all_time_high_to_low",all_time_high_to_low)
		
	#buy_low_cnt=int(sp500['TTM_LOW_VAL'].count())
	#sp500['TTM_LOW_VAL'].iloc[len(buy_low_cnt)-1].max()
	#print (hitting_low)
	buy_price=sp500['TTM_TRIM_LOW'].tail(1).max()
	
	#if(1==1):
	if (hitting_low=="PASS" and hitting_high=="PASS" and recent_all_high_status=="PASS" and all_time_high_to_low=="PASS"):
		print (stock_nm +','+ hitting_low +','+  hitting_high+','+recent_all_high_status+','+all_time_high_to_low+','+buy_price)

	sp500.to_excel(r'C:\Users\Deepan\Desktop\Screener Scrapping\stock_nm.xls')
    
stock_list=["LAURUSLABS.NS"]
#SMALLCAP400
#stock_list=["3MINDIA.NS","AARTIIND.NS","AAVAS.NS","ABB.NS","ABBOTINDIA.NS","ABCAPITAL.NS","ABFRL.NS","ACC.NS","ADANIGAS.NS","ADANIGREEN.NS","ADANIPORTS.NS","ADANIPOWER.NS","ADANITRANS.NS","ADVENZYMES.NS","AEGISCHEM.NS","AFFLE.NS","AIAENG.NS","AJANTPHARM.NS","AKZOINDIA.NS","ALKEM.NS","ALKYLAMINE.NS","ALLCARGO.NS","AMARAJABAT.NS","AMBER.NS","AMBUJACEM.NS","APLAPOLLO.NS","APLLTD.NS","APOLLOHOSP.NS","APOLLOTYRE.NS","ARVINDFASN.NS","ASAHIINDIA.NS","ASHOKA.NS","ASHOKLEY.NS","ASIANPAINT.NS","ASTERDM.NS","ASTRAL.NS","ASTRAZEN.NS","ATUL.NS","AUBANK.NS","AUROPHARMA.NS","AVANTIFEED.NS","AXISBANK.NS","BAJAJ-AUTO.NS","BAJAJCON.NS","BAJAJELEC.NS","BAJAJFINSV.NS","BAJAJHLDNG.NS","BAJFINANCE.NS","BALKRISIND.NS","BALMLAWRIE.NS","BALRAMCHIN.NS","BANDHANBNK.NS","BANKBARODA.NS","BANKINDIA.NS","BASF.NS","BATAINDIA.NS","BAYERCROP.NS","BBTC.NS","BDL.NS","BEL.NS","BEML.NS","BERGEPAINT.NS","BHARATFORG.NS","BHARATRAS.NS","BHARTIARTL.NS","BHEL.NS","BIOCON.NS","BIRLACORPN.NS","BLISSGVS.NS","BLUEDART.NS","BLUESTARCO.NS","BOMDYEING.NS","BOSCHLTD.NS","BPCL.NS","BRIGADE.NS","BRITANNIA.NS","BSE.NS","BSOFT.NS","CADILAHC.NS","CANBK.NS","CANFINHOME.NS","CAPLIPOINT.NS","CARBORUNIV.NS","CARERATING.NS","CASTROLIND.NS","CCL.NS","CDSL.NS","CEATLTD.NS","CENTRALBK.NS","CENTURYPLY.NS","CENTURYTEX.NS","CERA.NS","CESC.NS","CGCL.NS","CHAMBLFERT.NS","CHENNPETRO.NS","CHOLAFIN.NS","CHOLAHLDNG.NS","CIPLA.NS","COALINDIA.NS","COCHINSHIP.NS","COLPAL.NS","CONCOR.NS","COROMANDEL.NS","CREDITACC.NS","CRISIL.NS","CROMPTON.NS","CUB.NS","CUMMINSIND.NS","CYIENT.NS","DABUR.NS","DALBHARAT.NS","DBCORP.NS","DBL.NS","DCAL.NS","DCBBANK.NS","DCMSHRIRAM.NS","DEEPAKNTR.NS","DELTACORP.NS","DHANUKA.NS","DISHTV.NS","DIVISLAB.NS","DIXON.NS","DLF.NS","DMART.NS","DRREDDY.NS","ECLERX.NS","EDELWEISS.NS","EICHERMOT.NS","EIDPARRY.NS","EIHOTEL.NS","ELGIEQUIP.NS","EMAMILTD.NS","ENDURANCE.NS","ENGINERSIN.NS","EQUITAS.NS","ERIS.NS","ESABINDIA.NS","ESCORTS.NS","ESSELPACK.NS","EXIDEIND.NS","FCONSUMER.NS","FDC.NS","FEDERALBNK.NS","FINCABLES.NS","FINEORG.NS","FINPIPE.NS","FORTIS.NS","FRETAIL.NS","FSL.NS","GAIL.NS","GALAXYSURF.NS","GARFIBRES.NS","GEPIL.NS","GET&D.NS","GHCL.NS","GICRE.NS","GILLETTE.NS","GMDCLTD.NS","GMMPFAUDLR.NS","GMRINFRA.NS","GODFRYPHLP.NS","GODREJAGRO.NS","GODREJCP.NS","GODREJIND.NS","GODREJPROP.NS","GPPL.NS","GRANULES.NS","GRAPHITE.NS","GRASIM.NS","GREAVESCOT.NS","GRINDWELL.NS","GRSE.NS","GSFC.NS","GSPL.NS","GUJALKALI.NS","GUJGASLTD.NS","GULFOILLUB.NS","HAL.NS","HATHWAY.NS","HATSUN.NS","HAVELLS.NS","HCLTECH.NS","HDFC.NS","HDFCAMC.NS","HDFCBANK.NS","HDFCLIFE.NS","HEG.NS","HEIDELBERG.NS","HERITGFOOD.NS","HEROMOTOCO.NS","HEXAWARE.NS","HIMATSEIDE.NS","HINDALCO.NS","HINDCOPPER.NS","HINDPETRO.NS","HINDUNILVR.NS","HINDZINC.NS","HONAUT.NS","HSCL.NS","HUDCO.NS","IBULHSGFIN.NS","IBVENTURES.NS","ICICIBANK.NS","ICICIPRULI.NS","ICRA.NS","IDBI.NS","IDFC.NS","IDFCFIRSTB.NS","IEX.NS","IFBIND.NS","IFCI.NS","IGL.NS","IIFL.NS","IIFLWAM.NS","INDHOTEL.NS","INDIACEM.NS","INDIANB.NS","INDIGO.NS","INDOCO.NS","INDOSTAR.NS","INDUSINDBK.NS","INFIBEAM.NS","INFRATEL.NS","INFY.NS","INGERRAND.NS","INTELLECT.NS","IOB.NS","IOC.NS","IPCALAB.NS","IRB.NS","IRCON.NS","ISEC.NS","ITC.NS","ITDC.NS","ITI.NS","J&KBANK.NS","JAGRAN.NS","JAICORPLTD.NS","JAMNAAUTO.NS","JBCHEPHARM.NS","JCHAC.NS","JINDALSAW.NS","JINDALSTEL.NS","JKCEMENT.NS","JKLAKSHMI.NS","JKPAPER.NS","JKTYRE.NS","JMFINANCIL.NS","JSL.NS","JSLHISAR.NS","JSWENERGY.NS","JSWSTEEL.NS","JUBILANT.NS","JUBLFOOD.NS","JUSTDIAL.NS","JYOTHYLAB.NS","KAJARIACER.NS","KALPATPOWR.NS","KANSAINER.NS","KARURVYSYA.NS","KEC.NS","KEI.NS","KNRCON.NS","KOLTEPATIL.NS","KOTAKBANK.NS","KPITTECH.NS","KPRMILL.NS","KRBL.NS","KSB.NS","KSCL.NS","KTKBANK.NS","L&TFH.NS","LALPATHLAB.NS","LAOPALA.NS","LAURUSLABS.NS","LAXMIMACH.NS","LEMONTREE.NS","LINDEINDIA.NS","LT.NS","LTI.NS","LTTS.NS","LUPIN.NS","LUXIND.NS","M&M.NS","M&MFIN.NS","MAHINDCIE.NS","MAHLOG.NS","MAHSCOOTER.NS","MAHSEAMLES.NS","MANAPPURAM.NS","MARICO.NS","MARUTI.NS","MASFIN.NS","MCDOWELL-N.NS","MCX.NS","METROPOLIS.NS","MFSL.NS","MGL.NS","MHRIL.NS","MIDHANI.NS","MINDACORP.NS","MINDAIND.NS","MINDTREE.NS","MMTC.NS","MOIL.NS","MOTHERSUMI.NS","MOTILALOFS.NS","MPHASIS.NS","MRF.NS","MRPL.NS","MUTHOOTFIN.NS","NAM-INDIA.NS","NATCOPHARM.NS","NATIONALUM.NS","NAUKRI.NS","NAVINFLUOR.NS","NBCC.NS","NBVENTURES.NS","NCC.NS","NESCO.NS","NESTLEIND.NS","NFL.NS","NH.NS","NHPC.NS","NIACL.NS","NIITTECH.NS","NILKAMAL.NS","NLCINDIA.NS","NMDC.NS","NTPC.NS","OBEROIRLTY.NS","OFSS.NS","OIL.NS","OMAXE.NS","ONGC.NS","ORIENTCEM.NS","ORIENTELEC.NS","ORIENTREF.NS","PAGEIND.NS","PEL.NS","PETRONET.NS","PFC.NS","PFIZER.NS","PGHH.NS","PGHL.NS","PHILIPCARB.NS","PHOENIXLTD.NS","PIDILITIND.NS","PIIND.NS","PNB.NS","PNCINFRA.NS","POLYCAB.NS","POLYMED.NS","POWERGRID.NS","PRAJIND.NS","PRESTIGE.NS","PRSMJOHNSN.NS","PTC.NS","PVR.NS","QUESS.NS","RADICO.NS","RAIN.NS","RAJESHEXPO.NS","RALLIS.NS","RAMCOCEM.NS","RATNAMANI.NS","RAYMOND.NS","RBLBANK.NS","RCF.NS","RECLTD.NS","REDINGTON.NS","RELAXO.NS","RELIANCE.NS","RENUKA.NS","REPCOHOME.NS","RITES.NS","RVNL.NS","SADBHAV.NS","SAIL.NS","SANOFI.NS","SBILIFE.NS","SBIN.NS","SCHAEFFLER.NS","SCHNEIDER.NS","SCI.NS","SEQUENT.NS","SFL.NS","SHOPERSTOP.NS","SHREECEM.NS","SHRIRAMCIT.NS","SIEMENS.NS","SIS.NS","SJVN.NS","SKFINDIA.NS","SOBHA.NS","SOLARINDS.NS","SONATSOFTW.NS","SOUTHBANK.NS","SPANDANA.NS","SPARC.NS","SPICEJET.NS","SRF.NS","SRTRANSFIN.NS","STAR.NS","STARCEMENT.NS","STARCEMENT.NS","STRTECH.NS","SUDARSCHEM.NS","SUNDARMFIN.NS","SUNDRMFAST.NS","SUNPHARMA.NS","SUNTECK.NS","SUNTV.NS","SUPRAJIT.NS","SUPREMEIND.NS","SUZLON.NS","SWANENERGY.NS","SWSOLAR.NS","SYMPHONY.NS","SYNGENE.NS","TAKE.NS","TASTYBITE.NS","TATACOMM.NS","TATACONSUM.NS","TATAELXSI.NS","TATAINVEST.NS","TATAMOTORS.NS","TATAMTRDVR.NS","TATAPOWER.NS","TATASTEEL.NS","TATASTLBSL.NS","TCIEXP.NS","TCNSBRANDS.NS","TCS.NS","TEAMLEASE.NS","TECHM.NS","THERMAX.NS","THYROCARE.NS","TIINDIA.NS","TIMETECHNO.NS","TIMKEN.NS","TITAN.NS","TORNTPHARM.NS","TORNTPOWER.NS","TRENT.NS","TRIDENT.NS","TTKPRESTIG.NS","TV18BRDCST.NS","TVSMOTOR.NS","TVTODAY.NS","UBL.NS","UCOBANK.NS","UJJIVAN.NS","ULTRACEMCO.NS","UNIONBANK.NS","UPL.NS","VAIBHAVGBL.NS","VAKRANGEE.NS","VARROC.NS","VBL.NS","VEDL.NS","VENKEYS.NS","VESUVIUS.NS","VGUARD.NS","VINATIORGA.NS","VIPIND.NS","VMART.NS","VOLTAS.NS","VRLLOG.NS","VSTIND.NS","VTL.NS","WABCOINDIA.NS","WELCORP.NS","WELSPUNIND.NS","WESTLIFE.NS","WHIRLPOOL.NS","WIPRO.NS","WOCKPHARMA.NS","ZEEL.NS","ZENSARTECH.NS","ZYDUSWELL.NS"]


for stock in range(0,len(stock_list)):
    my_stock_price(stock_list[stock])