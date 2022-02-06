class Solution:
    def generate(self, numRows: int):
        pascal = []
        if numRows > 0:
            pascal.append([1])
        if numRows > 1:
            pascal.append([1, 1])
        for _ in range(numRows-2):
            pascal.append([1] + [pascal[-1][j] + pascal[-1][j+1]
                          for j in range(len(pascal[-1])-1)] + [1])
        return pascal
