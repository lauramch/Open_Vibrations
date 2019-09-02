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




tt = np.linspace(0,10,1000)

x_1 = (10/np.sqrt(20)*0.1/(20-10**2))*np.sin(np.sqrt(20)*tt) + 0 + 0.1/(20-10**2)*np.sin(10*tt)
x_2 = (10/np.sqrt(20)*0.1/(20-10**2))*np.sin(np.sqrt(20)*tt) + 0.005*np.cos(np.sqrt(20)*tt) + 0.1/(20-10**2)*np.sin(10*tt)
#x_2 = (10/np.sqrt(20)*0.1/(20-10**2))*np.sin(np.sqrt(20)*tt) + 0.01*np.cos(np.sqrt(20)*tt) + 0.1/(20-10**2)*np.sin(10*tt)













plt.figure(figsize=(7,3))
plt.plot(tt,x_1*1000,label='$x_0=0$, $v_0=0$')
plt.plot(tt,x_2*1000,'--',label='$x_0=0.005$, $v_0=0$')
plt.xlabel('time (s)')
plt.ylabel('displacement (mm)')
plt.grid('on')
plt.legend(loc=1)
plt.tight_layout()

plt.savefig('figures/example_2.png',dpi=300)








