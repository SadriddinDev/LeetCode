class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        while n > 0:
            if (n // 3)*3 == n:
                n = n // 3
            else:
                return n == 1
