#!/usr/bin/env python3

import matplotlib.pyplot as plt
import time

def file_source():
#  nt = time.time() + 0.1
  with open('minicom-12-05-ev2.cap', encoding='cp1251') as f:
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

class plotterLine:
  def __init__(self, subplot, min_count, max_count):
    self.min_count = min_count
    self.max_count = max_count
    self.line, = subplot.plot([], [])
    self.dataX = []
    self.dataY = []

  def push(self, x, y):
    self.dataX.append(x)
    self.dataY.append(y)
    if self.max_count > 0 and len(self.dataX) > self.max_count:
      self.dataX = self.dataX[1:]
      self.dataY = self.dataY[1:]
    if self.min_count <= len(self.dataX):
      self.line.set_data(self.dataX, self.dataY)

  def limits(self):
    if self.min_count <= len(self.dataX):
      return min(self.dataX), max(self.dataX), min(self.dataY), max(self.dataY)
    else:
      return None, None, None, None

class plotter:
  def __init__(self, min_count, max_count):
    self.min_count = min_count
    self.max_count = max_count
    self.lines = []
    plt.ion()
    self.fig = plt.figure(figsize=(13, 6))
    self.ax = self.fig.add_subplot(111)
    self.ax.set_xlim(0, 1)
    self.ax.set_ylim(0, 1)
    plt.show()

  def redraw(self):
    self.__update_limits__()
    plt.pause(0.0001)

  def __lmax__(self, a, b):
    if a == None:
      return b
    if b == None:
      return a
    if a > b:
      return a
    return b

  def __lmin__(self, a, b):
    if a == None:
      return b
    if b == None:
      return a
    if a > b:
      return b
    return a

  def __update_limits__(self):
    g_xmin = None
    g_xmax = None
    g_ymin = None
    g_ymax = None

    for l in self.lines:
      xmin, xmax, ymin, ymax =  l.limits()
      g_xmin = self.__lmin__(g_xmin, xmin)
      g_xmax = self.__lmin__(g_xmax, xmax)
      g_ymin = self.__lmin__(g_ymin, ymin)
      g_ymax = self.__lmin__(g_ymax, ymax)

    if g_xmin != None and g_xmax != None and g_ymin != None and g_ymax != None:
      self.ax.set_xlim(g_xmin, g_xmax)
      self.ax.set_ylim(g_ymin, g_ymax)

  def add_line(self, ):
    line = plotterLine(self.ax, self.min_count, self.max_count)
    self.lines.append(line)
    return line

class Kalman:
  def __init__(self, K):
    self.K = K
    self.vPrev = None
    self.vCur = None
    self.vCurReal = None
    self.vPrevReal = None

  def next(self, value):
    self.update(value)
    return self.current()

  def update(self, value):
    if self.vCur == None:
      self.vCur = value
      self.vPrev = value
      self.vPrevReal = value
      self.vCurReal = value
      return

    vNext = self.K * value + (1 - self.K) * self.vPrev
    self.vPrev = self.vCur
    self.vCur = vNext

    self.vPrevReal = self.vCurReal
    self.vCurReal = value

  def current(self):
    return self.vCur

  def real(self):
    return self.vCurReal

  def delta(self):
    return self.vCur - self.vPrev

  def deltaReal(self):
    return self.vCurReal - self.vPrevReal

class delta:
  def __init__(self):
    self.prevX = None
    self.curX = None
    self.prevY = None
    self.curY = None

  def next(self, x, y):
    self.update(x, y)
    return self.current()

  def update(self, x, y):
    self.prevX = self.curX
    self.curX = x
    self.prevY = self.curY
    self.curY = y

  def current(self):
    if self.prevX == None:
      return 0
    return (self.curY - self.prevY) / (self.curX - self.prevX)

class CMeasure:
  def __init__(self, keys):
    self.keys = keys
    self.region = None

#  def update(self, value):
#   l, r = self.region(value)
#   self.region

  def region(self, value):
    print(value, self.keys)
    for i in range(1, len(self.keys)):
      if value >= self.keys[i-1] and value < self.keys[i]:
        return self.keys[i-1], self.keys[i]
    return 0

p = plotter(10, 100)
line_orig_vel = p.add_line()
line_kalman1_vel = p.add_line()
#line_kalman2_vel = p.add_line()
line_delta1 = p.add_line()
line_kalman1_delta = p.add_line()

kalman1 = Kalman(0.5)
#kalman2 = Kalman(0.1)
delta1 = delta()
kalman1_delta = Kalman(0.3)

measure = CMeasure([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
source = file_source
for now, vel in source():
  print(measure.region(vel))
  if vel < 20:
    continue
  print(now, vel)
  line_orig_vel.push(now, vel)
  line_kalman1_vel.push(now, kalman1.next(vel))
#  line_kalman2_vel.push(now, kalman2.next(vel))
#  line_delta1.push(now, delta1.next(now, vel))
#  line_kalman1_delta.push(now, kalman1_delta.next(delta1.current()))
  p.redraw()


exit(1)


kKalman1 = 0.01
kKalman2 = 0.1

p = plotter(0, 1, 0, 1)
xvec = []
yvecRaw = []
yvecA = []
yvec3 = []
yvec4 = []
line1 = p.add_line()
line2 = p.add_line()
line3 = p.add_line()
line4 = p.add_line()
for now, vel in source():
  print(now, vel)

  if len(yvec2) == 0:
    yK1 = vel
    yK2 = vel
    acc = 0
  else:
    yK1 = kKalman1 * vel + (1 - kKalman1) * yvec2[-1]
    yK2 = kKalman2 * vel + (1 - kKalman2) * yvec2[-1]
    acc1 = (yK1 - yvec2[-1]) / (now - xvec[-1])
    acc2 = (yK2 - yvec4[-1]) / (now - xvec[-1])

  xvec.append(now)
  yvec.append(vel)
  yvec2.append(yK1)
  yvec3.append(acc)
  yvec4.append(yK2)

  if len(xvec) > 100:
    xvec = xvec[1:]
    yvec = yvec[1:]
    yvec2 = yvec2[1:]
    yvec3 = yvec3[1:]
  if len(xvec) > 10:
    p.update_limits(xvec[0], xvec[-1], min(yvec+yvec2+yvec3), max(yvec + yvec2 + yvec3))
    line1.set_data(xvec, yvec)
    line2.set_data(xvec, yvec2)
    line3.set_data(xvec, yvec3)
    p.refresh()
