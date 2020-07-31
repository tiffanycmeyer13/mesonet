import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import numpy as np
import calendar

path=''
years=[2017,2018,2019,2020]

colorTMax=['maroon','red','darksalmon','lightsalmon']
colorTMin=['darkslateblue','blue','cornflowerblue','lightsteelblue']
colorRain=['darkolivegreen','green','springgreen','palegreen']
labelTMax=['TMax-17','TMax-18','TMax-19','TMax-20']
labelTMin=['TMin-17','TMin-18','TMin-19','TMin-20']
labelRain=['Rain-17','Rain-18','Rain-19','Rain-20']
lstyle=['-','-','-','-']
rain=[0,0,0,0]
j=0
fullDate=[[],[],[],[]]
plotTmax=[[],[],[],[]]
plotTmin=[[],[],[],[]]
plotFrz=[[],[],[],[]]
plotRain=[[],[],[],[]]
plotH=[[],[],[],[]]
for year in years:
  #print 'year',year,j
  data=pd.read_csv(path+str(year)+'.csv', na_values='-996.00')
  for i in range(0,data['YEAR'].size):
    if int(data['MONTH'][i]) >= 4 and int(data['MONTH'][i]) <=8:
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
  print year,rain[j-1],"inches"

ax1=plt.subplot(212)
for i in range(0,len(lstyle)):
  plt.plot(fullDate[i],plotTmax[i],color=colorTMax[i],linestyle=lstyle[i],label=labelTMax[i])
  plt.plot(fullDate[i],plotTmin[i],color=colorTMin[i],linestyle=lstyle[i],label=labelTMin[i])

#plt.plot(fullDate[0],plotTmax[0],color="maroon",linestyle=lstyle[0],label='TMax-17')
#plt.plot(fullDate[1],plotTmax[1],color="red",linestyle=lstyle[1],label='TMax-18')
#plt.plot(fullDate[2],plotTmax[2],color="lightsalmon",linestyle=lstyle[2],label='TMax-19')
#plt.plot(fullDate[3],plotTmax[3],color="lightsalmon",linestyle=lstyle[3],label='TMax-20')
#plt.plot(fullDate[0],plotTmin[0],color="darkslateblue",linestyle=lstyle[0],label='TMin-17')
#plt.plot(fullDate[1],plotTmin[1],color="blue",linestyle=lstyle[1],label='TMin-18')
#plt.plot(fullDate[2],plotTmin[2],color="lightsteelblue",linestyle=lstyle[2],label='TMin-19')

plt.plot(fullDate[0],plotFrz[0],color="black", linestyle='dashed')

plt.axvline(x=fullDate[0][30],color="black") #may 1
plt.axvline(x=fullDate[0][61],color="black") #jun 1
plt.axvline(x=fullDate[0][91],color="black") #jul 1
plt.axvline(x=fullDate[0][122],color="black") #aug 1

plt.text(fullDate[0][13],25,'April')
plt.text(fullDate[0][43],25,'May')
plt.text(fullDate[0][73],25,'June')
plt.text(fullDate[0][104],25,'July')
plt.text(fullDate[0][134],25,'August')

plt.xticks(rotation=90)
plt.ylabel('Temperature (F)')
plt.xlabel('Date')
plt.legend(ncol=2)
ax1.yaxis.grid(color='gray',linestyle='dashed')


ax2=plt.subplot(211)

for i in range(0,len(lstyle)):
  plt.plot(fullDate[i],plotRain[i],color=colorRain[i],linestyle=lstyle[i],label=labelRain[i])

#plt.plot(fullDate[0],plotRain[0],color="darkolivegreen",linestyle=lstyle[0],label='RainAccum-17')
#plt.plot(fullDate[1],plotRain[1],color="green",linestyle=lstyle[1],label='RainAccum-18')
#plt.plot(fullDate[2],plotRain[2],color="palegreen",linestyle=lstyle[2],label='RainAccum-19')
plt.axvline(x=fullDate[0][30],color="black") #may 1
plt.axvline(x=fullDate[0][61],color="black") #jun 1
plt.axvline(x=fullDate[0][91],color="black") #jul 1
plt.axvline(x=fullDate[0][122],color="black") #aug 1

plt.xticks(rotation=90)
plt.xlabel('Date')
plt.ylabel('Rain Accumulation')
plt.legend()

plt.text(fullDate[0][13],1,'April')
plt.text(fullDate[0][43],1,'May')
plt.text(fullDate[0][73],1,'June')
plt.text(fullDate[0][104],1,'July')
plt.text(fullDate[0][134],1,'August')
plt.title('2017-2020 Temp and Rainfall Time Series')
#ax3 = ax2.twinx()
#plt.plot(fullDate[0],plotH[0],color="sandybrown",linestyle=lstyle[0],label='Humidity-17')
#plt.plot(fullDate[1],plotH[1],color="orange",linestyle=lstyle[1],label='Humidity-18')
#plt.plot(fullDate[2],plotH[2],color="wheat",linestyle=lstyle[2],label='Humidity-19')
#plt.ylabel('Humidity (%)')
ax2.yaxis.grid(color='gray',linestyle='dashed')
#ax2.set_xticklabels(ax2.get_xticklabels(),rotation=90)
#ax2.tick_params(axis='x',labelrotation=90)
#ax3.tick_params(axis='x',labelrotation=90)
#ax3.set_xticklabels(ax3.get_xticklabels(),rotation=90)
#ax3.set_xticklabels([])    
#plt.legend()

plt.show()
