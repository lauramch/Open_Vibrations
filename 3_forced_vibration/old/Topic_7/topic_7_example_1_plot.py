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

#%% for a forced response for a underdamped system with the forcing function being cos. 

# define the time steps
tt = np.linspace(0,10,1000)


#%% for varying initial conditions

# define the inputs
k= 100        # N/m
m = 10         # kg
c = 10          # kg/s
F_0 = 1      # N
omega = 8.162  # rad/sec
x_0=0.0       # m
v_0=0.0       # m/s 

f_0 = F_0/m 
omega_n = np.sqrt(k/m) # rad/sec
c_critical = 2*m*omega_n
zeta = c/c_critical
omega_d = omega_n*np.sqrt(1-zeta**2)

# calculate the underdamped response. 
X = f_0/np.sqrt((omega_n**2-omega**2)**2 + (2*zeta*omega_n*omega)**2)
theta_p = np.arctan((2*zeta*omega_n*omega)/(omega_n**2-omega**2))
theta = np.arctan((omega_d*(x_0-X*np.cos(theta_p)))/(v_0+(x_0-X*np.cos(theta_p)*zeta*omega_n-omega*X*np.sin(theta_p))))
A = (x_0 - X*np.cos(theta_p))/np.sin(theta)

xx_h = A*np.exp(-zeta*omega_n*tt)*np.sin(omega_n*tt+theta) # the transient solution
xx_p = X*np.cos(omega*tt-theta_p) # the steady-state solution
xx = xx_h + xx_p

plt.figure(figsize=(6,3))
plt.plot(tt,xx*1000,'-',label='total response')
plt.plot(tt,xx_p*1000,'--',label='steady state response')
plt.plot(tt,xx_h*1000,':',label='transient response')
plt.grid('on')
plt.ylabel('amplitude (mm)')
plt.xlabel('time (s)')
plt.ylim(-10,10)
plt.title('$x_0$ = '+str(x_0)+'; $v_0$ = '+str(v_0)+'; $F_0$='+str(F_0)+'; $\omega$='+str(omega),size=15)
plt.legend(loc=1,ncol=3)
plt.tight_layout()
plt.savefig('figures/example_1_1.png',dpi=300)




#%% for varying initial conditions

# define the inputs
k= 100        # N/m
m = 10         # kg
c = 10          # kg/s
F_0 = 3      # N
omega = 8.162  # rad/sec
x_0=0.0       # m
v_0=0.0       # m/s 

f_0 = F_0/m 
omega_n = np.sqrt(k/m) # rad/sec
c_critical = 2*m*omega_n
zeta = c/c_critical
omega_d = omega_n*np.sqrt(1-zeta**2)

# calculate the underdamped response. 
X = f_0/np.sqrt((omega_n**2-omega**2)**2 + (2*zeta*omega_n*omega)**2)
theta_p = np.arctan((2*zeta*omega_n*omega)/(omega_n**2-omega**2))
theta = np.arctan((omega_d*(x_0-X*np.cos(theta_p)))/(v_0+(x_0-X*np.cos(theta_p)*zeta*omega_n-omega*X*np.sin(theta_p))))
A = (x_0 - X*np.cos(theta_p))/np.sin(theta)

xx_h = A*np.exp(-zeta*omega_n*tt)*np.sin(omega_n*tt+theta) # the transient solution
xx_p = X*np.cos(omega*tt-theta_p) # the steady-state solution
xx = xx_h + xx_p

plt.figure(figsize=(6,3))
plt.plot(tt,xx*1000,'-',label='total response')
plt.plot(tt,xx_p*1000,'--',label='steady state response')
plt.plot(tt,xx_h*1000,':',label='transient response')
plt.grid('on')
plt.ylabel('amplitude (mm)')
plt.xlabel('time (s)')
plt.ylim(-10,10)
plt.title('$x_0$ = '+str(x_0)+'; $v_0$ = '+str(v_0)+'; $F_0$='+str(F_0)+'; $\omega$='+str(omega),size=15)
plt.legend(loc=1,ncol=3)
plt.tight_layout()
plt.savefig('figures/example_1_2.png',dpi=300)



#%% for varying initial conditions

# define the inputs
k= 100        # N/m
m = 10         # kg
c = 10          # kg/s
F_0 = 1      # N
omega = 5  # rad/sec
x_0=0.0       # m
v_0=0.0       # m/s 

f_0 = F_0/m 
omega_n = np.sqrt(k/m) # rad/sec
c_critical = 2*m*omega_n
zeta = c/c_critical
omega_d = omega_n*np.sqrt(1-zeta**2)

# calculate the underdamped response. 
X = f_0/np.sqrt((omega_n**2-omega**2)**2 + (2*zeta*omega_n*omega)**2)
theta_p = np.arctan((2*zeta*omega_n*omega)/(omega_n**2-omega**2))
theta = np.arctan((omega_d*(x_0-X*np.cos(theta_p)))/(v_0+(x_0-X*np.cos(theta_p)*zeta*omega_n-omega*X*np.sin(theta_p))))
A = (x_0 - X*np.cos(theta_p))/np.sin(theta)

xx_h = A*np.exp(-zeta*omega_n*tt)*np.sin(omega_n*tt+theta) # the transient solution
xx_p = X*np.cos(omega*tt-theta_p) # the steady-state solution
xx = xx_h + xx_p

plt.figure(figsize=(6,3))
plt.plot(tt,xx*1000,'-',label='total response')
plt.plot(tt,xx_p*1000,'--',label='steady state response')
plt.plot(tt,xx_h*1000,':',label='transient response')
plt.grid('on')
plt.ylabel('amplitude (mm)')
plt.xlabel('time (s)')
plt.ylim(-10,10)
plt.title('$x_0$ = '+str(x_0)+'; $v_0$ = '+str(v_0)+'; $F_0$='+str(F_0)+'; $\omega$='+str(omega),size=15)
plt.legend(loc=1,ncol=3)
plt.tight_layout()
plt.savefig('figures/example_1_3.png',dpi=300)



#%% for varying initial conditions

# define the inputs
k= 100        # N/m
m = 10         # kg
c = 10          # kg/s
F_0 = 1      # N
omega = omega_n  # rad/sec
x_0=0.0       # m
v_0=0.0       # m/s 

f_0 = F_0/m 
omega_n = np.sqrt(k/m) # rad/sec
c_critical = 2*m*omega_n
zeta = c/c_critical
omega_d = omega_n*np.sqrt(1-zeta**2)

# calculate the underdamped response. 
X = f_0/np.sqrt((omega_n**2-omega**2)**2 + (2*zeta*omega_n*omega)**2)
theta_p = np.arctan((2*zeta*omega_n*omega)/(omega_n**2-omega**2))
theta = np.arctan((omega_d*(x_0-X*np.cos(theta_p)))/(v_0+(x_0-X*np.cos(theta_p)*zeta*omega_n-omega*X*np.sin(theta_p))))
A = (x_0 - X*np.cos(theta_p))/np.sin(theta)

xx_h = A*np.exp(-zeta*omega_n*tt)*np.sin(omega_n*tt+theta) # the transient solution
xx_p = X*np.cos(omega*tt-theta_p) # the steady-state solution
xx = xx_h + xx_p

plt.figure(figsize=(6,3))
plt.plot(tt,xx*1000,'-',label='total response')
plt.plot(tt,xx_p*1000,'--',label='steady state response')
plt.plot(tt,xx_h*1000,':',label='transient response')
plt.grid('on')
plt.ylabel('amplitude (mm)')
plt.xlabel('time (s)')
plt.ylim(-10,10)
plt.title('$x_0$ = '+str(x_0)+'; $v_0$ = '+str(v_0)+'; $F_0$='+str(F_0)+'; $\omega=\omega_n$',size=15)
plt.legend(loc=1,ncol=3)
plt.tight_layout()
plt.savefig('figures/example_1_4.png',dpi=300)


#%% for varying initial conditions

tt = np.linspace(0,30,1000)

# define the inputs
k= 100        # N/m
m = 10         # kg
c = 10          # kg/s
F_0 = 1      # N
omega = omega_n  # rad/sec
x_0=0.0       # m
v_0=0.0       # m/s 

f_0 = F_0/m 
omega_n = np.sqrt(k/m) # rad/sec
c_critical = 2*m*omega_n
zeta = c/c_critical
omega_d = omega_n*np.sqrt(1-zeta**2)

# calculate the underdamped response. 
X = f_0/np.sqrt((omega_n**2-omega**2)**2 + (2*zeta*omega_n*omega)**2)
theta_p = np.arctan((2*zeta*omega_n*omega)/(omega_n**2-omega**2))
theta = np.arctan((omega_d*(x_0-X*np.cos(theta_p)))/(v_0+(x_0-X*np.cos(theta_p)*zeta*omega_n-omega*X*np.sin(theta_p))))
A = (x_0 - X*np.cos(theta_p))/np.sin(theta)

xx_h = A*np.exp(-zeta*omega_n*tt)*np.sin(omega_n*tt+theta) # the transient solution
xx_p = X*np.cos(omega*tt-theta_p) # the steady-state solution
xx = xx_h + xx_p

plt.figure(figsize=(6,3))
plt.plot(tt,xx*1000,'-',label='total response')
plt.plot(tt,xx_p*1000,'--',label='steady state response')
plt.plot(tt,xx_h*1000,':',label='transient response')
plt.grid('on')
plt.ylabel('amplitude (mm)')
plt.xlabel('time (s)')
plt.ylim(-50,50)
plt.title('$x_0$ = '+str(x_0)+'; $v_0$ = '+str(v_0)+'; $F_0$='+str(F_0)+'; $\omega=\omega_n$',size=15)
plt.legend(loc=1,ncol=3)
plt.tight_layout()
plt.savefig('figures/example_1_5.png',dpi=300)































