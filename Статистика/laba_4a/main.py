from math import *
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stat
from scipy.optimize import fsolve
# Open the file with read only permit
text_file = open("Hospital_17_visitorsTemp.csv", "r")
linT = text_file.readlines()
text_file.close()
text_file = open("Hospital_17_FluTemp.csv", "r")
linF = text_file.readlines()
text_file.close()

def analysis(lin):
 D1Size=len(lin)-1
 DataTemp=np.zeros(D1Size)
 Age=np.zeros((D1Size,1))
 for i in range(1,D1Size):
  data=lin[i].split(';')
  Age[i]=int(data[1])
  DataTemp[i] = float(data[2])

 DataTemp = sorted(DataTemp[:])
 DataTemp[0] = DataTemp[1]
 MeanTemp = np.mean(DataTemp)
 stdTemp= np.std(DataTemp)
 T_min = min(DataTemp)
 T_max = max(DataTemp)

 return DataTemp, MeanTemp, stdTemp, T_min, T_max


DataTempN, MeanTempN, stdTempN, TN_min, TN_max = analysis(linT)
DataTempF, MeanTempF, stdTempF, TF_min, TF_max = analysis(linF)

print('Average temperature of healthy person h is ' + str(MeanTempN))
print('with standard deviation ' + str(stdTempN))
print('All the data on normal temperature is between ' + str(TN_min) + ' and ' + str(TN_max))

print('\nAverage temperature of ill person h is ' + str(MeanTempF))
print('with standard deviation ' + str(stdTempF))
print('All the data on normal temperature is between ' + str(TF_min) + ' and ' + str(TF_max))


histT,bT=np.histogram(DataTempN,8,density=True)
plt.hist(DataTempN,bins=bT,density=True)

histT,bT=np.histogram(DataTempF,8,density=True)
plt.hist(DataTempF,bins=bT,density=True)

mTN,sTN = stat.norm.fit(DataTempN)
mTF,sTF = stat.norm.fit(DataTempF)
xx=np.linspace(0.99*TN_min,1.1*TF_max,100)
yTN=stat.norm.pdf(xx,loc=mTN,scale=sTN)
yTF=stat.norm.pdf(xx,loc=mTF,scale=sTF)
plt.plot(xx,yTN,'-b')
plt.plot(xx,yTF,'-r')

TN_Edge=37.0
xxEdge=[TN_Edge,TN_Edge]
yyEdge=[0,0.8]
plt.plot(xxEdge,yyEdge,'-k')
plt.show()

tN=np.linspace(0.99*TN_min,TN_Edge,100)
yTN=stat.norm.pdf(tN,loc=mTN,scale=sTN)
Pr11=np.trapz(yTN,tN)
tF=np.linspace(TN_Edge,1.1*TF_max,100)
yTF=stat.norm.pdf(tF,loc=mTN,scale=sTN)
Pr12=np.trapz(yTF,tF)
tN=np.linspace(0.99*TN_min,TN_Edge,100)
yTN=stat.norm.pdf(tN,loc=mTF,scale=sTF)
tF=np.linspace(TN_Edge,1.1*TF_max,100)
yTF=stat.norm.pdf(tF,loc=mTF,scale=sTF)
Pr21=np.trapz(yTN,tN)
Pr22=np.trapz(yTF,tF)
print('\nProbablity of correct decision for healthy person is '+ str(Pr11))
print('Probablity of the mistake of 1st type "the healthy person with high temperature" is '+ str(Pr12))
print('Probablity of correct decision for ill person is '+ str(Pr22))
print('Probablity of the mistake of 2nd type "the ill person with low temperature" is '+ str(Pr21))

C12=15 # the cost of the mistake of 1st type
C21=15 # the cost of the mistake of 2nd type
P2=0.17
P1=0.1
R=C12*P1*Pr12+C21*P2*Pr21
print('\nThe risk is ' + str(R))
print('The apriory risk for 1st mistake is ' + str(C12*P1))
print('The apriory risk for 2nd mistake is ' + str(C21*P2))

def DR(x0):
 F1=1/sqrt(2*np.pi*sTN)*exp(-(x0-mTN)**2/2/sTN)
 F2=1/sqrt(2*np.pi*sTF)*exp(-(x0-mTF)**2/2/sTF)
 y=F1/F2-(C21*P2)/(C12*P1)
 return y

x00=fsolve(DR,37)
print(mTN,mTF)
print(x00)