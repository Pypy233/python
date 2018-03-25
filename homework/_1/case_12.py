#-*- coding:utf-8 -*-
from math import floor
class Solution():
    def solve(self):
        a = 18.985
        b = 21.015
        avg = (a + b) / 2
        df = a + b - 2 * avg
        sd = 1.015 * 6 / 2.03
        return [avg, floor(sd)]
