#!/usr/bin/env python3

import matplotlib.pyplot as plt
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

#colors=['green', 'red', 'blue']
colors=['green', 'green', 'green']
idx = 0
for filename in sys.argv[1:]:
  print(filename)
  dataX = []
  dataY = []
  startX = None
  for now,vel in source(filename):
    if len(dataX) == 0:
      dataX.append(0)
      startX = now
    else:
      dataX.append(now - startX)
    dataY.append(vel)
  if idx < len(colors):
    plt.plot(dataX, dataY, color=colors[idx])
  else:
    plt.plot(dataX, dataY)
  idx += 1

plt.show()
