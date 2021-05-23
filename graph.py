import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1000,1000, 10000000)
plt.ylim(-50, 100)
plt.xlim(-50, 50)
plt.plot([-10000,10000],[0,0], 'k-', linewidth=1)
plt.plot([0,0], [-10000,10000], 'k-', linewidth=1)
plt.grid(color='b', linestyle='-', linewidth=0.5)

def pravac(a,b):
    y = a*x + b
    return y

def parabola(c,d,e):
    y = c*x**2 + d*x + e
    return y

def sin(f,g, h):
    y = f*np.sin(g*x + h)
    return y

def cos(i,j,k):
    y = i*np.cos(j*x + k)
    return y

graf = int(input('''Odaberi graf:\n1) Pravac (y = ax + b)\n2) Parabola (y = ax^2 + bx + c)\n3) Graf sinus (y = a*sin(bx+c))
4) Graf kosinus (y = a*cos(bx+c)\n5) Graf sinus + kosinus\nVaš odabir: '''))

if graf == 1:
    a = float(input('Oderdi nagib pravca(a):'))
    b = float(input('Odredi odsjecak na osi y(b):'))
    pravac(a, b)
    plt.plot(x, pravac(a,b), 'r')

if graf == 2:
    a = float(input('Odredi kvadratni član(a)'))
    b = float(input('Odredi linearni član(b)'))
    c = float(input('Odredi slobodni član(c)'))
    plt.plot(x, parabola(a,b,c), 'b')

if graf == 100:
    a = float(input('Oderdi nagib pravca(a):'))
    b = float(input('Odredi odsjecak na osi y(b):'))
    c = float(input('Odredi kvadratni član(a)'))
    d = float(input('Odredi linearni član(b)'))
    e = float(input('Odredi slobodni član(c)'))
    plt.plot(x, parabola(c, d, e), 'b')
    plt.plot(x, pravac(a, b), 'r')

if graf == 3:
  f = float(input('Odredi kvadratni član(a):'))
  g = float(input('Odredi slobodni član(b):'))
  h = float(input('odredi asnfnas:'))
  plt.plot(x, sin(f,g, h), 'b')

if graf == 4:
    i = float(input('Odredi koeficijent:'))
    j = float(input('Odredi koeficijent:'))
    k = float(input('Odredi koeficijent:'))
    plt.plot(x, cos(i,j,k), 'r')

if graf == 5:
    i = float(input('Odredi koeficijent:'))
    j = float(input('Odredi koeficijent:'))
    k = float(input('Odredi koeficijent:'))
    f = float(input('Odredi kvadratni član(a):'))
    g = float(input('Odredi slobodni član(b):'))
    h = float(input('odredi asnfnas:'))
    plt.plot(x, sin(f, g, h), 'b')
    plt.plot(x, cos(i, j, k), 'r')

#if graf == 6:


plt.show()
