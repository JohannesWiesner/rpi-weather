# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 17:29:32 2022

@author: johwi
"""

# from rpi_weather import RpiWeather
import sys
sys.path.append('../')

from rpi_weather import RpiWeather
from led8x8icons import LED8x8ICONS as ICONS

sunny_bitmap = ICONS['sunny']

display = RpiWeather()

display.set_raw64(value=sunny_bitmap,matrix=1)