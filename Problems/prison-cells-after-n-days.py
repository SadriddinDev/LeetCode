class Solution:
    def prisonAfterNDays(self, cells, n: int):
        cash = []
        for _ in range(n):
            new_cells = [0]*8
            for j in range(1, 7):
                if cells[j-1] == cells[j+1]:
                    new_cells[j] = 1
            if new_cells in cash:
                k = n % (len(cash) - cash.index(new_cells))
                return cash[cash.index(new_cells)+k-1]
            else:
                cells = new_cells
                cash.append(new_cells)
        return cells
