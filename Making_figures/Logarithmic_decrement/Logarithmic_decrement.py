# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# import modules
import IPython as IP
IP.get_ipython().magic('reset -sf')

import warnings     # added to ignore the plotting warings about font types in math mode
warnings.simplefilter("ignore", UserWarning)

import matplotlib as mpl
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import axes3d
import os as os
import numpy as np
import scipy as sp
import copy as copy
from matplotlib import cm
import time
#import pykrige as pykrige
import scipy.io as sio
tt1 = time.time()

plt.close('all')



#%% Problem 3


tt = np.linspace(0,10,1000)

k= 20         # N/m
m = 3         # kg
c = 2       # kg/s
omega_n = np.sqrt(k/m) # rad/sec
c_critical = 2*m*omega_n
xi = c/c_critical
omega_d = omega_n*np.sqrt(1-xi**2)

x_0=25/1000   # mm
v_0=-0/1000   # mm/s 

# calculate the underdamped response. 
A = np.sqrt((v_0+xi*omega_n*x_0)**2+(x_0*omega_d)**2)/omega_d
theta = np.arctan((omega_d*x_0)/(v_0+xi*omega_n*x_0))
xx_underdamped = A*np.exp(-xi*omega_n*tt)*np.sin(omega_d*tt+theta)

xx_peak = A*np.exp(-xi*omega_n*tt)

#xx_underdamped = xx_underdamped + 0.001*np.random.randn(len(xx_underdamped))


plt.figure(figsize=(6,3))
plt.plot(tt,xx_underdamped*1000,label='data')
plt.plot(tt,xx_peak*1000,'k--',label='envelope of maximum values')
plt.plot(tt,-xx_peak*1000,'k--')


plt.grid('on')
plt.ylabel('amplitude (mm)')
plt.xlabel('time (s)')
plt.xlim(0,10)
plt.ylim(-28,28)
plt.tight_layout()
plt.legend(loc=1,ncol=3)
plt.savefig('Logarithmic_decrement',dpi=300)













































































