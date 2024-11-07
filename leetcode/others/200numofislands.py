class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        cnt = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == '0':
                    continue
                self.dfs(grid, i, j)
                cnt += 1
        return cnt

    def dfs(self, grid, i, j):
        if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] == '0':
            return
        print('*******')
        for item in grid:
            print(item)
        grid[i][j] = '0'

        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)


# class Solution:
#     def numIslands(self, grid: [[str]]) -> int:
#         def dfs(grid, i, j):
#             if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j] == '0':
#                 return
#             grid[i][j] = '0'
#             dfs(grid, i + 1, j)
#             dfs(grid, i, j + 1)
#             dfs(grid, i - 1, j)
#             dfs(grid, i, j - 1)
#         count = 0
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == '1':
#                     dfs(grid, i, j)
#                     count += 1
#         return count

a = Solution()
grid = grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
result = a.numIslands(grid)
print(result)