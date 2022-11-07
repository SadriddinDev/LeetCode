class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
      for row in matrix:
        if row[0] <= target <= row[-1]:
          l, r = 0, len(row)-1
          while l <= r:
            m = (l+r)//2
            if row[m] == target:
              return True
            elif row[m] < target:
              l = m + 1
            else:
              r = m + 1
      return False


print(Solution().searchMatrix([[-1]], -1))
