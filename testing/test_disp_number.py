# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 19:38:03 2022

@author: johwi
"""

import sys
sys.path.append('../')


from rpi_weather import RpiWeather
from led8x8icons import LED8x8ICONS as ICONS

display = RpiWeather()
number = 1234

display.disp_number(number)