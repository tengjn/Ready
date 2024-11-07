# 物品数量n = 3, 背包容量capacity = 5
# weights = [1, 2, 3], values = [6, 10, 12]
# 最大价值：22
# 选择物品 2 和物品 3，总重量为 2 + 3 = 5，总价值为 10 + 12 = 22。

# n = 4  capacity = 5
# weights = [2, 3, 4, 5]  values = [3, 4, 5, 6]
# 最大价值：7
# 选择物品 1 和物品 2，总重量为 2 + 3 = 5，总价值为 3 + 4 = 7。

# n = 4, capacity = 7
# weights = [1, 3, 4, 5]values = [1, 4, 5, 7]
# 最大价值：9
# 选择物品 2 和物品 3，总重量为 3 + 4 = 7，总价值为 4 + 5 = 9。

# n = 5, capacity = 10
# weights = [2, 2, 6, 5, 4], values = [6, 3, 5, 4, 6]
# 最大价值：15
# 选择物品 1、物品 2 和物品 5，总重量为 2 + 2 + 4 = 8，总价值为 6 + 3 + 6 = 15。


# dp[i] = max(dp[i], dp[i - weights[j] + values[j]])

class Solution():
    def solve_maxValue(self, n, capacity, weights, values):
        dp = [0 for i in range(capacity + 1)]
        dp[0] = 0
        for j in range(n):
            for i in range(capacity, weights[j] - 1, -1):
                if i >= weights[j]:
                    dp[i] = max(dp[i], dp[i - weights[j]] + values[j])
        return dp[capacity]
    
a = Solution()
n = 3
capacity = 5
weights = [1, 2, 3]
values = [6, 10, 12] # ---> 22
print(a.solve(n, capacity, weights, values))

## 1. 方案是否重复：内外层循环
## 2. 每个物品是否能取多次：内层循环倒序