import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

#здесь пробуем найти линейную функцию с полиномом степени 2
#и делим данные на обучающие и тестовые

def error(f, x, y):
    return np.sum((f(x) - y) ** 2)

data = np.genfromtxt(r'c:\Temp\!my\Luis\web_traffic.tsv')
x = data[:,0] #часы
y = data[:,1] #число запросов
x = x[~np.isnan(y)]
y = y[~np.isnan(y)]

#делим на до 3.5 недели и после неё
inflection = 3.5 * 7 * 24
inflection = int(inflection)
xa = x[:inflection]
ya = y[:inflection]
xb = x[inflection:]
yb = y[inflection:]

frac = 0.3
split_idx = int(frac * len(xb))
shuffled = np.random.permutation(list(range(len(xb))))
test = sorted(shuffled[:split_idx])
train = sorted(shuffled[split_idx:])

fbt1 = np.poly1d(np.polyfit(xb[train], yb[train], 1))
fbt2 = np.poly1d(np.polyfit(xb[train], yb[train], 2))
print(error(fbt1, xb[test], yb[test]))
print(error(fbt2, xb[test], yb[test]))
print(fbt2)

#какую задачу мы решали?
#нужно было спрогнозировать когда выйдем на 100000 запросов в час
#итоговое предсказание:
#решаем линейное уравнение, где х0=800
from scipy.optimize import fsolve
print(fbt2)
print(fbt2 - 100000)
reached_max = fsolve(fbt2 - 100000, x0=800) / (7 * 24)
print("100,000 hits/hour expected at week %f" % reached_max[0])