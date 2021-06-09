import numpy as np
import matplotlib.pyplot as plt
from math import *

x = np.linspace(-1000,1000, 10000000)

def pravac(a,b):
    y = a*x + b
    return y

def parabola(a,b, c):
    y = a*x**2 + b*x + c
    return y

def sin(a,b,c):
    y = a*np.sin(b*x + c)
    return y

def cos(a,b,c):
    y = a*np.cos(b*x + c)
    return y

prviod = int(input('Odaberi: \n1) Gotovi grafovi\n2) Sam upiši koeficijente\nVaš odabir: '))


if prviod == 1:
    drugiod = (int(input('Odaberi gotov graf: \n1) Slobodni pad na Zemlji (h-t graf) \n2) Slobodni pad na Mjesecu (h-t graf) \n3) Slobodni pad na Marsu (h-t graf)\nVaš odabir: '))) 
    if drugiod == 1 or drugiod == 2 or drugiod ==3:
        h = float(input('Odaberi visinu:'))
        plt.clf()
        plt.ylim(0, h*1.5)
        plt.xlim(0, sqrt(h/1.625))
        plt.xlabel('Vrijeme')
        plt.ylabel('Visina')
        plt.plot([-10000,10000],[0,0], 'k-', linewidth=1)
        plt.plot([0,0], [-10000,10000], 'k-', linewidth=1)
        plt.grid(color='b', linestyle='-', linewidth=0.5)
        if drugiod == 1:
            y = (h -9.81*x**2)
            plt.plot(x, y, 'r', label='Zemlja')
        if drugiod == 2:
            ym = (h -1.625*x**2)
            plt.plot(x, ym, 'r', label='Mjesec')
            yz = (h -9.81*x**2)
            plt.plot(x, yz, 'b', label='Zemlja')
        if drugiod == 3:
            ya = (h-3.72*x**2)
            plt.plot(x, ya, 'r', label='Mars')
            yz = (h-9.81*x**2)
            plt.plot(x, yz, 'b', label='Zemlja')
    else:
        print('Upišite jedan od ponuđenih odgovora')
    

elif prviod == 2:
    graf = int(input('''Odaberi graf:\n1) Pravac\n2) Parabola\n3) Graf sinus
4) Graf kosinus \n5) Graf sinus i kosinus\n6) Graf pravac i parabola \nVaš odabir: '''))
    plt.clf()
    plt.ylim(-50, 50)
    plt.xlim(-50, 50)
    plt.xlabel('Apscisa')
    plt.ylabel('Ordinata')
    plt.plot([-10000,10000],[0,0], 'k-', linewidth=1)
    plt.plot([0,0], [-10000,10000], 'k-', linewidth=1)
    plt.grid(color='b', linestyle='-', linewidth=0.5)
    if graf == 1:
        print('Pravac: A*x + B')
        a = float(input('Odredi A:'))
        b = float(input('Odredi B:'))
        pravac(a, b)
        plt.plot(x, pravac(a,b), 'r', label=f'y = {a}x + {b}')

    if graf == 2:
        print('Parabola: y = A*x^2 + B*x + C')
        a = float(input('Odredi A:'))
        b = float(input('Odredi B:'))
        c = float(input('Odredi C:'))
        plt.plot(x, parabola(a,b,c), 'b', label=f'y = {a}$x^2$ + {b}x + {c}')

    if graf == 3:
        print('Sinus: y = A*sin(B*x + C)')
        a = float(input('Odredi A:'))
        b = float(input('Odredi B:'))
        c = float(input('odredi C:'))
        plt.plot(x, sin(a,b,c), 'b', label=f'{a}sin({b}x + {c})')

    if graf == 4:
        print('Kosinus: y = A*cos(B*x + C)')
        a = float(input('Odredi A:'))
        b = float(input('Odredi B:'))
        c = float(input('odredi C:'))
        plt.plot(x, cos(a,b,c), 'r', label=f'{a}cos({b}x + {c})')

    if graf == 5:
        print('Sinus: y = A*sin(B*x + C)')
        print('Kosinus: y = D*cos(E*x + F)')
        a = float(input('Odredi A:'))
        b = float(input('Odredi B:'))
        c = float(input('odredi C:'))
        d = float(input('Odredi D:'))
        e = float(input('Odredi E:'))
        f = float(input('odredi F:'))
        plt.plot(x, sin(a, b, c), 'b', label=f'{a}sin({b}x + {c})')
        plt.plot(x, cos(d, e, f), 'r', label=f'{d}cos({e}x + {f})')

    if graf == 6:
        print('Pravac: y = A*x + B')
        print('Parabola: y = C*x^2 + D*x + E')
        a = float(input('Odredi A:'))
        b = float(input('Odredi B:'))
        c = float(input('Odredi C:'))
        d = float(input('Odredi D:'))
        e = float(input('Odredi E:'))
        plt.plot(x, parabola(c, d, e), 'b', label=f'y = {c}$x^2$ + {d}x + {e}')
        plt.plot(x, pravac(a, b), 'r', label=f'y = {a}x + {b}')

    else:
        print('Upišite jedan od ponuđenih odgovora')
else:
    print('Upišite jedan od ponuđenih odgovora')

plt.legend()
plt.show()
