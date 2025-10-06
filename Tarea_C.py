# -*- coding: utf-8 -*-
"""
Created on Fri Oct  3 23:28:25 2025

@author: Carlos Gil
"""

import matplotlib.pyplot as plt
import numpy as np

def rota(x=0, teta=0):
  rota = np.array([[np.cos(teta), -np.sin(teta)], [np.sin(teta), np.cos(teta)]])
  prod = np.dot(rota,x)
  return prod

t = np.arange(-6.2, 6.2, .01)

a= 1
b= 49
c= 0

x = np.cos(a * t) + np.cos(b * t) / 2 + np.sin(c * t) / 3
y = np.sin(a * t) + np.sin(b * t) / 2 + np.cos(c * t) / 3

xy = np.array([x, y]).transpose()

nn = xy.shape
print(nn)

rr = xy[0,:]

rrn = rota(rr, np.pi/2)
xyn = np.array([rrn])
print(xyn.shape)

for i in np.arange(1,nn[0]):
  rr = np.array(xy[i,:])
rrn = rota(rr, np.pi/4)
xyn = np.append(xyn, [rrn], axis=0)

print(xyn.shape)

plt.plot(x,y)
plt.plot(xyn[:,0], xyn[:,1])

plt.show()
plt.close()

plt.show()