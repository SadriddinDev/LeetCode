class Solution:
    def matrixReshape(self, mat, r: int, c: int):
        m = len(mat)
        n = len(mat[0])
        if m*n == r*c and m != r:
            nmat = []
            temp = []
            for i in range(m):
                for j in range(n):
                    temp.append(mat[i][j])
                    if len(temp) == c:
                        nmat.append(temp)
                        temp = []
            return nmat
        else:
            return mat
