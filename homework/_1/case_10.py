#-*- coding:utf-8 -*-

class Solution():
    def solve(self, A):
        result = {}
        for i in A:
            result.setdefault(i, 0)
        for i in A:
            result[i] += 1
        return result;