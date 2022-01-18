# class Solution:
#     def rotate(self, nums, k: int):
#         n = len(nums)
#         ans = nums[:]
#         for i in range(n):
#             index = i + k
#             if index >= n:
#                 index %= n
#             nums[index] = ans[i]
class Solution:
    def rotate(self, nums, k: int):
        for i in range(k):
            nums.insert(0, nums.pop(-1))
        print(nums)

        
        
Solution().rotate([1,2,3,4,5,6,7], 3)