allocation={"EQ":0.75,"DEBT":0.25}
EQ_allocation={"EQ_DIR":0.60,"EQ_MF":0.40}
EQ_MF_allocation={"EQ_MF_NIFTY":0.50,"EQ_MF_NIFTY_50":0.50}
EQ_DIR_allocation={"EQ_DIR_BIG20":0.50,"EQ_DIR_NEXT20":0.25,"EQ_DIR_QUICK30":0.25}
DEBT_allocation={"DEBT_EMER":0.75,"DEBT_LIFE":0.25}

print("Allocation Summary:: ")
print ("Over all Equity allocation::",str(allocation["EQ"]*100) +'%' )
print ("Over all Debt allocation::",str(allocation["DEBT"]*100) +'%' )
print(" ")
print("Equity Allocation Summary:: ")
print ("Direct Equity allocation::",str(EQ_allocation["EQ_DIR"]*100) +'%' )
print ("MF Equity allocation::",str(EQ_allocation["EQ_MF"]*100) +'%' )
print(" ")
print("Equity Direct Allocation Summary:: ")
print ("Direct Equity allocation - Big-20::",str(EQ_DIR_allocation["EQ_DIR_BIG20"]*100) +'%' )
print ("Direct Equity allocation - Next-20::",str(EQ_DIR_allocation["EQ_DIR_NEXT20"]*100) +'%' )
print ("Direct Equity allocation- Quick-30::",str(EQ_DIR_allocation["EQ_DIR_QUICK30"]*100) +'%' )
print(" ")
print("Equity MF Allocation Summary:: ")
print ("MF Equity allocation - Nifty-50::",str(EQ_MF_allocation["EQ_MF_NIFTY"]*100) +'%' )
print ("MF Equity allocation - Next-50::",str(EQ_MF_allocation["EQ_MF_NIFTY_50"]*100) +'%' )
print(" ")
print("Debt Allocation Summary:: ")
print ("Debt Allocation - Emergency::",str(DEBT_allocation["DEBT_EMER"]*100) +'%' )
print ("Debt Allocation - LifeStyle::",str(DEBT_allocation["DEBT_LIFE"]*100) +'%' )


from datetime import datetime
def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d") 
    return abs((d2 - d1).days)

now = datetime.now() # current date and time
date_time = now.strftime("%Y-%m-%d")
No_of_Days=days_between('2020-07-06', date_time)
No_of_Months=int(No_of_Days / 31)

#Allocation Split:

EQ_DIR_BIG20_AMT=210000
EQ_DIR_NEXT20_AMT=105000
EQ_DIR_QUICK30_AMT=105000

EQ_MF_NIFTY_AMT=140000
EQ_MF_NIFTY_50_AMT=140000

#Claim from Allocation

NEW_EQ_DIR_BIG20_AMT=210000 + (11200 * No_of_Months )
NEW_EQ_DIR_NEXT20_AMT=105000 + (5600 * No_of_Months )
NEW_EQ_DIR_QUICK30_AMT=105000 + (5600 * No_of_Months )

NEW_EQ_MF_NIFTY_AMT=140000
NEW_EQ_MF_NIFTY_50_AMT=140000

print(" ")
print("Cash left for Big-20 strategy    =>  ₹", NEW_EQ_DIR_BIG20_AMT )
print("Cash left for Next-20 strategy   =>  ₹", NEW_EQ_DIR_NEXT20_AMT )
print("Cash left for Quick-30 strategy  =>  ₹", NEW_EQ_DIR_QUICK30_AMT )
print(" ")
print("Cash left for Nifty-50 Index strategy =>  ₹", NEW_EQ_MF_NIFTY_AMT )
print("Cash left for Next-50 Index strategy  =>  ₹", NEW_EQ_MF_NIFTY_50_AMT )

