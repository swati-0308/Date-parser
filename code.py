import datefinder
 
string_with_dates = '''
  The meeting is scheduled for June 30.
  The meeting is scheduled for the 30th of June.
  We have had tricks played on us on April 1.
  The 1st of April puts some people on edge.  
  You are expecting me on coming wednesday.
  We expect to deliver this between late 2021 and early 2022.
  I will  arrive either in 3rd october or 4th nov
  Please deliver the package by August 1.
  I received the packet before Monday.
  since 2000.
  I will receive the packet on 19.08.2020.
 
'''  
 
 
i=0
dic=[]
matches = datefinder.find_dates(string_with_dates)
for match in matches:
   print(match)
   dic.append(match)

import pandas as pd
d={}
d["start"]=dic
df=pd.DataFrame(d)
df.info()
 
df['date']=pd.DatetimeIndex(df.start).date
df['year']=pd.DatetimeIndex(df.start).year
df['day']=pd.DatetimeIndex(df.start).day
df['month']=pd.DatetimeIndex(df.start).month
df['em']='jan'
 
i=0
for i in range(0,len(df)):
 t=df.at[i,'month']
 if (t==1):
   df.at[i,'em']='jan'
 elif (t==2):
   df.at[i,'em']='Feb'
 elif (t==3):
   df.at[i,'em']='March'
 elif (t==4):
   df.at[i,'em']='April'
 elif (t==5):
   df.at[i,'em']='May' 
 elif (t==6):
   df.at[i,'em']='June'
 elif (t==7):
   df.at[i,'em']='July' 
 elif (t==8):
   df.at[i,'em']='Aug'
 elif (t==9):
   df.at[i,'em']='Sept'
 elif (t==10):
   df.at[i,'em']='oct'
 elif (t==11):
   df.at[i,'em']='Nov'              
 else: 
   df.at[i,'em']='Dec'
 i=i+1 
df
