from math import *
import numpy as np
import matplotlib.pyplot as plt
N=int(input('Введите количество испытаний: '))

D1=(N/100)*90 # исправный подшипник
D2=(N/100)*10 # неисправный подшипник
# K1 - вибрация
# K11 - вибрация в диапазоне 0,25-0,5
# K12 - вибрация в диапазоне 0,5-0,75
# K13 - вибрация в диапазоне >0,75
PrK11_D1=0.7
PrK12_D1=0.2
PrK13_D1=0.1
PrK11_D2=0.05
PrK12_D2=0.15
PrK13_D2=0.8
# K2 - температура
# K21 - температура в диапазоне 50-70 С
# K22 - температура в диапазоне 70-90 С
# K23 - температура в диапазоне >90 С
PrK21_D1=0.8
PrK22_D1=0.1
PrK23_D1=0.1
PrK21_D2=0.07
PrK22_D2=0.08
PrK23_D2=0.85
# K3 - загрязнение смазки
# K31 - в пределах нормы
# K32 – повышенное
PrK31_D1=0.9
PrK32_D1=0.1
PrK31_D2=0.3
PrK32_D2=0.7
# K - k11*k22*k31
print('При наблюдении: ')
print(' вибрации в диапазоне 0.75 (признак k11);')
print(' температуре в диапазоне 50-70 (признак k22);')
print(' загрязнение смазки в пределах нормы (признак k31).')
print('------------')

PrKD=np.zeros((4,4,3))
PrD=np.zeros(4)
PrK_D=np.zeros(4)
PrD_K=np.zeros(4)

PrKD[1,1,1]=PrK11_D1
PrKD[1,2,1]=PrK12_D1
PrKD[1,3,1]=PrK13_D1
PrKD[1,1,2]=PrK11_D2
PrKD[1,2,2]=PrK12_D2
PrKD[1,3,2]=PrK13_D2
PrKD[2,1,1]=PrK21_D1
PrKD[2,2,1]=PrK22_D1
PrKD[2,3,1]=PrK23_D1
PrKD[2,1,2]=PrK21_D2
PrKD[2,2,2]=PrK22_D2
PrKD[2,3,2]=PrK23_D2
PrKD[3,1,1]=PrK31_D1
PrKD[3,2,1]=PrK32_D1
PrKD[3,1,2]=PrK31_D2
PrKD[3,2,2]=PrK32_D2
D=[0,D1,D2]
K=[0,2,1,1]
for i in range(1,np.size(D)):
    PrD[i] = D[i] / N
    PrK_D[i]=PrKD[1,K[1],i]
    for j in range(2,np.size(K)):
        PrK_D[i]=PrK_D[i]*PrKD[j,K[j],i]
        PrK=PrD[1]*PrK_D[1]

for i in range(2,np.size(D)):
    PrK=PrK+PrD[i]*PrK_D[i]
for i in range(1,np.size(D)):
    PrD_K[i]=PrD[i]*PrK_D[i]/PrK

print('Вероятность исправного состояния (диагноз D1) составляет:')
print(round(PrD_K[1]*100,2),'%')
print('Вероятность неисправного состояния (диагноз D1) составляет:')
print((round(PrD_K[2]*100,2)),'%')
X=[1,2]
Y=[round(PrD_K[1]*100,2),round(PrD_K[2]*100,2)]
plt.bar(X,Y)
plt.text(X[0],Y[0]/2,'Исправное состояние',ha='center')
plt.text(X[0],Y[0]/3,Y[0],ha='center')
plt.text(X[1],Y[1]/2,'Неисправное состояние',ha='center')
plt.text(X[1],Y[1]/3,Y[1],ha='center')
plt.xlabel('Диагнозы')
plt.ylabel('Вероятность диагноза')
plt.show()