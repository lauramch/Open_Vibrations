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

m_1 = 10
m_2 = 5
k_1 = 10
k_2 =25

# quadratic equation
a = m_1*m_2
b = -(m_1*k_2+m_2*k_1+m_2*k_2)
c = k_1*k_2

w_1 = np.sqrt((-b-np.sqrt(b**2-4*a*c))/(2*a))
w_2 = np.sqrt((-b+np.sqrt(b**2-4*a*c))/(2*a))

MK_1=np.zeros((2,2))
MK_1[0,0] =(k_1+k_2)-w_1**2*m_1 
MK_1[0,1] =-k_2
MK_1[1,0] =-k_2
MK_1[1,1] =k_2-w_1**2*m_2
u_11 = -MK_1[0,1]/MK_1[0,0]
u_21 = 1

MK_2=np.zeros((2,2))
MK_2[0,0] =(k_1+k_2)-w_2**2*m_1 
MK_2[0,1] =-k_2
MK_2[1,0] =-k_2
MK_2[1,1] =k_2-2_1**2*m_2
u_12 = -MK_2[0,1]/MK_2[0,0]
u_22 = 1

A_2 = -1/(u_11-u_12)
A_1 = -A_2


tt = np.linspace(0,20,10000)
theta = np.pi/2


xx = 1*np.cos(np.sqrt(k_1/m_1)*tt)
xx_1 =  A_1*np.sin(w_1*tt+theta)*u_11 + A_2*np.sin(w_2*tt + theta)*u_12
xx_2 =  A_1*np.sin(w_1*tt+theta)*u_21 + A_2*np.sin(w_2*tt + theta)*u_22


plt.figure(figsize=(6,3))
plt.plot(tt,xx,label='uncontrolled')
plt.plot(tt,xx_1,label='$x_1$')
plt.plot(tt,xx_2,'--',label='$x_2$')
plt.grid('on')
plt.ylabel('amplitude (mm)')
plt.xlabel('time (s)')
#plt.xlim([0,2])
plt.tight_layout()
plt.legend(loc=1,ncol=3,framealpha=1,bbox_to_anchor=[0,0,1,1.09])
plt.savefig('figures/Example_2_2_DOF_response.png',dpi=300)
























