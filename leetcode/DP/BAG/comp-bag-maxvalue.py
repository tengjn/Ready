# capacity = 5
# weights = [1, 2, 3, 4], values = [2, 4, 4, 5]
# result = 10
# 每个物品可以选择多次
## dp[i] = max(dp[i], dp[i - weights[j]] + values[j])
class Solution:
    def solve(self, capacity, weights, values):
        dp = [0 for i in range(capacity + 1)]
        dp[0] = 0
        for i in range(capacity + 1):
            for j in range(len(weights)):
                if i >= weights[j]:
                    dp[i] = max(dp[i], dp[i - weights[j]] + values[j])
        return dp[capacity]

a = Solution()
capacity = 5
weights = [1, 2, 3, 4]
values = [2, 4, 4, 5]
print(a.solve(capacity, weights, values))