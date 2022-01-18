class Solution:
    def sortedSquares(self, nums):
        ans = []
        for num in nums:
            n = num*num

            l, r = 0, len(ans)-1
            while l <= r:
                m = (l + r) // 2
                if ans[m] == n:
                    l = m
                    break
                elif ans[m] > n:
                    r = m - 1
                else:
                    l = m + 1
            ans.insert(l, n)
        return ans

# second way
# class Solution:
#     def sortedSquares(self, nums: List[int]) -> List[int]:
#         return list(map(lambda x:x**2, sorted(nums, key=abs)))
		