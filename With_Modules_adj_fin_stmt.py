import pandas as pd
import yahoo_fin.stock_info as si

pd.set_option('display.max_columns',100)
pd.set_option('display.max_rows', 100)


def financial_stmt_checks(stock_nm):
    stock_nm="VSTIND.NS"
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
    net_prof=income_statement_df['netIncomeApplicableToCommonShares']
    #op_exp=income_statement_df['totalOperatingExpenses']
    
    #########Aggregation##########
    tot_revenue=income_statement_df['totalRevenue'].sum()
    tot_exp=income_statement_df['totalOperatingExpenses'].sum()
    tot_np=income_statement_df['netIncomeFromContinuingOps'].sum()
    avg_revenue=income_statement_df['totalRevenue'].mean()
    
    cfo=cash_flow_statement_df['totalCashFromOperatingActivities']
    CCFO=cfo.sum()
    CNPAT=income_statement_df['netIncomeApplicableToCommonShares'].sum()
    CCFO_to_CNPAT=round(CCFO/CNPAT,2)
    
    
    ebit=income_statement_df['ebit'].sort_index()
    net_prof_sort=income_statement_df['netIncomeApplicableToCommonShares'].sort_index()
    
    ebit_to_net_prof=(ebit/net_prof_sort)
    avg_ebit_to_net_prof=ebit_to_net_prof.mean()
    
    #tot_int=income_statement_df['interestExpense'].sum()
    
    #############################
    
    if "netReceivables" in balance_sheet_df:
        avg_recei=balance_sheet_df['netReceivables'].mean()
        avg_recei_latest=balance_sheet_df['netReceivables']
    else:
        #print ("notfound")
        avg_recei_df = revenue
        avg_recei_df = avg_recei_df.replace(avg_recei_df, 0)
        avg_recei=avg_recei_df.mean()
        avg_recei_latest=avg_recei_df
        
    revenue.sort_index()
    pat.sort_index()
    nprof.sort_index()
    net_prof.sort_index()
    
    def int_to_net_prof_lt():
        tot_int=income_statement_df['interestExpense'].sum()
        if tot_int ==0:
            tot_int=0.001
            
        if (tot_int/CNPAT) <= 0.5:
            print ("All checks passed", stock_nm)
    
    def ebit_to_net_prof_check():
        latest_ebit_to_net_prof = float(ebit_to_net_prof.iloc[-1])
        if latest_ebit_to_net_prof >= (avg_ebit_to_net_prof - (avg_ebit_to_net_prof*10/100)):
            #print ("All checks passed")
            int_to_net_prof_lt()
            
        
        
    def Ccfo_to_Cpat():
        if CCFO_to_CNPAT > 0.8:
            #print ("All checks passed")
            ebit_to_net_prof_check()
        
    def receivables_sales():
        if avg_recei <= ((avg_revenue*30)/100):
            #print ("All checks passed")
            Ccfo_to_Cpat()
        
        
    def net_prof_sales_gt_8pct():
        if tot_np >= ((tot_revenue*8)/100):
            receivables_sales()
        
    def expense_less_sales():
        if tot_revenue>=tot_exp:
            net_prof_sales_gt_8pct()

    
    def net_prof_growth():
        print ("inside net_prof_growth" )
        end_value = float(net_prof.iloc[0])
        start_value = float(net_prof.iloc[-1])
        num_periods = len(net_prof)

        if end_value < 0:
            end_value=0.001
        else:
            end_value=end_value

        if start_value <= 0:
            start_value=0.001
        else:
            start_value=start_value

        if start_value == end_value:
            net_prof_grw=0
        else:
            net_prof_grw=((end_value / start_value) ** (1 / (num_periods )) - 1)*100
            print ("Net profit growth", net_prof_grw)
        if int(net_prof_grw) > 7:
            expense_less_sales()
            #net_prof_growth()
    def income_stmt():
        print ("income",avg_recei)
        net_prof_growth()
        balance_sheet()
    def balance_sheet():
        print ("balance",avg_recei)
        cashflow_stmt()
    def cashflow_stmt():
        print ("cashflow",avg_recei)
    def dummy():
        net_prof_growth()
        
    dummy()
    
    
stock_list=["DEVIT.NS","GLOBAL.NS","PKTEA.NS","SVLL.NS","BEDMUTHA.NS","KSOLVES.NS","NILASPACES.NS","SHIVAUM.NS","KRITIKA.NS","RSSOFTWARE.NS","SHRADHA.NS","BAGFILMS.NS","MTEDUCARE.NS","SIL.NS","AVG.NS","MAHICKRA.NS","SRPL.NS","TEXMOPIPES.NS","INDOSOLAR.NS","SICAGEN.NS","SONAMCLOCK.NS","OSWALSEEDS.NS","SAGARDEEP.NS","IZMO.NS","ARSSINFRA.NS","SUPREMEENG.NS","REMSONSIND.NS","LOKESHMACH.NS","CMICABLES.NS","GLOBE.NS","GANGESSECU.NS","DSSL.NS","NITIRAJ.NS","CORDSCABLE.NS","KEYFINSERV.NS","BDR.NS","KALYANIFRG.NS","JAKHARIA.NS","MANAKALUCO.NS","PRESSMN.NS","DCM.NS","SPMLINFRA.NS","ACCURACY.NS","UJAAS.NS","GARDENSILK.NS","IL&FSENGG.NS","ALMONDZ.NS","BANKA.NS","IMAGICAA.NS","TIRUPATI.NS","MITCON.NS","TOUCHWOOD.NS","MANAKCOAT.NS","STEELCITY.NS","MALUPAPER.NS","MORARJEE.NS","GAL.NS","AARON.NS","SURYALAXMI.NS","PATINTLOG.NS","ORTINLABSS.NS","HOVS.NS","SANGINITA.NS","INDBANK.NS","PANACHE.NS","TREJHARA.NS","ENERGYDEV.NS","ALKALI.NS","MEGASOFT.NS","ONEPOINT.NS","HPIL.NS","SHREERAMA.NS","ARCHIES.NS","MRO.NS","NECCLTD.NS","WFL.NS","MCDHOLDING.NS","EDUCOMP.NS","LAMBODHARA.NS","HISARMETAL.NS","MAJESCO.NS","ARVEE.NS","GODHA.NS","PAR.NS","TARACHAND.NS","MADHUCON.NS","ANIKINDS.NS","SURANASOL.NS","PALASHSECU.NS","NEXTMEDIA.NS","LIBAS.NS","AARVEEDEN.NS","RAJSREESUG.NS","BANG.NS","WIPL.NS","CENTEXT.NS","ANSALHSG.NS","FLEXITUFF.NS","PALREDTEC.NS","ASAL.NS","SAMBHAAV.NS","ZENITHEXPO.NS","AIROLAM.NS","CINEVISTA.NS","MDL.NS","SERVOTECH.NS","XPROINDIA.NS","KRIDHANINF.NS","INDOWIND.NS","BHANDARI.NS","PANSARI.NS","VINNY.NS","MHHL.NS","OISL.NS","BANARBEADS.NS","MADHAV.NS","KANANIIND.NS","SALONA.NS","UNIVASTU.NS","DIAPOWER.NS","SHAIVAL.NS","AMDIND.NS","RAJMET.NS","PNC.NS","DBSTOCKBRO.NS","KERNEX.NS","SILGO.NS","AAATECH.NS","SALSTEEL.NS","LEXUS.NS","BVCL.NS","VIVIDHA.NS","DIGJAMLTD.NS","PEARLPOLY.NS","BSL.NS","ASCOM.NS","MKPL.NS","MANUGRAPH.NS","SOMICONVEY.NS","AGROPHOS.NS","SANGHVIFOR.NS","SUPREMEINF.NS","KSK.NS","MERCATOR.NS","ORIENTALTL.NS","VARDMNPOLY.NS","SIMBHALS.NS","JITFINFRA.NS","SARVESHWAR.NS","LGHL.NS","PARABDRUGS.NS","BLBLIMITED.NS","MOKSH.NS","SUMEETINDS.NS","KGL.NS","TIRUPATIFL.NS","GOENKA.NS","SUMIT.NS","COX&KINGS.NS","DELTAMAGNT.NS","RMCL.NS","TREEHOUSE.NS","KHFM.NS","RMDRIP.NS","ABMINTLTD.NS","AUTOLITIND.NS","ARCOTECH.NS","NAGREEKEXP.NS","SHIVAMILLS.NS","EXCEL.NS","COUNCODOS.NS","AJOONI.NS","INDOTHAI.NS","BEARDSELL.NS","UNIINFO.NS","TMRVL.NS","JINDALPHOT.NS","HINDCON.NS","ATLASCYCLE.NS","RELIABLE.NS","ARTNIRMAN.NS","SHANTI.NS","KEERTI.NS","AURDIS.NS","CUBEXTUB.NS","CELEBRITY.NS","SUPERSPIN.NS","LATTEYS.NS","UCL.NS","TIMESGTY.NS","SILLYMONKS.NS","TIJARIA.NS","GANGAFORGE.NS","GTNIND.NS","SHIRPUR-G.NS","DCI.NS","HECPROJECT.NS","PROLIFE.NS","AISL.NS","METALFORGE.NS","AMBANIORG.NS","NITINFIRE.NS","BCONCEPTS.NS","AGRITECH.NS","ANKITMETAL.NS","GOLDSTAR.NS","MIC.NS","SECL.NS","WILLAMAGOR.NS","GLOBOFFS.NS","KHANDSE.NS","SGL.NS","KSHITIJPOL.NS","RKDL.NS","VERA.NS","JPOLYINVST.NS","LPDC.NS","FOCUS.NS","BALKRISHNA.NS","VSCL.NS","MILTON.NS","PRITI.NS","HUSYSLTD.NS","BURNPUR.NS","LFIC.NS","FOURTHDIM.NS","INFOMEDIA.NS","3PLAND.NS","PATSPINLTD.NS","SHUBHLAXMI.NS","ARIHANT.NS","GOLDTECH.NS","UNITEDPOLY.NS","MMNL.NS","CNOVAPETRO.NS","ZODIAC.NS","LAGNAM.NS","DHARSUGAR.NS","BILENERGY.NS","CASTEXTECH.NS","VASWANI.NS","ATALREAL.NS","ADL.NS","SIGMA.NS","ADROITINFO.NS","CANDC.NS","FELIX.NS","MAGNUM.NS","UNITY.NS","ROML.NS","MARSHALL.NS","WEWIN.NS","KKVAPOW.NS","MOHOTAIND.NS","SHAHALLOYS.NS","SONAHISONA.NS","CADSYS.NS","MANGTIMBER.NS","GICL.NS","TGBHOTELS.NS","ROHITFERRO.NS","INDLMETER.NS","CALSOFT.NS","INNOVATIVE.NS","AVSL.NS","NARMADA.NS","MUKANDENGG.NS","AVROIND.NS","PRAKASHSTL.NS","SURANI.NS","SIKKO.NS","BRIGHT.NS","JETFREIGHT.NS","ZODJRDMKJ.NS","EMCO.NS","KARMAENG.NS","GAYAHWS.NS","HILTON.NS","SOLEX.NS","LAXMICOT.NS","SANCO.NS","SETUINFRA.NS","VICEROY.NS","PREMIER.NS","NATNLSTEEL.NS","MITTAL.NS","SEPOWER.NS","SEZAL.NS","SRIRAM.NS","LYPSAGEMS.NS","UWCSL.NS","NKIND.NS","PERFECT.NS","DQE.NS","HAVISHA.NS","BARTRONICS.NS","SSINFRA.NS","VCL.NS","ASLIND.NS","EASTSILK.NS","NORBTEAEXP.NS","21STCENMGM.NS","MASKINVEST.NS","JETKNIT.NS","AHIMSA.NS","NANDANI.NS","TECHNOFAB.NS","ZENITHSTL.NS","RAJRAYON.NS","WSI.NS","SYNCOM.NS","BTML.NS","AMJUMBO.NS","BSELINFRA.NS","CONTI.NS","ACEINTEG.NS","DSML.NS","SECURCRED.NS","ALCHEM.NS","ONELIFECAP.NS","SUBCAPCITY.NS","SOMATEX.NS","ZICOM.NS","MOHITIND.NS","EASUNREYRL.NS","GUJRAFFIA.NS","BKMINDST.NS","CREATIVEYE.NS","ACCORD.NS","ABNINT.NS","CROWN.NS","SKSTEXTILE.NS","POWERFUL.NS","PIGL.NS","NAGREEKCAP.NS","GTNTEX.NS","SUJANAUNI.NS","SONISOYA.NS","TVVISION.NS","ABINFRA.NS","SHYAMTEL.NS","UMESLTD.NS","EUROTEXIND.NS","PULZ.NS","NTL.NS","OMFURN.NS","MINDPOOL.NS","SPENTEX.NS","NIRAJISPAT.NS","TFL.NS","DNAMEDIA.NS","ALPSINDUS.NS","MPTODAY.NS","CHROMATIC.NS","GFSTEELS.NS","GLFL.NS","TCIFINANCE.NS","KALYANI.NS","RADAAN.NS","TRANSWIND.NS","VIJIFIN.NS","LAKPRE.NS","KAUSHALYA.NS","EUROCERA.NS","S&SPOWER.NS","METKORE.NS","DRL.NS","INTEGRA.NS","ORCHPHARMA.NS","THIRUSUGAR.NS","CMMIPL.NS","BHALCHANDR.NS","HBSL.NS","TNTELE.NS","EUROMULTI.NS","SMPL.NS","TECHIN.NS","JALAN.NS","SMVD.NS","ORTEL.NS","ARENTERP.NS","CYBERMEDIA.NS","TANTIACONS.NS","MELSTAR.NS","GRETEX.NS","RAMSARUP.NS","DCMFINSERV.NS","VASA.NS","PRADIP.NS","MANAV.NS","CKPLEISURE.NS","GISOLUTION.NS","GBGLOBAL.NS","THOMASCOTT.NS","PAEL.NS","BOHRA.NS","JAINSTUDIO.NS","HOTELRUGBY.NS","JAIHINDPRO.NS","SABEVENTS.NS" ]
for stock in range(0,len(stock_list)):
    financial_stmt_checks(stock_list[stock])