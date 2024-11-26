# 给定不同面额的硬币 coins 和金额 amount，计算凑成总金额所需的最少的硬币个数。如果没有任何一种方案能组成该金额，返回 -1。每种硬币的数量是无限的。

# 求最小硬币数量
# 输入: coins = [1, 2, 5], amount = 11
# 输出: 3 
# 解释: 11 = 5 + 5 + 1
# dp[k] = min(dp[k - 1], dp[k - 2], dp[k - 5]) + 1
# return dp[amount]
# dp[0] = 0

class Solution:
    def solve(self, coins, amount):
        dp = [float('inf') for i in range(amount + 1)]
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin]) + 1

        if dp[amount] > amount:
            return -1
        return dp[amount]

a = Solution()
print(a.solve(coins=[1, 2, 5], amount=11))


# dp[i][j] = min(dp[i-1][j], dp[i][j-coins[i-1]]) + 1
# dp[j] =    min(dp[j],      dp[j - coin])        + 1