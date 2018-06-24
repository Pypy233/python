#-*- coding:utf-8 -*-
from math import sqrt
from scipy.stats import t

class Solution():
    def solve(self):
        n, std1, std2, mean1, mean2, group_num, s = 44, 45.1, 26.4, 52.1, 27.1, 2, 0
        alpha = 0.05
        n1 = n2 = n / group_num
        sw = sqrt(((n1 - 1) * (std1 ** 2) + (n2 - 1) * (std2 ** 2)) / (n1 + n2 - 2))
        hold = t.isf(alpha / 2, n1 + n2 - 2)
        t_val = (mean1 - mean2) / (sw * sqrt(1.0 / n1 + 1.0 / n2))
        s = abs(t_val) < hold
        return [n1 - 1, round(t_val, 2), s]