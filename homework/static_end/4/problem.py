#-*- coding:utf-8 -*-
from math import sqrt
from scipy.stats import t
class Solution():
    def solve(self):
        mean, sigma, alpha, n, s = 4.6, 2.2, 0.05, 20, 0
        claim = 5
        t_val = (mean - claim)/(sigma/sqrt(n))
        hold = t.ppf(alpha, n - 1)
        s = t_val > hold
        return [n -1, round(t_val, 2), s]