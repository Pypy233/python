#-*- coding:utf-8 -*-
import numpy as np

class Solution():
    def solve(self, A):
        g = np.array(A)
        f = np.array([2.0,0.0,-1.0,1.0])
        g1 = np.poly1d(g)
        f1 = np.poly1d(f)
        print(g1)
        print(f1)
        return g1 * f1