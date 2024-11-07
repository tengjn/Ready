# 输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
# 输出：7
# 解释：因为路径 1→3→1→1→1 的总和最小。

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = grid[0][0]

        for i in range(1, len(dp[0])):
            dp[0][i] = dp[0][i-1] + grid[0][i]

        for j in range(1, len(dp)):
            dp[j][0] = dp[j-1][0] + grid[j][0]

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]



a = Solution()
grid = [[1,3,1],[1,5,1],[4,2,1]]
result = a.minPathSum(grid)
print(result)