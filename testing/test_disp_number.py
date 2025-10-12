# -*- coding: utf-8 -*-
"""
Just a simple testscript that displays 1 2 3 4 on the led-matrices

@author: JohannesWiesner
"""

import sys
sys.path.append('../')
from rpi_weather import RpiWeather
from led8x8icons import LED8x8ICONS as ICONS

display = RpiWeather()
number = 1234
display.disp_number(number)
