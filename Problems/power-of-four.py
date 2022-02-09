class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
        while n > 0:
            if (n // 4)*4 == n:
                n = n // 4
            else:
                return n == 1
