# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 23:38:58 2022

@author: johwi
"""

BITMAP = [
[1, 1, 1, 1, 1, 1, 1, 1,],
[1, 1, 0, 0, 0, 0, 0, 1,],
[1, 0, 1, 0, 0, 0, 0, 1,],
[1, 0, 0, 1, 0, 0, 0, 1,],
[1, 0, 0, 0, 1, 0, 0, 1,],
[1, 0, 0, 0, 0, 1, 0, 1,],
[1, 0, 0, 0, 0, 0, 1, 1,],
[1, 0, 0, 0, 0, 0, 0, 1,],
]

row_bytes = []
values = []

value = 0
for y,row in enumerate(BITMAP):
    row_byte = 0
    for x,bit in enumerate(row):
        row_byte += bit<<x
    row_bytes.append(row_byte)
    values.append(row_byte<<(8*y))
    value += row_byte<<(8*y)

row_bytes_sum = sum(row_bytes)

print(value)
print(format(value,'02x'))
print('0x'+ format(value,'02x'))


value=0x81c1a191898583ff
value=9349931947847418879

for y in range(8):
    row_byte = value >> (8*y)
    print(row_byte)
    for x in range(8):
        pixel_bit = row_byte >> x & 0x01 
        
        
row_byte = value >> 8*0
# is first shifted by 0 and then logical operation with 1
pixel_bit = row_byte >> 0 & 0x01

36523171671278979 >> 1

