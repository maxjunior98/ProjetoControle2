# -*- coding: utf-8 -*-

from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'qt')

# Importando bibliotecas para uso

import numpy as np
import math
import matplotlib.pyplot as plt
import control as ctrl
from control.matlab import *

# Definindo função de transferencia da planta

num = [2000]
den = [1000, 1]
G= ctrl.tf(num,den)

#Gráfico da planta para degrau unitário

t = np.linspace(0, 9000, 1000)
y1, t1 = step(G, t)
plt.figure()
plt.plot(t1,y1)
plt.legend(('Gmf'))
plt.xlabel('Tempo(s)')
plt.ylabel('Amplitude')

#Função de transferencia da planta

Ksensor = 0.5
Kph = 0.000239

Gplanta = G * Ksensor * Kph
print(Gplanta)

Gmf = feedback(Gplanta, 1)

y1, t1 = step(Gmf, t)
plt.figure()
plt.plot(t1,y1)
plt.legend(('Gmf'))
plt.xlabel('Tempo(s)')
plt.ylabel('Amplitude')

#Compensadores

Kc = 41.05
numPD = [1, 12.74]
denPD = [1]
PD = ctrl.tf(numPD, denPD)
print(PD)

numPI = [1, 0.005]
denPI = [1, 0]
PI = ctrl.tf(numPI, denPI)
print(PI)

Gc = Kc * PD * PI
print(Gc)

#Gráfico do Projeto Compensado

Gfinal = feedback(Gc*Gplanta, 1)

t2 = np.linspace(0, 100, 1000)
y1, t1 = step(Gfinal, t2)
plt.figure()
plt.plot(t1,y1)
plt.legend(('Gmf'))
plt.xlabel('Tempo(s)')
plt.ylabel('Amplitude')




