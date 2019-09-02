#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 09:30:27 2016

@author: downey
"""

# %% import modules

import IPython as IP
IP.get_ipython().magic('reset -sf')
import matplotlib.pyplot as plt
import matplotlib as mpl
import os as os
import numpy as np
import pandas as PD
import scipy as sp
from scipy import interpolate
import pickle
import time
import re
import json as json

import pylab
plt.rcParams.update({'font.size': 9})


cc = plt.rcParams['axes.prop_cycle'].by_key()['color']
plt.close('all')

#%% Load the expermintal data

F_0 = 1
k = 10
c = 1
m = 1
c_cr = 2*np.sqrt(k*m)
zeta = c/c_cr
omega_n = np.sqrt(k/m)
omega_d = omega_n*np.sqrt(1-zeta**2)
tt = np.linspace(0,10,1000)
tau = 0.1



# impulse loading

xx_1 = 0.2/(m*omega_d)*np.exp(-zeta*omega_n*tt)*np.sin(omega_d*tt)
xx_2 = 0.1/(m*omega_d)*np.exp(-zeta*omega_n*(tt-tau))*np.sin(omega_d*(tt-tau))
xx_2[0:np.argmin(np.abs(tt-tau))] = 'NaN'
xx = xx_1+xx_2


plt.figure(figsize=(6,3))
plt.plot(tt,xx_1*1000,':',linewidth=1,label='first impact')
plt.plot(tt,xx_2*1000,'--',linewidth=1,label='second impact')
plt.plot(tt,xx*1000,'-',label='total response')
plt.grid('on')
plt.ylabel('amplitude (mm)')
plt.xlabel('time (s)')
plt.tight_layout()
plt.legend(loc=1,ncol=3,framealpha=1,bbox_to_anchor=[0,0,1,1.09])
plt.savefig('response_double_impact.png',dpi=300)








