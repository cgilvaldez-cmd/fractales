# -*- coding: utf-8 -*-
"""
Created on Sun Oct  5 22:57:22 2025

@author: Carlos Gil
"""

import matplotlib.pyplot as plt
import numpy as np

def rota(x=0, teta=0):
  rota = np.array([[np.cos(teta), -np.sin(teta)], [np.sin(teta), np.cos(teta)]])
  prod = np.dot(rota,x)
  return prod

t = np.arange(-6, 6, .01)

x = 2.5 * np.sin(-5 * t)**2 * 2 * np.cos(np.cos(4.28 * 2.3 * t))
y = 2.5 * np.sin(np.sin(-5 * t)) * np.cos(4.28 * 2.3 * t)**2

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