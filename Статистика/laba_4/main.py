from math import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import *
import scipy.stats as stat
import scipy.special as spec

# Open the file with read only permit
text_file=open("ZNO_var17.csv", "r")
lin=text_file.readlines()
text_file.close()
N=len(lin)-1
Age =np.zeros(N)
MarkMath = np.zeros(N)
MarkUA = np.zeros(N)
MarkEng = np.zeros(N)
MarkPhys = np.zeros(N)

for i in range(1,N):
 data=lin[i].split(";")
 Age[i]=int(data[1])
 MarkMath[i]= int(data[2])
 MarkUA[i] = int(data[3])
 MarkEng[i] = int(data[4])
 MarkPhys[i] = int(data[5])

Age[0]= Age[1]
MarkMath[0]= MarkMath[1]
MarkUA[0]= MarkUA[1]
MarkEng[0]= MarkEng[1]
MarkPhys[0]= MarkPhys[1]
Age=sorted(Age)
Age_max=Age[N-1]
Age_min=Age[1]
print("The age of students is between (min="+str(Age_min)+"; max="+str(Age_max)+").")

def calc(Mark, Name):
 print("Statistic for " + Name + ":")
 l = plt.plot(Age, Mark, 'ro')
 plt.setp(l, markersize=10)

 MeanGrade=np.mean(Mark)
 stdGrade=np.std(Mark)
 MedianGrade=np.median(Mark)
 LPercentileGrade=np.percentile(Mark,5)
 RPercentileGrade=np.percentile(Mark,95)

 print('Average students grade is '+str(MeanGrade))
 print('with standard deviation '+str(stdGrade))
 print('the median of distribution is '+str(MedianGrade))
 print('the 5% persentile of distribution is '+str(LPercentileGrade))
 print('the 95% persentile of distribution is '+str(RPercentileGrade))


 MeanArr=np.zeros(N)+MeanGrade
 MedArr=np.zeros(N)+MedianGrade
 stdArr=np.zeros(N)+stdGrade
 LPArr=np.zeros(N)+LPercentileGrade
 RPArr=np.zeros(N)+RPercentileGrade

 plt.plot(Age,MeanArr,'r-',lw=3)
 plt.plot(Age,MedArr, 'b-',lw=1)

 plt.plot(Age,LPArr,'g:',lw=1)
 plt.plot(Age,RPArr,'g:',lw=1)

 plt.plot(Age, MeanArr+stdArr, 'b:',lw=1)
 plt.plot(Age,MeanArr-stdArr,'b:',lw=1)
 plt.title('Distribution for ' + str(Name))
 plt.show()

 Mark=sorted(Mark)
 Max = Mark[N-1]
 Min = Mark[1]

 k = round(N**0.5)

 d=(Max-Min)/k

 histogr, b = np.histogram(Mark,k, density=True)
 plt.hist(Mark, bins=b, density=True)

 xx = np.linspace(Min, Max, 100)
 Mx=MeanGrade
 Sx=stdGrade
 y = ((1 / (np.sqrt(2 * np.pi) * Sx)) * np.exp(-0.5 * (1 / Sx * (xx - Mx))**2))
 plt.plot(xx,y, '-r')

 a, dd, p = stat.gamma.fit(Mark)
 yy= 1/spec.gamma(a)/p**a*(xx-dd)**(a-1)*np.exp(-(xx-dd)/p)
 plt.plot(xx, yy, '-g')

 yyy = gamma.pdf(xx, a=a, loc=dd, scale=p)
 plt.plot(xx, yyy, '--c')

 exp_freqG=np.zeros(k)
 exp_freqN=np.zeros(k)

 for i in range(0,k):
  exp_freqG[i]=stat.gamma.cdf(Min+(i+1)*d, a=a, loc=dd, scale=p)-stat.gamma.cdf(Min+i*d, a=a, loc=dd, scale=p)
  exp_freqN[i] = stat.norm.cdf(Min + (i + 1) * d, Mx,Sx) - stat.norm.cdf(Min + i * d, Mx,Sx)

 obs_freq = histogr*d

 chiG,pG=stat.chisquare(obs_freq,exp_freqG)
 print('Chi squred test for Gamma distribution')
 print(chiG,pG)
 chiN,pN=chisquare(obs_freq,exp_freqN)
 print('Chi squred test for Hauss distribution')
 print(chiN,pN)
 plt.title('Approximation for ' + str(Name))
 plt.show()

calc(MarkMath, "Math")
calc(MarkUA, "Ukrainian language")
calc(MarkEng, "English language")
calc(MarkPhys, "Physics")

