class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        return int(((1+n)/2)*n - sum(nums))
