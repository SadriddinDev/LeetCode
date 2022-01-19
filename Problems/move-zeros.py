class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = None
        for i in range(len(nums)):
            if l is None:
                if nums[i] == 0:
                    l = i
            elif nums[i] != 0:
                    nums[l], nums[i] = nums[i], nums[l]
                    l += 1