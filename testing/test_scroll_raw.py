# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 20:19:06 2022

@author: johwi
"""

# BITMAP = [
# [1, 1, 1, 1, 1, 1, 1, 1,],
# [1, 1, 0, 0, 0, 0, 0, 1,],
# [1, 0, 1, 0, 0, 0, 0, 1,],
# [1, 0, 0, 1, 0, 0, 0, 1,],
# [1, 0, 0, 0, 1, 0, 0, 1,],
# [1, 0, 0, 0, 0, 1, 0, 1,],
# [1, 0, 0, 0, 0, 0, 1, 1,],
# [1, 0, 0, 0, 0, 0, 0, 1,],
# ]






value = 0x9142183dbc184289 # sunny bitmap
buffer = bytearray([0]*16)
print(buffer)

for step in range(7,-1,-1):
    for old_row in range(7,0,-1):
        buffer[old_row*2] = buffer[(old_row-1)*2]
        new_row = (value >> (8*step)) & 0xff
        new_row = (new_row << 7 | new_row >> 1) & 0xff  #fix for memory buffer error
        buffer[0] = new_row

print(buffer)

f = open('/tmp/myimage.jpeg', 'wb')
f.write(bytearray(buffer))
f.close()

import time

matrices = [0,0,0,0]
matrix = 0
delay = 0.15

for step in range(7,-1,-1):
    for old_row in range(7,0,-1):
        matrices[matrix].buffer[old_row*2] = matrices[matrix].buffer[(old_row-1)*2]
    new_row = (value >> (8*step)) & 0xff
    new_row = (new_row << 7 | new_row >> 1) & 0xff  #fix for memory buffer error
    matrices[matrix].buffer[0] = new_row
    matrices[matrix].show()
    time.sleep(delay)  







foobar = []

value = 0x9142183dbc184289

# go from 7 to 0
for step in range(7,-1,-1):
    # go from 7 to 1
    for old_row in range(7,0,-1):
        
        foo = old_row*2
        bar = (old_row-1)*2
        # print(f"foo:{foo}")
        # print(f"bar:{bar}")
        foobar.append(foo)
        foobar.append(bar)
        
        new_row = (value >> (8*step)) & 0xff
        new_row = (new_row << 7 | new_row >> 1) & 0xff  #fix for memory buffer error
        print(f"current step: {step}")
        print(f"current row: {old_row}")
        # new_row = (value >> (8*step)) & 0xff
        # print(new_row)
        # print(f'new row: {new_row}')




