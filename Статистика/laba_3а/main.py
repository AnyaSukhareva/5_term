from math import *
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk

Sympthoms_a=np.zeros((6,4))
Sympthoms_s=np.zeros((6,4))
Sympthoms_h=np.zeros((6,4))

PrK_Stones = None
PrK_Ascariasis= None
PrK_Hepatitis = None

age = 3
nausea = 1
yellowishness = 0
pain = 0
liver = 1
appetite = 0


def processing(lin_s, Sympthoms):
 D1Size = len(lin_s)
 Number = D1Size - 1
 print(Number)
 for i in range(1, D1Size):
  data = lin_s[i].split(';')
  if data[0]<'20':
   Sympthoms[0,0] += 1
  elif (data[0]>='20') and (data[0]<'40'):
   Sympthoms[0,1] += 1
  elif (data[0]>='40') and (data[0]<'60'):
   Sympthoms[0,2] += 1
  else:
   Sympthoms[0,3] += 1

  if data[1] == 'yes':
   Sympthoms[1, 0] += 1
  else:
   Sympthoms[1, 1] += 1

  if data[2]=='eye':
   Sympthoms[2,0] += 1
  elif data[2]=='skin':
   Sympthoms[2,1] += 1
  else:
   Sympthoms[2,2] += 1

  if data[3] == 'yes':
   Sympthoms[3, 0] += 1
  else:
   Sympthoms[3, 1] += 1

  if data[4] == 'yes':
   Sympthoms[4, 0] += 1
  else:
   Sympthoms[4, 1] += 1

  if data[5] == 'yes\n':
   Sympthoms[5, 0] += 1
  else:
   Sympthoms[5, 1] += 1
 prob = Sympthoms/Number
 print(prob)
 return prob


def insert_text_s():
 global PrK_Stones
 file_name = fd.askopenfilename()
 text_file_s = open(file_name)
 lin_s = text_file_s.readlines()
 prob_s = processing(lin_s, Sympthoms_s)
 text_file_s.close()
 PrK_Stones = prob_s[0, age] * prob_s[1, nausea] * prob_s[2, yellowishness] * prob_s[3, pain] * prob_s[4, liver] * prob_s[5, appetite]

def insert_text_a():
 global PrK_Ascariasis
 file_name = fd.askopenfilename()
 text_file_a = open(file_name)
 lin_a = text_file_a.readlines()
 prob_a = processing(lin_a, Sympthoms_a)
 text_file_a.close()
 PrK_Ascariasis = prob_a[0, age] * prob_a[1, nausea] * prob_a[2, yellowishness] * prob_a[3, pain] * prob_a[4, liver] * prob_a[5, appetite]

def insert_text_f():
 global PrK_Hepatitis
 file_name = fd.askopenfilename()
 text_file_h = open(file_name)
 lin_h = text_file_h.readlines()
 prob_h = processing(lin_h, Sympthoms_h)
 text_file_h.close()
 PrK_Hepatitis = prob_h[0, age] * prob_h[1, nausea] * prob_h[2, yellowishness] * prob_h[3, pain] * prob_h[4, liver] * prob_h[5, appetite]


def get_sympthoms():
 global age, nausea, yellowishness, pain, liver, appetite
 a = int(entry_age.get())
 n = entry_nausea.get()
 y = entry_yellowishness.get()
 p = entry_pain.get()
 l = entry_liver.get()
 ap = entry_appetite.get()
 if a < 20:
  age = 0
 elif (a >= 20) and (a < 40):
  age = 1
 elif (a >= 40) and (a < 60):
  age = 2
 elif a >= 60:
  age = 3
 else:
  age = None

 if n == 'yes':
  nausea = 0
 if n == 'no':
  nausea = 1
 else:
  nausea = None

 if y == 'eye':
  yellowishness = 0
 elif y == 'skin':
  yellowishness = 1
 elif y == 'no':
  yellowishness = 2
 else:
  yellowishness = None

 if p == 'yes':
  pain = 0
 elif p == 'no':
  pain = 1
 else:
  pain = None

 if l == 'yes':
  liver = 0
 elif l == 'no':
  liver = 1
 else:
  liver = None

 if ap == 'yes':
  appetite = 0
 elif ap == 'no':
  appetite = 1
 else:
  appetite = None
 # print(a, n, y, p, l, ap)
 print(age, nausea, yellowishness, pain, liver, appetite)
 validator()

def validator():
 global age, nausea, yellowishness, pain, liver, appetite
 valid = ttk.Label(root)
 valid.grid(column=2, row=3)
 if (age == None) or (nausea == None) or (yellowishness == None) or (pain == None) or (liver == None) or (appetite == None):
  valid['text'] = "Try again. Input is wrong"
 else:
  valid['text'] = "Good! You can download files"


def get_result():
 global PrK_Stones, PrK_Ascariasis, PrK_Hepatitis
 result = ttk.Label(root)
 result.grid(row=11, columnspan=3)
 result1 = ttk.Label(root)
 result1.grid(row=11, columnspan=3)
 result2 = ttk.Label(root)
 result2.grid(row=12, columnspan=3)
 result3 = ttk.Label(root)
 result3.grid(row=13, columnspan=3)
 if (PrK_Stones != None) and (PrK_Ascariasis != None) and (PrK_Hepatitis != None):
  result['text'] = ""
  PrStones_K = 1 * PrK_Stones / (1 * PrK_Stones + 1 * PrK_Ascariasis + 1 * PrK_Hepatitis)
  PrAscariasis_K = 1 * PrK_Ascariasis / (1 * PrK_Stones + 1 * PrK_Ascariasis + 1 * PrK_Hepatitis)
  PrHepatitis_K = 1 * PrK_Hepatitis / (1 * PrK_Stones + 1 * PrK_Ascariasis + 1 * PrK_Hepatitis)
  result1['text'] = ("Probability of stones: ", round(PrStones_K * 100, 4), "%")
  result2['text'] = ("Probability of ascariasis: ", round(PrAscariasis_K * 100, 4), "%")
  result3['text'] = ("Probability of hepatitis: ", round(PrHepatitis_K * 100, 4), "%")

  X = [1, 2, 3]
  Y = [round(PrStones_K * 100, 2), round(PrAscariasis_K * 100, 2), round(PrHepatitis_K * 100, 2)]
  plt.bar(X, Y)
  plt.text(X[0], Y[0] / 2, 'Камені жовчних проток', ha='center')
  plt.text(X[0], Y[0] / 3, Y[0], ha='center')
  plt.text(X[1], Y[1] / 2, 'Аскаридоз жовчних проток', ha='center')
  plt.text(X[1], Y[1] / 3, Y[1], ha='center')
  plt.text(X[2], Y[2] / 2, 'Паренхіматозний гепатит', ha='center')
  plt.text(X[2], Y[2] / 3, Y[2], ha='center')
  plt.xlabel('Диагнози')
  plt.ylabel('Вірогідність диагнозу')
  plt.show()
 else:
  result['text'] = "Not enough information yet"


root = Tk()

label1 = ttk.Label(root, text="Enter the patient's age:")
label1.grid(column=0, row=0, sticky=W, padx=5, pady=5)
label2 = ttk.Label(root, text="Have nausea? (yes / no):")
label2.grid(column=0, row=1, sticky=W, padx=5, pady=5)
label3=ttk.Label(root, text="Have yellowishness? (eye / skin / no)")
label3.grid(column=0, row=2, sticky=W, padx=5, pady=5)
label4=ttk.Label(root, text="Have pain in the right side? (yes / no)")
label4.grid(column=0, row=3, sticky=W, padx=5, pady=5)
label5=ttk.Label(root, text="Have liver enlargement? (yes / no)")
label5.grid(column=0, row=4, sticky=W, padx=5, pady=5)
label6=ttk.Label(root, text="Have appetite? (yes / no)")
label6.grid(column=0, row=5, sticky=W, padx=5, pady=5)

entry_age = ttk.Entry(root)
entry_age.grid(column=1, row=0)
entry_nausea = ttk.Entry(root)
entry_nausea.grid(column=1, row=1)
entry_yellowishness = ttk.Entry(root)
entry_yellowishness.grid(column=1, row=2)
entry_pain = ttk.Entry(root)
entry_pain.grid(column=1, row=3)
entry_liver = ttk.Entry(root)
entry_liver.grid(column=1, row=4)
entry_appetite = ttk.Entry(root)
entry_appetite.grid(column=1, row=5)

b4 = ttk.Button(root, text="I agree", command=get_sympthoms)
b4.grid(row=2, column=2)

label7=ttk.Label(root, text="--------------------Download files--------------------")
label7.grid(row=7, pady=15, columnspan=3)

b1 = ttk.Button(root, text="Download stones", command=insert_text_s)
b1.grid(column=0, row=8, padx = 30)
b2 = ttk.Button(root, text="Download ascariasis", command=insert_text_a)
b2.grid(column=1, row=8, padx = 30)
b3 = ttk.Button(root, text="Download hepatitis", command=insert_text_f)
b3.grid(column=2, row=8, padx = 30)

label8=ttk.Label(root, text="--------------------Result--------------------")
label8.grid(row=9, pady=15, columnspan=3)
res = ttk.Button(root, text="Calculate result", command=get_result)
res.grid(row=10, columnspan=3)

root.mainloop()


##  Хворий у віці 66 років, при огляді виявлено збільшення печінки і слизових. Блювоти і нападів болю в правому підребер'ї
## немає, на апетит не скаржиться.

