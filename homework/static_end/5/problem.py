#-*- coding:utf-8 -*-
from math import sqrt
from scipy.stats import t
class Solution():
    def solve(self):
        n, mean, std, s = 51.0, 1.1, 4.9, 1
        alpha = 0.05
        t_val = mean / (std / sqrt(n))
        hold = t.ppf(alpha, n - 1)
        s = t_val >= hold
        return [n - 1, round(t_val, 2), s]