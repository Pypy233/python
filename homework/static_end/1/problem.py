class Solution():
    def solve(self, A):
        return [i for i in A if self.prime(i)]

    #judge whether x is prime or not
    def prime(self, x):
        if x == 1 or x == 2 or x == 3:
            return True
        if x == 4:
            return False
        if x <= 0:
            return False
        for i in range(2, x/2):
            if x % i == 0:
                return False
        return True