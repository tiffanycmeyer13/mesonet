import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np
import calendar

path='/aiidata/mesonet/'
years=[2017,2018,2019]
months=[4,5,6,7,8]
months=[4,5,6]
months=[4]
#colorMax=['#ff4d4d','#b30000']
#colorMin=['#4d4dff','#0000b3']
lstyle=['-',':','-.']
rain=[0,0,0]
j=0
fullDate=[[],[],[]]
plotTmax=[[],[],[]]
plotTmin=[[],[],[]]
plotFrz=[[],[],[]]
plotRain=[[],[],[]]
plotH=[[],[],[]]
for year in years:
  print 'year',year,j
  data=pd.read_csv(path+str(year)+'.csv', na_values='-996.00')
  for i in range(0,data['YEAR'].size):
    if int(data['MONTH'][i]) >= 4 and int(data['MONTH'][i]) <=8:
      #if(int(data['DAY'][i]) <22 and int(data['YEAR'][i]) == 2019): break
      date=datetime.date(int(data['YEAR'][i]),int(data['MONTH'][i]),int(data['DAY'][i]))
      print date.strftime('%m-%d'),data['HMAX'][i]
      fullDate[j].append(date.strftime('%m-%d'))
      #fullDate.append(datetime.date(int(data['YEAR'][i]),int(data['MONTH'][i]),int(data['DAY'][i])))
      plotTmax[j].append(data['TMAX'][i])
      plotTmin[j].append(data['TMIN'][i])
      plotFrz[j].append(32)
      rain[j]=rain[j]+data['RAIN'][i]
      plotRain[j].append(rain[j])
      plotH[j].append(data['HMAX'][i])

  print 'j here',j
  j=j+1

ax1=plt.subplot(212)
plt.plot(fullDate[0],plotTmax[0],color="red",linestyle=lstyle[0],label='TMax-17')
plt.plot(fullDate[1],plotTmax[1],color="red",linestyle=lstyle[1],label='TMax-18')
plt.plot(fullDate[2],plotTmax[2],color="red",linestyle=lstyle[2],label='TMax-19')
plt.plot(fullDate[0],plotTmin[0],color="blue",linestyle=lstyle[0],label='TMin-17')
plt.plot(fullDate[1],plotTmin[1],color="blue",linestyle=lstyle[1],label='TMin-18')
plt.plot(fullDate[2],plotTmin[2],color="blue",linestyle=lstyle[2],label='TMin-19')
if month<5: plt.plot(fullDate[0],plotFrz[0],color="black", linestyle='dashed')
#plt.xticks(rotation=90)
plt.ylabel('Temperature (F)')
plt.xlabel('Date')
plt.legend(ncol=2)
ax1.yaxis.grid(color='gray',linestyle='dashed')


ax2=plt.subplot(211)
plt.plot(fullDate[0],plotRain[0],color="green",linestyle=lstyle[0],label='RainAccum-17')
plt.plot(fullDate[1],plotRain[1],color="green",linestyle=lstyle[1],label='RainAccum-18')
plt.plot(fullDate[2],plotRain[2],color="green",linestyle=lstyle[2],label='RainAccum-19')
plt.ylabel('Rain Accumulation')
  #plt.xticks(rotation=90)
plt.legend()
plt.title(calendar.month_name[month])
ax2.set_xticklabels([])
ax3 = ax2.twinx()
plt.plot(fullDate[0],plotH[0],color="orange",linestyle=lstyle[0],label='Humidity-17')
plt.plot(fullDate[1],plotH[1],color="orange",linestyle=lstyle[1],label='Humidity-18')
plt.plot(fullDate[2],plotH[2],color="orange",linestyle=lstyle[2],label='Humidity-19')
plt.ylabel('Humidity (%)')
ax3.tick_params(axis='x',labelrotation=90)
#ax3.set_xticklabels(ax3.get_xticklabels(),rotation=90)
#ax3.set_xticklabels([])    
plt.legend()

plt.show()
