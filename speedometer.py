#!/usr/bin/env python3

import os

class CSpeedometer:
  def set_message(self, message):
    self.message = message

  def show_digits(self, numbers):
    os.system('clear')
    print(numbers)
    for h in range(0, self.height):
      for n in numbers:
        print(self.Numbers[n][h], end = '')
      print()
    print("################################################################################\n")
    print(self.message)
    print("\n################################################################################")

  def show(self, value):
    if value == 0:
      self.show_digits([0])
      return

    numbers = []
    while(value != 0):
      high = int(value / 10)
      low  = int(value % 10)
      numbers.insert(0, low)
      value = high

    self.show_digits(numbers)


  def __init__(self):
    self.message = ""
    self.height = 17
    self.Number1 = \
    '             ####   \n' \
    '           ##  ##   \n' \
    '         ##    ##   \n' \
    '       ##      ##   \n' \
    '     ##        ##   \n' \
    '               ##   \n' \
    '               ##   \n' \
    '               ##   \n' \
    '               ##   \n' \
    '               ##   \n' \
    '               ##   \n' \
    '               ##   \n' \
    '               ##   \n' \
    '               ##   \n' \
    '               ##   \n' \
    '               ##   \n' \

    self.Number2= \
    '      ########      \n' \
    '    ##        ##    \n' \
    '  ##            ##  \n' \
    '  ##            ##  \n' \
    '  ##            ##  \n' \
    '  ##            ##  \n' \
    '              ##    \n' \
    '            ##      \n' \
    '          ##        \n' \
    '        ##          \n' \
    '      ##            \n' \
    '    ##              \n' \
    '  ##                \n' \
    '  ##                \n' \
    '  ##                \n' \
    '  ################  \n' \

    self.Number3= \
    '      ########      \n' \
    '    ##        ##    \n' \
    '  ##            ##  \n' \
    '  ##            ##  \n' \
    '  ##            ##  \n' \
    '              ##    \n' \
    '            ##      \n' \
    '          ##        \n' \
    '            ##      \n' \
    '              ##    \n' \
    '  ##            ##  \n' \
    '  ##            ##  \n' \
    '  ##            ##  \n' \
    '  ##            ##  \n' \
    '    ##        ##    \n' \
    '      #######       \n' \

    self.Number4= \
    '  ##            ##  \n' \
    '  ##            ##  \n' \
    '  ##            ##  \n' \
    '  ##            ##  \n' \
    '  ##            ##  \n' \
    '  ##            ##  \n' \
    '  ################  \n' \
    '                ##  \n' \
    '                ##  \n' \
    '                ##  \n' \
    '                ##  \n' \
    '                ##  \n' \
    '                ##  \n' \
    '                ##  \n' \
    '                ##  \n' \
    '                ##  \n' \

    self.Number5= \
    '  ################  \n' \
    '  ##                \n' \
    '  ##                \n' \
    '  ##                \n' \
    '  ##                \n' \
    '  ##                \n' \
    '    ###########     \n' \
    '              ####  \n' \
    '                ##  \n' \
    '                ##  \n' \
    '  ##            ##  \n' \
    '  ##            ##  \n' \
    '  ##            ##  \n' \
    '  ##            ##  \n' \
    '    ##        ##    \n' \
    '      #######       \n' \

    self.Number6= \
    '      ########      \n' \
    '    ##        ##    \n' \
    '  ##            ##  \n' \
    '  ##            ##  \n' \
    '  ##                \n' \
    '  ##                \n' \
    '  ##                \n' \
    '  ##  ##########    \n' \
    '  ####          ##  \n' \
    '  ##            ##  \n' \
    '  ##            ##  \n' \
    '  ##            ##  \n' \
    '  ##            ##  \n' \
    '  ##            ##  \n' \
    '    ##        ##    \n' \
    '      #######       \n' \

    self.Number7= \
    ' #################  \n' \
    '               ##   \n' \
    '              ##    \n' \
    '             ##     \n' \
    '            ##      \n' \
    '           ##       \n' \
    '          ##        \n' \
    '         ##         \n' \
    '         ##         \n' \
    '         ##         \n' \
    '         ##         \n' \
    '         ##         \n' \
    '         ##         \n' \
    '         ##         \n' \
    '         ##         \n' \
    '         ##         \n' \

    self.Number8= \
    '      ########      \n' \
    '    ##        ##    \n' \
    '  ##            ##  \n' \
    '  ##            ##  \n' \
    '  ##            ##  \n' \
    '    ##        ##    \n' \
    '      ##    ##      \n' \
    '        ####        \n' \
    '      ##    ##      \n' \
    '    ##        ##    \n' \
    '  ##            ##  \n' \
    '  ##            ##  \n' \
    '  ##            ##  \n' \
    '  ##            ##  \n' \
    '    ##        ##    \n' \
    '      #######       \n' \

    self.Number9= \
    '      ########      \n' \
    '    ##        ##    \n' \
    '  ##            ##  \n' \
    '  ##            ##  \n' \
    '  ##            ##  \n' \
    '  ##            ##  \n' \
    '  ##            ##  \n' \
    '  ##          ####  \n' \
    '    ##########  ##  \n' \
    '                ##  \n' \
    '                ##  \n' \
    '                ##  \n' \
    '  ##            ##  \n' \
    '  ##            ##  \n' \
    '    ##        ##    \n' \
    '      #######       \n' \

    self.Number0= \
    '      ########      \n' \
    '    ##        ##    \n' \
    '  ##            ##  \n' \
    '  ##            ##  \n' \
    '  ##            ##  \n' \
    '  ##            ##  \n' \
    '  ##            ##  \n' \
    '  ##            ##  \n' \
    '  ##            ##  \n' \
    '  ##            ##  \n' \
    '  ##            ##  \n' \
    '  ##            ##  \n' \
    '  ##            ##  \n' \
    '  ##            ##  \n' \
    '    ##        ##    \n' \
    '      #######       \n' \


    self.Numbers = \
    [
    self.Number0.split('\n'),
    self.Number1.split('\n'),
    self.Number2.split('\n'),
    self.Number3.split('\n'),
    self.Number4.split('\n'),
    self.Number5.split('\n'),
    self.Number6.split('\n'),
    self.Number7.split('\n'),
    self.Number8.split('\n'),
    self.Number9.split('\n'),
    ]

