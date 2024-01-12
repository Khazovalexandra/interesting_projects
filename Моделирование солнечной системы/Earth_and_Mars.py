import numpy as np
import matplotlib.pyplot as plt

R1 = 1.496*10e8 # Радиус орбиты Земли
T1 = 365.24 # Период вращения Земли 
am = 2.28*10e8 # бОльшая полуось вращения Марса по эллипсу
Tm = 689.98 # Период вращения Марса
ee = 0.093 # Эксцентриситет орбиты Марса
N = 36000 # Произвольное количество точек

def x(g):
         return am*(np.cos(g)-ee)
def y(g):
         return am*np.sqrt(1-ee**2)*np.sin(g)
def t(g):
         return Tm*(g-ee*np.sin(g))/2*np.pi
def X(g):
         return R1*np.cos(2*np.pi*t(g)/T1)
def Y(g):
         return R1*np.sin(2*np.pi*t(g)/T1)

y = np.array([y(2*np.pi*i/N) for i in np.arange(0,N,1)])
x = np.array([x(2*np.pi*i/N) for i in np.arange(0,N,1)])
X = np.array([X(2*np.pi*i/N) for i in np.arange(0,N,1)])
Y = np.array([Y(2*np.pi*i/N) for i in np.arange(0,N,1)])
t = np.array([t(2*np.pi*i/N) for i in np.arange(0,N,1)])

plt.figure()
plt.title("Гелиоцентрические орбиты  Земли и Марса")
plt.xlabel('x(g),X(g)')
plt.ylabel('y(g),Y(g)')
plt.plot(x,y,label='Орбита Марса')
plt.plot(X,Y,label='Орбита Земли')
plt.legend(loc='best')

plt.figure()
plt.title("Положение Марса в системе отсчёта связанной с Землёй")
plt.xlabel('x1/10e8')
plt.ylabel('y1(g/10e8')
x1=(x-X)
y1=(y-Y)
plt.plot(x1/10e8,y1/10e8)

plt.figure()
plt.title("Зависимость расстояния между Землёй и Марсом \n от времени в годах")
plt.xlabel('t/365.24')
plt.ylabel('sqrt(x1**2+y1**2)/10e8')
y2=np.sqrt(x1**2+y1**2)/10e8
x2=t/365.24
plt.plot(x2,y2)

plt.show()