# 给定一个由正整数组成且不存在重复数字的数组 nums，找出和为给定目标正整数 target 的组合的个数。顺序不同的序列视作不同的组合。

# 示例：nums = [1, 2, 3]，target = 4。所有可能的组合为：
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)

## 求方案数量 ## 本质就是爬楼梯 ## 不取重的完全背包
# dp[k] = dp[k - 1] + dp[k - 2] + dp[k - 3]
# return dp[target]
# dp[0] = 0
class Solution():
    def solve(self, coins, target):
        dp = [0 for i in range(target + 1)]
        dp[0] = 1
        for i in range(1, target + 1):
            for j in range(len(coins)):
                if i >= coins[j]:
                    dp[i] += dp[i - coins[j]]
            
        return dp[target]
    
a = Solution()
print(a.solve(coins=[1,2,3], target=4))