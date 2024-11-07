class Solution:

    def dfs(self, grid, x, y):

        row = len(grid)
        col = len(grid[0])
        if x >= row or x < 0 or y >= col or y < 0 or grid[x][y] == '0':
            return
        grid[x][y] = '0'

        self.dfs(grid, x + 1, y)
        self.dfs(grid, x - 1, y)
        self.dfs(grid, x, y + 1)
        self.dfs(grid, x, y - 1)

    def numIslands(self, grid):
        row, col, ret = len(grid), len(grid[0]), 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    ret += 1
        return ret
