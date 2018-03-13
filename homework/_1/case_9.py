#-*- coding:utf-8 -*-

class Solution():
    def solve(self, A):
        lst = {}
        for i in range(0, 10):
            lst.setdefault(i, 0)
        for i in A:
            for c in i:
                lst[ord(c) - ord('0')] += 1
        return lst