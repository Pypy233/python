#-*- coding:utf-8 -*-

class Solution():
    def solve(self, A):
        #call function prime
        lst = []
        for i in A:
            if self.prime(i):
                lst.append(i)
        return lst
    

    #judge whether x is prime or not
    def prime(self, x):
        if x <= 0 or x == 1:
            return False;
        if x == 2:
            return True
        for i in range(2, x//2):
            if x % i == 0:
                return False
        return True
       