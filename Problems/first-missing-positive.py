class Solution:
    def firstMissingPositive(self, nums) -> int:
        nums = sorted(list(set([i for i in nums if i > 0])))
        for i in range(len(nums)):
            if i+1 != nums[i]:
                return i+1
        return len(nums)+1
        
    # wich hashtable method
    # def firstMissingPositive(self, nums: List[int]) -> int:
    #     k = 1
    #     hashT = {}
    #     for i in nums:
    #         hashT[i] = 1
    #     for _ in nums:
    #         if hashT.get(k)==None:
    #             return k
    #         else:
    #             k+=1
    #     return k

print(Solution().firstMissingPositive([1, 1000]))
