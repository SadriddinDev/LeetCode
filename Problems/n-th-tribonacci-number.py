class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 2:
            return n
        a,b,c = 1,1,2
        i = 1
        while i < n:
            a, b, c = b, c, a+b+c
            i += 1
        return a