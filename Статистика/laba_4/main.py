from math import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import *
import scipy.stats as stat
import scipy.special as spec
# Open the file with read only permit
text_file=open("Example.csv", "r")
lin=text_file.readlines()
text_file.close()
N=len(lin)
Age=np.zeros(N)
MarkMath= np.zeros(N)
UAlang = np.zeros(N)
Englishlang = np.zeros(N)
Physics =np.zeros(N)

for i in range(1,N):
 data=lin[i].split(";")
 Age[i] = int(data[1])
 MarkMath[i]= int(data[2])
 UAlang[i] = int(data[3])
 Englishlang[i] = int(data[4])
 Physics[i] = int(data[5])
Age=Age[1:]
Age=Age[1:]
MarkMath = MarkMath[1:]
UAlang = UAlang[1:]
Englishlang = Englishlang[1:]
Physics = Physics[1:]

Age = sorted(Age)
Age_max = Age[-1]
Age_min = Age[0]
print("The age of students is between (min="+str(Age_min)+"; max="+str(Age_max)+").")

categories = ['Math', 'UAlang', 'Englishlang', 'Physics']
MeanGrade = np.zeros([4])
stdGrade = np.zeros([4])
MedianGrade = np.zeros([4])
LPercentileGrade = np.zeros([4])
RPercentileGrade = np.zeros([4])

def StatisticData(category, numberOfEl):
 MeanGrade[numberOfEl]=np.mean(category)
 stdGrade[numberOfEl]=np.std(category)
 MedianGrade[numberOfEl]=np.median(category)
 LPercentileGrade[numberOfEl]=np.percentile(category,5)
 RPercentileGrade[numberOfEl]=np.percentile(category,95)


StatisticData(MarkMath, 0), StatisticData(UAlang, 1), StatisticData(Englishlang, 2), StatisticData(Physics, 3)

i=0
for i in range(len(categories)):
 print('Average students grade on ' + str(categories[i]) +' is '+str(MeanGrade[i]) + ', with standard deviation '+str(stdGrade[i]) +', the median of distribution is '+str(MedianGrade[i]) +', the 5% persentile of distribution is '+ str(LPercentileGrade[i]) + ', the 95% persentile of distribution is ' + str(RPercentileGrade[i]))
 i = i + 1
 
#
# l=plt.plot(Age, MarkMath, 'ro')
# plt.setp(l, markersize=10)
#
# MeanArr=np.zeros(N)+MeanGradeOnMath
# MedArr=np.zeros(N)+MedianGradeOnMath
# stdArr=np.zeros(N)+stdGradeOnMath
# LPArr=np.zeros(N)+LPercentileGradeOnMath
# RPArr=np.zeros(N)+RPercentileGradeOnMath
#
# plt.plot(Age,MeanArr,'r-',lw=3)
# plt.plot(Age,MedArr, 'b-',lw=1)
#
# plt.plot(Age,LPArr,'g:',lw=1)
# plt.plot(Age,RPArr,'g:',lw=1)
#
# plt.plot(Age, MeanArr+stdArr, 'b:',lw=1)
# plt.plot(Age,MeanArr-stdArr,'b:',lw=1)
# plt.show()
#
# MarkMath=sorted(MarkMath)
# Math_max = MarkMath[N-1]
# Math_min = MarkMath[1]
#
# k = round(N**0.5)
#
# d=(Math_max-Math_min)/k
# dell = (Math_max-Math_min)/20
# xl = Age_min-dell
# xr = Math_max+dell
#
# histogr, b = np.histogram(MarkMath,k, density=True)
# plt.hist(MarkMath, bins=b, density=True)
#
# xx = np.linspace(Math_min, Math_max, 100)
# Mx=MeanGradeOnMath
# Sx=stdGradeOnMath
# y = ((1 / (np.sqrt(2 * np.pi) * Sx)) * np.exp(-0.5 * (1 / Sx * (xx - Mx))**2))
# plt.plot(xx,y, '-r')
#
# a, dd, p = stat.gamma.fit(MarkMath)
# yy= 1/spec.gamma(a)/p**a*(xx-dd)**(a-1)*np.exp(-(xx-dd)/p)
# plt.plot(xx, yy, '-g')
#
# yyy = stat.gamma.pdf(xx, a=a, loc=dd, scale=p)
# plt.plot(xx, yyy, '--c')
#
# exp_freqG=np.zeros(k)
# exp_freqN=np.zeros(k)
#
# for i in range(0,k):
#  exp_freqG[i]=stat.gamma.cdf(Math_min+(i+1)*d, a=a, loc=dd, scale=p)-stat.gamma.cdf(Math_min+i*d, a=a, loc=dd, scale=p)
#  exp_freqN[i] = stat.norm.cdf(Math_min + (i + 1) * d, Mx,Sx) - stat.norm.cdf(Math_min + i * d, Mx,Sx)
#
# obs_freq = histogr*d
#
# chiG,pG=stat.chisquare(obs_freq,exp_freqG)
# print('Chi squred test for Gamma distribution')
# print(chiG,pG)
# chiN,pN=chisquare(obs_freq,exp_freqN)
# print('Chi squred test for Hauss distribution')
# print(chiN,pN)
# plt.show()
