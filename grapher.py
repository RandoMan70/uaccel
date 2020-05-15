#!/usr/bin/env python3

import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
#import scipy.interpolate
from scipy.optimize import fsolve
import numpy as np
import time
import sys

def usage():
  print("Usage: grapher.py <filename1> <filename2> ...")
  exit(1)

if len(sys.argv) == 1:
  usage()

def source(filename):
  with open(filename, encoding='cp1251') as f:
    for l in f:
      kws = l.split(',')
      t = kws[0]
      if t == '$GNRMC':
        time = kws[1]
        h = int(time[0:2])
        m = int(time[2:4])
        s = int(time[4:6])
        ms = int(time[7:9]) * 10
        ltime = h * 3600 + m * 60 + s + ms/1000
        status = kws[2]
        svel = kws[7]
        if not svel:
          svel = '0'
        vel = float(svel) * 1.85
        yield ltime, vel

def subgraph(dataX, dataY, ymin, ymax):
  resX = []
  resY = []
  for idx in range (0, len(dataX)):
    if dataY[idx] >= ymin and dataY[idx] <= ymax:
      resX.append(dataX[idx])
      resY.append(dataY[idx])
  return resX, resY

def resolve(dataX, dataY, reqY):
  for idx in range(1, len(dataX)):
    if dataY[idx-1] <= reqY and reqY <= dataY[idx]:
      return dataX[idx]

def get_startx(source, reqY):
  rawX = []
  rawY = []
  for now,vel in source(filename):
    rawX.append(now)
    rawY.append(vel)

  sgX, sgY = subgraph(rawX, rawY, 15, 25)
  xs = np.linspace(sgX[0], sgX[-1], 1000)
  spl = UnivariateSpline(sgX, sgY)
  spl.set_smoothing_factor(2)
  return resolve(xs, spl(xs), 20)

colors=['green', 'red', 'blue',]
factors=[1, 2, 3, 4, 5]
color_idx = 0
fig_speed = plt.figure()
plot_speed = fig_speed.gca()
plot_speed.set(xlabel='speed(km/h)', ylabel='acceleration(km/h*s)', title='Acceleration over speed')
fig_time = plt.figure()
plot_time = fig_time.gca()
plot_time.set(xlabel='time(s)', ylabel='speed (km/h) / acceleration(km/h*s)', title='Speed and acceleration over time')
for filename in sys.argv[1:]:
  startX = get_startx(source, 20)

  if color_idx >= len(colors):
    color = colors[-1]
  else:
    color = colors[color_idx]
    color_idx += 1

  print(filename)
  dataX = []
  dataY = []
  for now,vel in source(filename):
    dataX.append(now - startX)
    dataY.append(vel)

  xs = np.linspace(dataX[0], dataX[-1], 1000)
  spl = UnivariateSpline(dataX, dataY)
  spl.set_smoothing_factor(10)
  d = spl.derivative()
  plot_speed.plot(spl(xs), d(xs), color=color)
  plot_time.plot(xs, spl(xs), color=color)
  plot_time.plot(dataX, dataY, 'x', color=color)
  plot_time.plot(xs, d(xs), color=color)

plt.show()
