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


#%% 

tt = np.linspace(0,20,1000)

xx_1 = 1/2*(np.cos(np.sqrt(2)*tt) + np.cos(2*tt))
xx_2 = 3/2*(np.cos(np.sqrt(2)*tt) - np.cos(2*tt))


plt.figure(figsize=(6,3))
plt.plot(tt,xx_1,label='$x_1$')
plt.plot(tt,xx_2,'--',label='$x_2$')
plt.grid('on')
plt.ylabel('amplitude (mm)')
plt.xlabel('time (s)')
plt.xlim([0,20])
plt.tight_layout()
plt.legend(loc=1,ncol=3,framealpha=1,bbox_to_anchor=[0,0,1,1.09])
plt.savefig('figures/Example_1_2_DOF_response.png',dpi=300)
























