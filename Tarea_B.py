# -*- coding: utf-8 -*-
"""
Created on Fri Oct  3 22:49:20 2025

@author: Carlos Gil
"""

import matplotlib.pyplot as plt
import numpy as np

def rota(x=0, teta=0):
  rota = np.array([[np.cos(teta), -np.sin(teta)], [np.sin(teta), np.cos(teta)]])
  prod = np.dot(rota,x)
  return prod


t = np.arange(-6.2, 6.2, .01)

x = 10 * np.sin(2.78 * t)* np.round(np.sqrt(np.cos(np.cos(8.2*t))))
y = 9*(np.cos(2.78*t))**2 * np.sin(np.sin(8.2*t))

xy = np.array([x, y]).transpose()

nn = xy.shape
print(nn)

n_rotations = 4
angle_step = 2 * np.pi / n_rotations

for i in range(n_rotations):
    angle = i * angle_step
    x_rot = x * np.cos(angle) - y * np.sin(angle)
    y_rot = x * np.sin(angle) + y * np.cos(angle)
    plt.plot(x_rot, y_rot)
    
    

plt.show()
plt.close()

plt.show()