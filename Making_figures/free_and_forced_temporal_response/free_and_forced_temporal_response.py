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



#%% free_and_forced_temporal_response

cc = plt.rcParams['axes.prop_cycle'].by_key()['color']
tt = np.linspace(0,7,1000)

k= 10           # N/m
m = 2.5         # kg
omega_n = np.sqrt(10/2.5) # rad/sec
omega = 4 # rad/sec
F_0 = 0.1 # kN
f_0 = F_0/m 

x_0 = 1/1000         # mm
v_0 = 0/1000     # mm/s 
xx_1 = v_0/omega_n*np.sin(omega_n*tt) + x_0*np.cos(omega_n*tt)

xx_2 = v_0/omega_n*np.sin(omega_n*tt) + (x_0-f_0/(omega_n**2-omega**2))*np.cos(omega_n*tt) + (f_0/(omega_n**2-omega**2))*np.cos(omega*tt)
xx_forcing = F_0*np.cos(omega*tt)

fig, ax1 = plt.subplots(figsize=(5.5,3))
t = np.arange(0.01, 10.0, 0.01)
lns1 = ax1.plot(tt,xx_1*1000,color=cc[0],label='free vibration')
lns2 = ax1.plot(tt,xx_2*1000,'--',color=cc[1],label='forced vibration')
ax1.set_xlabel('time (s)')
# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_ylabel('amplitude (mm)')
#ax1.tick_params('y', co)


ax2 = ax1.twinx()
s2 = np.sin(2 * np.pi * t)
lns3 = ax2.plot(tt,xx_forcing*1000,':',color=cc[2],label='forcing function',zorder=0)
ax2.set_ylabel('force', color=cc[2])
ax2.tick_params('y', colors=cc[2])


# added these three lines
lns = lns1+lns2+lns3
labs = [l.get_label() for l in lns]
ax2.legend(lns, labs, loc=3, framealpha=1)

fig.tight_layout()
plt.show()

plt.savefig('free_and_forced_temporal_response.png',dpi=300)

































































