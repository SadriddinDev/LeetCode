class Solution:
    def floodFill(self, image, sr: int, sc: int, newColor: int):
        checked = []
        m = len(image)
        n = len(image[0])
        oldColor = image[sr][sc]
        def dfs(i, j):
            if [i, j] in checked:
                return
            checked.append([i, j])
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if image[i][j] == oldColor:
                image[i][j] = newColor
                dfs(i-1, j)
                dfs(i, j-1)
                dfs(i+1, j)
                dfs(i, j+1)
        dfs(sr, sc)
        return image

print(Solution().floodFill([[0,0,0],[0,1,1]],1,1,4))