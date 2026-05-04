from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n-1):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()


matrix = [
    [5,1,9,11],
    [2,4,8,10],
    [13,3,6,7],
    [15,14,12,16]
]
matrix2 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

Solution().rotate(matrix)
assert matrix == [
    [15,13,2,5],
    [14,3,4,1],
    [12,6,8,9],
    [16,7,10,11]
]

Solution().rotate(matrix2)
assert matrix2 == [
    [7,4,1],
    [8,5,2],
    [9,6,3]
]