class Solution:
    def isValidSudoku(self, board) -> bool:
        for i in range(9):
            nums = []
            nums2 = []
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in nums:
                        return False
                    else:
                        nums.append(board[i][j])
                if board[j][i] != ".":
                    if board[j][i] in nums2:
                        return False
                    else:
                        nums2.append(board[j][i])
        for i in range(3):
            for j in range(3):
                nums = []
                for i1 in range(3):
                    for j1 in range(3):
                        b = board[i*3+i1][j*3+j1]
                        if b != ".":
                            if b in nums:
                                return False
                            else:
                                nums.append(b)
        return True
