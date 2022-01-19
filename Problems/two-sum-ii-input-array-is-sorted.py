# class Solution:
#     def twoSum(self, numbers, target: int):
#         for i in range(len(numbers)-1):
#             j = target - numbers[i]
#             try:
#                 index = numbers[i+1:].index(j)
#                 return [i+1, index+1+ i+1]
#             except:
#                 pass
class Solution:
    def twoSum(self, numbers, target: int):
        l = 0
        r = len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1