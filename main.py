# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 14:22:33 2020

@author: anton
"""


# hw model - synthesizable operations only
def anlz_byte(src_byte):
    wrk_byte = src_byte
    msb_detected = False
    msb = 0
    for i in range(0, 8):
        if (wrk_byte & 0x1) != 0:
            msb_detected = True
            msb = i
        wrk_byte = wrk_byte >> 1
    return msb_detected, msb


def msb(x):
    byte_msb = [0, 0, 0, 0]
    byte_msb_detected = [False, False, False, False]

    byte_msb_detected[0], byte_msb[0] = anlz_byte((x >> 0) & 0xff)
    byte_msb_detected[1], byte_msb[1] = anlz_byte((x >> 8) & 0xff)
    byte_msb_detected[2], byte_msb[2] = anlz_byte((x >> 16) & 0xff)
    byte_msb_detected[3], byte_msb[3] = anlz_byte((x >> 24) & 0xff)

    msb = 0
    for i in range(0, 4):
        if byte_msb_detected[i]:
            msb = byte_msb[i] + (i << 3)

    return msb


# generating stimulus
for i in range(0, 16):
    x = pow(2, (i * 2) + 1) + i * 333
    print("x: " + '0x{:08x}'.format(x) + ", msb: " + str(msb(x)))