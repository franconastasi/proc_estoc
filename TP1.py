#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 18:20:00 2018

@author: franco
"""



import numpy as np

import matplotlib.pyplot as plt

from scipy.stats import norm


snr = np.arange(-5, 31)

snr_db = 10*np.log10(snr)

n_vect = np.arange(1,26,4)



p_d_e_n = (1- (1 - 2*(1-norm(snr**(0.5) ) )  )**n )


fig, ax = plt.subplot()

for n in n_vect:
    p_d_e_n = (1- (1 - 2*(1-norm(snr**(0.5) ) )  )**n )
    ax.plot()
