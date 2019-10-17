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

omega = np.linspace(0,3,1000)
S_0 = 1


k = 10
m = 10
c = 10
PSD_1 = S_0/((k-m*omega**2)**2+c**2*omega**2) 

k = 10
m = 10
c = 5
PSD_2 = S_0/((k-m*omega**2)**2+c**2*omega**2) 

k = 5
m = 10
c = 9
PSD_3 = S_0/((k-m*omega**2)**2+c**2*omega**2) 

k = 5
m = 10
c = 15
PSD_4 = S_0/((k-m*omega**2)**2+c**2*omega**2) 

plt.figure(figsize=(6.5,3))

plt.plot(omega,PSD_1,'-',label=('$k$=10, $m$=10, $c$=10, $\zeta$=0.5'))
plt.plot(omega,PSD_2,'--',label=('$k$=10, $m$=10, $c$=5, $\zeta$=0.25'))
plt.plot(omega,PSD_3,'-.',label=('$k$=5, $m$=10, $c$=9, $\zeta$=0.63'))
plt.plot(omega,PSD_4,':',label=('$k$=5, $m$=10, $c$=15, $\zeta$=1.06'))
plt.ylabel('PSD')
plt.xlabel(r'frequency intput ($\omega$)')
plt.grid('on')
plt.legend('Response to white noise input fo S_0=1')
plt.xlim(0,2.5)
#plt.ylim(-1.1,1.1)
plt.legend(framealpha=1)
plt.tight_layout()
plt.savefig('figures/response_to_white_noise',dpi=300)






















