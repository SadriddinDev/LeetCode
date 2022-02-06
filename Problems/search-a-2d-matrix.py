class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        role_1 = True  # all sorted
        role_2 = False # isset targint in matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if j == 0:
                    if i != 0:
                        role_1 = role_1 and (matrix[i-1][-1] <= matrix[i][j])
                else:
                    role_1 = role_1 and (matrix[i][j-1] <= matrix[i][j])
                role_2 = role_2 or (matrix[i][j] == target)
        return role_1 and role_2

                    