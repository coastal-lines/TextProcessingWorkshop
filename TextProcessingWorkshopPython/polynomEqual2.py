import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

#что мы вообще тут делаем:
#передаём все точки (x,y) в метод, который ищет функцию, которая бы наилучшим образом её описывала
#чем сложнее данные, тем тяжелее найти такую функцию. Отсюда апроксимация и сравнение погрешностей.
#сравнение погрешностей даёт возможность оценить какая модель работает лучше

#здесь пробуем найти линейную функцию с полиномом степени 2

#квадрат расстояния
def error(f, x, y):
    return np.sum((f(x) - y) ** 2)

data = np.genfromtxt(r'c:\Temp\!my\Luis\web_traffic.tsv')
x = data[:,0] #часы
y = data[:,1] #число запросов
#print(np.sum(np.isnan(y))) #число пустых запросов

#удаляем пустые элементы
#isnan возвращает массив, а тильда означает логическое отрицание. Т.е. если не ноль, то копируем в новый массив
x = x[~np.isnan(y)]
y = y[~np.isnan(y)]

#получаем коэффициенты многочлена для формулы a0 + a1*x + an*x^n
#где "а" и будут найденные коэфициенты
#1,2,3... это задаваемые степени полинома, т.е. наибольшая степень
#если грубо, то чем больше степень, тем точнее формула, но и одновременно сложнее
np.polyfit(x, y, 1, full=False)
print(np.polyfit(x, y, 1, full=False))

fp2, residuals, rank, singular_values, rcond2 = np.polyfit(x, y, 2, full=True)
print("fp is: ")
print(fp2)

#poly1d форматирует в привычно вглядящую функцию
f2 = np.poly1d(fp2)
print(f2)

#находим квадрат расстояния:
print(error(f2, x, y))

fx = np.linspace(0, x[-1], 1000)
plt.plot(fx, f2(fx), linewidth=1)
plt.legend(["d=%i" % f2.order], loc="upper left")
plt.scatter(x, y, s=10)
plt.title("Web traffic over the last month - FP2")
plt.xlabel("Time")
plt.ylabel("Hits/hour")
plt.xticks([w * 7 * 24 for w in range(10)], ['week %i' % w for w in range(10)])
plt.autoscale(tight=True)
plt.grid(True, linestyle='-', color='0.75')
plt.show()

#но если тупо увеличивать степень полинома, то в функции появятся характерные изгибы - т.е. мы получим переобучение
#функция начинает улавливать и шум, повторяя данные