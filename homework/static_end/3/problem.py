#-*- coding:utf-8 -*-
from scipy.stats import norm
from math import sqrt
class Solution:
    def solve(self):
        mean, var, n, alpha, s = 8.5, 25.0, 3600.0, 0.05, 0
        z_val = norm.isf(alpha/2)
        s = sqrt(var/n) * z_val
        return [-s + mean, s + mean]