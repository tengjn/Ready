# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
# 输入：n = 3
# 输出：3

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0]* (n + 1)
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

    def climbStaris_dfs(self, n):
        self.result = []
        self.path = []
        self.dfs(n, 0)
        print(self.result)

    ## 若想保存每个方案 需要用回溯法遍历每一个方案
    def dfs(self, n, count):
        if count == n:
            self.result.append(self.path[:])
            return
        if count > n:
            return

        self.path.append(1)
        self.dfs(n, count + 1)
        self.path.pop()

        self.path.append(2)
        self.dfs(n, count + 2)
        self.path.pop()

n = 4
a = Solution()
result = a.climbStaris_dfs(n)
print(result)



