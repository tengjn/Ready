## 装满背包的方案数量, 每个物品只能用1次
## 背包容量：5
## 物品重量：[1, 2, 3, 5]
## dp = dp[i - 1] + dp[i - 2] .. + dp[i - 5]

class Solution():
    def solve(self, capacity, weight):
        dp = [0 for i in range(capacity + 1)]
        dp[0] = 1
        for w in weight:
            for i in range(capacity, w - 1, -1): ## 必须到w - 1
                if i >= w:
                    dp[i] += dp[i - w]
        print(dp)
        return dp[capacity]

    
a = Solution()
capacity = 5
weights = [1, 2, 3, 4, 5]
print(a.solve(capacity, weights))

## 1. 方案是否重复：内外层循环
## 2. 每个物品是否能取多次：内层循环倒序