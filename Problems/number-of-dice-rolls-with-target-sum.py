class Solution:
    mdict = {}
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if target < n or target > n*k:
            return 0
        if n == 1:
            return 1 if target <= k else 0
        key = (n, k, target)
        if self.mdict.get(key):
            return self.mdict.get(key)
        else:
            summa = 0
            for i in range(1, k+1):
                summa += self.numRollsToTarget(n-1, k, target - i)
                summa %= (10**9+7)
            self.mdict[key] = summa
            return summa