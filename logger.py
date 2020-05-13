#!/usr/bin/env python3

import serial
import time
import sys
import os
from speedometer import CSpeedometer

min_speed = 17
max_speed = 73

if len(sys.argv) > 1:
  prefix = '-' + sys.argv[1]
else:
  prefix = ''

def file_source():
  with open('minicom-12-05-ev1.cap', 'rb') as f:
    for l in f:
      yield l
      if l.decode('cp1251').startswith('$GNRMC'):
        time.sleep(0.1)

def port_source():
  port = serial.Serial('/dev/ttyUSB0', 115200, parity=serial.PARITY_NONE, timeout=1)
  for l in port:
    yield l

source = port_source

speedometer = CSpeedometer()

filename = time.strftime('logger-%Y-%m-%d_%H-%M-%S.cap{}'.format(prefix))

started = False
stopped = False

with open(filename, 'ab') as f:
  for line in source():
    l = line.decode('cp1251')
    tokens = l.split(',')
    sentence_type = tokens[0]
    if sentence_type == '$GNRMC':
      svel = tokens[7]
      if not svel:
        svel = '0'
      vel = float(svel) * 1.85
      speedometer.show(int(vel))
      if not started and vel > min_speed:
        speedometer.set_message(' !!!!!!!!!!!! MEASURING !!!!!!!!!!!! ')
        started = True

      if started and not stopped and vel > max_speed:
        speedometer.set_message(' done ')
        stopped = True

    if started and not stopped:
      f.write(line)
