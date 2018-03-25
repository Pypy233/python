#-*- coding:utf-8 -*-

class Solution():
    def solve(self):
        n = 25
        mean = 7.73
        sd = 0.77
        min = 6.17
        max = 9.78
        u = 8
        t = (mean - u) / (sd / (n ** 0.5))
        return[n - 1, round(t, 2), False]