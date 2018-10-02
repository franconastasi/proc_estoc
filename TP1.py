#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 18:20:00 2018

@author: franco
"""



import numpy as np

import matplotlib.pyplot as plt

from scipy.stats import norm


snr_db = np.arange(-5, 31) # defino vector para snr

snr = 10**(snr_db/ 10) # le hago la inversa de db

n_vect = np.arange(1,26,4) # vector para n

std_norm = norm()  # creo una variable que es un objeto de la gaussiana normal
                    # std.cdf(x) te devuelve la función distribución evaluada en x
                    # ej std.cdf(0) = 0.5; std.cdf(100) = 1.0 ; std.cdf(-100) = 0.0




#p_d_e_n = (1- (   1   -  2 * std_norm.cdf(snr**0.5)   )**n  ) / 2


###### CODIGO DE PRUEBA ######
# y = np.zeros(len(snr))
# x = np.arange(-1,4)
# for index, snr_e in enumerate(snr):
#    aux = np.sum (snr_e**x)
#    y[index] =  aux + snr_e
####FIN CODIGO DE PRUEBA ######

#phi_n = snr/   (    )
#p_a_e_n = ( std_norm.cdf( - (phi_n**0.5) ) -  std_norm.cdf( (phi_n**0.5) +1 )  ) / 2 


fig, ax = plt.subplot()


for n in n_vect:
    
    phi_den = np.zeros(len(snr)) # aca voy a guardar el denominador de phi_n
    i_vect = np.arange(-1,n-2 + 1)
    for index, snr_elem in enumerate(snr):
        phi_den[index] = np.sum((snr_elem / (snr_elem +1 ))**(-i_vect-1)) # calculo el denominador de phi_n para cada snr
    phi_n = snr/ phi_den
    
    p_a_e_n = ( std_norm.cdf( - (phi_n**0.5) ) -  std_norm.cdf( (phi_n**0.5) +1 )  ) / 2 # probabilidad de error del analógico
    p_d_e_n = (1- (   1   -  2 * std_norm.cdf(snr**0.5)   )**n  ) / 2 # probabilidad de error del digital
    
    ax.plot()
