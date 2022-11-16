from math import *
import numpy as np
import matplotlib.pyplot as plt

Sympthoms_a=np.zeros((6,4))
Sympthoms_s=np.zeros((6,4))
Sympthoms_h=np.zeros((6,4))
# Open the file with read only permit
text_file_s=open("Stones_var7.csv", "r")
lin_s=text_file_s.readlines()
text_file_s.close()
D1Size=len(lin_s)
Stones=D1Size-1
print(Stones)
for i in range(1,D1Size):
 data=lin_s[i].split(';')

for i in range(1,D1Size):
 data=lin_s[i].split(';')
 if data[0]<'20':
  Sympthoms_s[0,0] += 1
 elif (data[0]>='20') and (data[0]<'40'):
  Sympthoms_s[0,1] += 1
 elif (data[0]>='40') and (data[0]<'60'):
  Sympthoms_s[0,2] += 1
 else:
  Sympthoms_s[0,3] += 1

 if data[1] == 'yes':
  Sympthoms_s[1, 0] += 1
 else:
  Sympthoms_s[1, 1] += 1

 if data[2]=='eye':
  Sympthoms_s[2,0] += 1
 elif data[2]=='skin':
  Sympthoms_s[2,1] += 1
 else:
  Sympthoms_s[2,2] += 1

 if data[3] == 'yes':
  Sympthoms_s[3, 0] += 1
 else:
  Sympthoms_s[3, 1] += 1

 if data[4] == 'yes':
  Sympthoms_s[4, 0] += 1
 else:
  Sympthoms_s[4, 1] += 1

 if data[5] == 'yes\n':
  Sympthoms_s[5, 0] += 1
 else:
  Sympthoms_s[5, 1] += 1

prob_s=Sympthoms_s/Stones
print(prob_s)



text_file_a=open("Ascariasis_var7.csv", "r")
lin_a=text_file_a.readlines()
text_file_a.close()
D1Size=len(lin_a)
Ascariasis=D1Size-1
print(Ascariasis)

for i in range(1,D1Size):
 data=lin_a[i].split(';')
 if data[0]<'20':
  Sympthoms_a[0,0] += 1
 elif (data[0]>='20') and (data[0]<'40'):
  Sympthoms_a[0,1] += 1
 elif (data[0]>='40') and (data[0]<'60'):
  Sympthoms_a[0,2] += 1
 else:
  Sympthoms_a[0,3] += 1

 if data[1] == 'yes':
  Sympthoms_a[1, 0] += 1
 else:
  Sympthoms_a[1, 1] += 1

 if data[2]=='eye':
  Sympthoms_a[2,0] += 1
 elif data[2]=='skin':
  Sympthoms_a[2,1] += 1
 else:
  Sympthoms_a[2,2] += 1

 if data[3] == 'yes':
  Sympthoms_a[3, 0] += 1
 else:
  Sympthoms_a[3, 1] += 1

 if data[4] == 'yes':
  Sympthoms_a[4, 0] += 1
 else:
  Sympthoms_a[4, 1] += 1

 if data[5] == 'yes\n':
  Sympthoms_a[5, 0] += 1
 else:
  Sympthoms_a[5, 1] += 1


prob_a = Sympthoms_a/Ascariasis
print(prob_a)


text_file_h=open("Hepatitis_var7.csv", "r")
lin_h=text_file_h.readlines()
text_file_h.close()
D1Size=len(lin_h)
Hepatitis=D1Size-1
print(Hepatitis)

for i in range(1,D1Size):
 data=lin_h[i].split(';')
 if data[0]<'20':
  Sympthoms_h[0,0] += 1
 elif (data[0]>='20') and (data[0]<'40'):
  Sympthoms_h[0,1] += 1
 elif (data[0]>='40') and (data[0]<'60'):
  Sympthoms_h[0,2] += 1
 else:
  Sympthoms_h[0,3] += 1

 if data[1] == 'yes':
  Sympthoms_h[1, 0] += 1
 else:
  Sympthoms_h[1, 1] += 1

 if data[2]=='eye':
  Sympthoms_h[2,0] += 1
 elif data[2]=='skin':
  Sympthoms_h[2,1] += 1
 else:
  Sympthoms_h[2,2] += 1

 if data[3] == 'yes':
  Sympthoms_h[3, 0] += 1
 else:
  Sympthoms_h[3, 1] += 1

 if data[4] == 'yes':
  Sympthoms_h[4, 0] += 1
 else:
  Sympthoms_h[4, 1] += 1

 if data[5] == 'yes\n':
  Sympthoms_h[5, 0] += 1
 else:
  Sympthoms_h[5, 1] += 1


prob_h = Sympthoms_h/Hepatitis
print(prob_h)

##  Хворий у віці 66 років, при огляді виявлено збільшення печінки і слизових. Блювоти і нападів болю в правому підребер'ї
## немає, на апетит не скаржиться.

PrK_Stones = prob_s[0, 3] * prob_s[1, 1] * prob_s[2,0] * prob_s[3,1] * prob_s[4, 0] * prob_s[5, 0]
PrK_Ascariasis = prob_a[0, 3] * prob_a[1, 1] * prob_a[2,0] * prob_a[3,1] * prob_a[4, 0] * prob_a[5, 0]
PrK_Hepatitis = prob_h[0, 3] * prob_h[1, 1] * prob_h[2,0] * prob_h[3,1] * prob_h[4, 0] * prob_h[5, 0]

PrStones = 1
PrAscariasis = 1
PrHepatitis = 1

PrStones_K = PrStones*PrK_Stones/(PrStones*PrK_Stones + PrAscariasis*PrK_Ascariasis + PrHepatitis*PrK_Hepatitis)
PrAscariasis_K = PrAscariasis*PrK_Ascariasis/(PrStones*PrK_Stones + PrAscariasis*PrK_Ascariasis + PrHepatitis*PrK_Hepatitis)
PrHepatitis_K = PrHepatitis*PrK_Hepatitis/(PrStones*PrK_Stones + PrAscariasis*PrK_Ascariasis + PrHepatitis*PrK_Hepatitis)

print('Вірогідність каменів жовчних проток: ', round(PrStones_K*100,4),'%')
print('Вірогідність аскаридозу жовчних проток: ', round(PrAscariasis_K*100,4),'%')
print('Вірогідність паренхіматозного гепатиту: ', round(PrHepatitis_K*100,4),)

X=[1,2,3]
Y=[round(PrStones_K*100,2),round(PrAscariasis_K*100,2), round(PrHepatitis_K*100,2)]
plt.bar(X,Y)
plt.text(X[0],Y[0]/2,'Камені жовчних проток',ha='center')
plt.text(X[0],Y[0]/3,Y[0],ha='center')
plt.text(X[1],Y[1]/2,'Аскаридоз жовчних проток',ha='center')
plt.text(X[1],Y[1]/3,Y[1],ha='center')
plt.text(X[2],Y[2]/2,'Паренхіматозний гепатит',ha='center')
plt.text(X[2],Y[2]/3,Y[2],ha='center')
plt.xlabel('Диагнози')
plt.ylabel('Вірогідність диагнозу')
plt.show()