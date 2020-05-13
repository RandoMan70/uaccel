#!/usr/bin/env python3

import serial
import time
import sys

if len(sys.argv) > 1:
  prefix = '-' + sys.argv[1]
else:
  prefix = ''

filename = time.strftime('logger-%Y-%m-%d_%H-%M-%S.cap{}'.format(prefix))

port = serial.Serial('/dev/ttyUSB0', 115200, parity=serial.PARITY_NONE, timeout=1)
with open(filename, 'ab') as f:
  for line in port:
    f.write(line)
    print(line)
