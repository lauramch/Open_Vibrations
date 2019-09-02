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





tt = np.linspace(0,12,1000)

k= 500         # N/m
m = 10         # kg
c = 0       # kg/s
omega = 8.162
F_0 = 100
f_0 = F_0/m 
omega_n = np.sqrt(k/m) # rad/sec
c_critical = 2*m*omega_n
zeta = c/c_critical
omega_d = omega_n*np.sqrt(1-zeta**2)


x_0=0.00   # m
v_0=0.00   # m/s 

# calculate the underdamped response. 
X = f_0/(omega_n**2-omega**2)
A = np.sqrt((v_0/omega_n)**2+(x_0-X)**2)
theta = np.arctan((omega_n*(x_0-X))/(v_0))
xx_h = A*np.sin(omega_n*tt+-0)
xx_p = X*np.cos(omega*tt)
xx_underdamped = xx_h + xx_p


plt.figure(figsize=(6,3))
plt.plot(tt,xx_h*1000,':',lw=1.5,label='homogeneous solution')
plt.plot(tt,xx_p*1000,'--',lw=1.5,label='partial solution')
plt.plot(tt,xx_underdamped*1000,'-',lw=1,label='total solution')
plt.grid('on')
plt.ylabel('amplitude (mm)')
plt.xlabel('time (s)')
plt.tight_layout()
plt.legend(loc=1,ncol=3,framealpha=1,bbox_to_anchor=[0,0,1,1.09])
plt.savefig('figures/example_1.png',dpi=300)




omega_n/(v_0)


#7.0710678118654755/(0.0)



