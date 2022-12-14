# -*- coding: utf-8 -*-
"""Kursach

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MbvMMi4XYHE9zuBQCY92TpVxYvdvRbU3
"""

import pandas as pd
import seaborn as sns
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

"""**Частина 1 (описова частина)**
> Визначення статистичних ознак



"""

sns.set(style="ticks", context="talk")
plt.style.use("dark_background")

file = "https://raw.githubusercontent.com/firebenderyt123/IMDB/main/IMDB%20top%201000.csv"
data = pd.read_csv(file, sep=',')
data = data.rename(columns={'Unnamed: 0': 'id'})

N = len(data)

cats = data['Genre']
certs = data['Certificate']
meta = data['Metascore']
#print('\n', cats)
# print('\n', certs)
print('Meta Min:', meta.min())
print('Meta Max:', meta.max())
print('Meta Std:', meta.std())
print('Meta Mean:', meta.mean())
print('Meta Dispersion:', meta.var())
print('Meta Assimetry:', meta.skew(), end='\n')

data

"""

> Визначення довірчих інтервалів

"""

tstar = 2.064 # хуй пойми этокуда это число .. Надо разобратся

se = meta.std()/np.sqrt(N)
lcb = meta.mean() - tstar * se
ucb = meta.mean() + tstar * se
(lcb, ucb)

"""
> Перерва на чай, каву, графіки


"""

sns.histplot(data=meta, bins=10, stat="density", palette="pastel")

"""Шото делаем"""

data_one_cat = data.copy()
data_one_cat['Genre'] = cats.str.split(', ')
data_one_cat = data_one_cat.apply(pd.Series.explode)
data_one_cat['id'] = [i for i in range(len(data_one_cat))]
data_one_cat = data_one_cat.set_index(['id'])
data_one_cat

"""**График по котам**"""

N = len(data_one_cat)
x = data_one_cat['Genre']
y = data_one_cat['Metascore']

mean_arr = np.zeros(N) + y.mean()
std_arr = np.zeros(N) + y.std()
med_arr = np.zeros(N) + y.median()
lp_arr = np.zeros(N) + y.quantile(.05)
rp_arr = np.zeros(N) + y.quantile(.95)

sns.set(rc={'figure.figsize':(30, 10)})
plt.style.use("dark_background")

sns.lineplot(x=x, y=med_arr, label='median', palette="pastel")
sns.lineplot(x=x, y=mean_arr, label='mean', palette="pastel")

sns.lineplot(x=x, y=lp_arr, label='5%', palette="pastel", color = "blue")
sns.lineplot(x=x, y=rp_arr, label='95%', palette="pastel", color = "blue")

sns.lineplot(x=x, y=mean_arr + std_arr, label='mean + std', palette="pastel", color = "orange")
ax = sns.lineplot(x=x, y=mean_arr - std_arr, label='mean - std', palette="pastel", color = "orange")
ax.lines[2].set_linestyle("--")
ax.lines[3].set_linestyle("--")
ax.lines[4].set_linestyle("--")
ax.lines[5].set_linestyle("--")

print(mean_arr[0])
print(std_arr[0])
print(med_arr[0])
print(y.describe())

sns.scatterplot(x=x, y=y, palette="pastel")

"""*   Напишемо декілька функцій для розрахунку різних законів розподілу


"""

def normal_from_library(array, min, max, draw = True, label='normal'):
	dd, p = stats.norm.fit(array)
	x = np.linspace(min, max, 100)
	y = stats.norm.pdf(x, loc = dd, scale = p)
	if draw:
		sns.lineplot(x=x, y=y, label=label)
	return x, y, dd, p

def gamma_from_library(array, min, max, draw = True, label='gamma'):
	a, dd, p = stats.gamma.fit(array)
	x = np.linspace(min, max, 100)
	y = stats.gamma.pdf(x, a = a, loc = dd, scale = p)
	if draw:
		sns.lineplot(x=x, y=y, label=label)
	return x, y, a, dd, p

def rayleigh_from_library(array, min, max, draw = True, label='rayleigh'):
	dd, p = stats.rayleigh.fit(array)
	x = np.linspace(min, max, 100)
	y = stats.rayleigh.pdf(x, dd, p)
	if draw:
		sns.lineplot(x=x, y=y, label=label)
	return x, y, dd, p

def chisquare_from_library(array, min, max, draw = True, label='chisquare'):
	df, dd, p = stats.chi2.fit(array)
	x = np.linspace(min, max, 100)
	y = stats.chi2.pdf(x, df, loc = dd, scale = p)
	if draw:
		sns.lineplot(x=x, y=y, label=label)
	return x, y, df, dd, p

def cool_function(df, min, max):
  sns.histplot(
    df,
    bins = 10,
    stat="density",
    element="step",
    palette="pastel"
  )
  x_n, y_n, dd_n, p_n = normal_from_library(
    array = df,
    min = min,
    max = max
  )
  x_g, y_g, a_g, dd_g, p_g = gamma_from_library(
    array = df,
    min = min,
    max = max
  )
  x_r, y_r, dd_r, p_r = rayleigh_from_library(
    array = df,
    min = min,
    max = max
  )
  x_c, y_c, df_c, dd_c, p_c = chisquare_from_library(
    array = df,
    min = min,
    max = max
  )
  return {
      'normal': [x_n, y_n, dd_n, p_n],
      'gamma': [x_g, y_g, a_g, dd_g, p_g],
      'rayleigh': [x_r, y_r, dd_r, p_r],
      'chisquare': [x_c, y_c, df_c, dd_c, p_c]
  }

sns.set(rc={'figure.figsize':(10, 5)})
plt.style.use("dark_background")

df = data['Metascore'].dropna() # дроп на, красиво и элегантно сносит неизвестные данные (None и тд.)
min = df.min()
max = df.max()
results = cool_function(df, min, max)
print() # просто прячем вывод чтобы красиво было

"""Терь надо понять шо мы должны выбрать"""

k = round(N**0.5)
d = (max - min) / k

histogr, b = np.histogram(df, k, density = True)

x_n, y_n, dd_n, p_n = results['normal']
x_g, y_g, a_g, dd_g, p_g = results['gamma']
x_r, y_r, dd_r, p_r = results['rayleigh']
x_c, y_c, df_c, dd_c, p_c = results['chisquare']

exp_freqN = np.zeros(k)
exp_freqG = np.zeros(k)
exp_freqR = np.zeros(k)
exp_freqC = np.zeros(k)

for i in range(k):
  exp_freqN[i] = stats.norm.cdf(min + (i + 1) * d, loc=dd_n, scale=p_n)
  - stats.norm.cdf(min + i * d, loc=dd_n, scale=p_n)
  exp_freqG[i] = stats.gamma.cdf(min +(i + 1) * d, a=a_g, loc=dd_g, scale=p_g)
  - stats.gamma.cdf(min + i * d, a=a_g, loc=dd_g, scale=p_g)
  exp_freqR[i] = stats.rayleigh.cdf(min + (i + 1) * d, loc=dd_r, scale=p_r)
  - stats.rayleigh.cdf(min + i * d, loc=dd_r, scale=p_r)
  exp_freqC[i] = stats.chi2.cdf(min + (i + 1) * d, df_c, loc=dd_c, scale=p_c)
  - stats.chi2.cdf(min + i * d, df_c, loc=dd_c, scale=p_c)

obs_freq = histogr * d

print(obs_freq, exp_freqR)

chiN, pN = stats.chisquare(obs_freq, exp_freqN)
print('Chi squred test for Normal distribution')
print(chiN, pN)
chiG, pG = stats.chisquare(obs_freq, exp_freqG)
print('\n\nChi squred test for Gamma distribution')
print(chiG, pG)
chiR, pR = stats.chisquare(obs_freq, exp_freqR)
print('Chi squred test for Rayleigh distribution')
print(chiR, pR, '\n-------------------\n\n')