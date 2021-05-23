import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import numpy as np
import calendar

path=''
years=[2017,2018,2019,2020,2021]

colorTMax=['maroon','red','darksalmon','lightsalmon','mistyrose']
colorTMin=['darkslateblue','blue','cornflowerblue','lightsteelblue','powderblue']
colorRain=['darkolivegreen','green','lime','springgreen','palegreen']
labelTMax=['TMax-17','TMax-18','TMax-19','TMax-20','TMax-21']
labelTMin=['TMin-17','TMin-18','TMin-19','TMin-20','TMin-21']
labelRain=['Rain-17','Rain-18','Rain-19','Rain-20','Rain-21']
lstyle=['-','-','-','-','-']
rain=[0,0,0,0,0]
j=0
fullDate=[[],[],[],[],[]]
plotTmax=[[],[],[],[],[]]
plotTmin=[[],[],[],[],[]]
plotFrz=[[],[],[],[],[]]
plotRain=[[],[],[],[],[]]
plotH=[[],[],[],[],[]]
for year in years:
  #print 'year',year,j
  data=pd.read_csv(path+str(year)+'.csv', na_values='-996.00')
  for i in range(0,data['YEAR'].size):
    if int(data['MONTH'][i]) >= 4 and int(data['MONTH'][i]) <=5:
      #if(int(data['DAY'][i]) <22 and int(data['YEAR'][i]) == 2019): break
      date=datetime.date(int(data['YEAR'][i]),int(data['MONTH'][i]),int(data['DAY'][i]))
      #print date.strftime('%m-%d'),data['TMAX'][i]
      fullDate[j].append(date.strftime('%m-%d'))
      #fullDate.append(datetime.date(int(data['YEAR'][i]),int(data['MONTH'][i]),int(data['DAY'][i])))
      plotTmax[j].append(data['TMAX'][i])
      plotTmin[j].append(data['TMIN'][i])
      plotFrz[j].append(32)
      rain[j]=rain[j]+data['RAIN'][i]
      plotRain[j].append(rain[j])
      plotH[j].append(data['HMAX'][i])

  #print 'j here',j
  j=j+1
  print (year,rain[j-1],"inches")

ax1=plt.subplot(212)
for i in range(0,len(lstyle)):
  plt.plot(fullDate[i],plotTmax[i],color=colorTMax[i],linestyle=lstyle[i],label=labelTMax[i])
  plt.plot(fullDate[i],plotTmin[i],color=colorTMin[i],linestyle=lstyle[i],label=labelTMin[i])

plt.plot(fullDate[0],plotFrz[0],color="black", linestyle='dashed')

plt.axvline(x=fullDate[0][30],color="black") #may 1
#plt.axvline(x=fullDate[0][61],color="black") #jun 1
#plt.axvline(x=fullDate[0][91],color="black") #jul 1
#plt.axvline(x=fullDate[0][122],color="black") #aug 1

plt.text(fullDate[0][13],25,'April')
plt.text(fullDate[0][43],25,'May')
#plt.text(fullDate[0][73],25,'June')
#plt.text(fullDate[0][104],25,'July')
#plt.text(fullDate[0][134],25,'August')

plt.xticks(rotation=90)
plt.ylabel('Temperature (F)')
plt.xlabel('Date')
plt.legend(ncol=2)
ax1.yaxis.grid(color='gray',linestyle='dashed')


ax2=plt.subplot(211)

for i in range(0,len(lstyle)):
  plt.plot(fullDate[i],plotRain[i],color=colorRain[i],linestyle=lstyle[i],label=labelRain[i])

plt.axvline(x=fullDate[0][30],color="black") #may 1
#plt.axvline(x=fullDate[0][61],color="black") #jun 1
#plt.axvline(x=fullDate[0][91],color="black") #jul 1
#plt.axvline(x=fullDate[0][122],color="black") #aug 1

plt.xticks(rotation=90)
plt.xlabel('Date')
plt.ylabel('Rain Accumulation')
plt.legend()

plt.text(fullDate[0][13],1,'April')
plt.text(fullDate[0][43],1,'May')
#plt.text(fullDate[0][73],1,'June')
#plt.text(fullDate[0][104],1,'July')
#plt.text(fullDate[0][134],1,'August')
plt.title('2017-2021 Temp and Rainfall Time Series')
ax2.yaxis.grid(color='gray',linestyle='dashed')

plt.show()
