# -*- coding: utf-8 -*-
"""
Spyder Editor

Dies ist eine temporäre Skriptdatei.
"""

import time

def time2int(time_struct, format24=False):
    """Convert time, passed in as a time.struct_time object, to an integer with
    hours in the hundreds place and minutes in the units place. Returns 24
    hour format if format24 is True, 12 hour format (default) otherwise.
    """
    if not isinstance(time_struct, time.struct_time):
        return None
    h = time_struct.tm_hour
    m = time_struct.tm_min
    if not format24:
        h = h if h <= 12 else h - 12
    return h*100+m

local_time = time.localtime()


new_val = time2int(time.localtime())