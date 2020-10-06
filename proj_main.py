# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

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
