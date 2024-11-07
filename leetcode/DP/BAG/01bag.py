# 最大子数组和
# vector<int> weight = {1, 3, 4};   //各个物品的重量
# vector<int> value = {15, 20, 30}; //对应的价值
# int bagWeight = 4;                //背包最大能放下多少重的物品

# weights = [3, 5, 7, 2, 6]
# values = [6, 10, 12, 4, 8]
# bagWeight = 10
# result = 20

class Solution(object):
    def bag(self, weights, values, capacity):
        n = len(weights)
        dp = [[0] * (capacity + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for w in range(1, capacity + 1):
                if weights[i - 1] > w:
                    dp[i][w] = dp[i - 1][w]
                else:
                    dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])

        return dp[n][capacity]

    ## 每个物体放或不放
    # def dfs(self, weights, values, capacity, idx):
    #
    #     if idx == len(weights) and capacity >= 0:
    #         self.result.append(self.path[:])
    #         return
    #     if idx >= len(weights):
    #         return
    #     self.path.append(weights[idx])
    #     self.dfs(weights, values, capacity - weights[idx], idx + 1)
    #     self.path.pop()
    #
    #     self.path.append(-1)
    #     self.dfs(weights, values, capacity, idx + 1)
    #     self.path.pop()
    #
    # def bag(self, weights, values, capacity):
    #     self.result = []
    #     self.path = []
    #     self.dfs(weights, values, capacity, 0)
    #     print(self.result)
    #     final_res = -1
    #     for res in self.result:
    #         total_val = 0
    #         for idx, r in enumerate(res):
    #             if r > 0:
    #                 total_val += values[idx]
    #         final_res = max(final_res, total_val)
    #
    #     return final_res

    # 跳过某个物体, 没有return, 循环结束自动return
    # def dfs(self, weights, values, capacity, idx):
    #
    #     if capacity >= 0:
    #         self.result.append(self.path[:])
    #
    #     for i in range(idx, len(weights)):
    #         self.path.append(weights[i])
    #         self.dfs(weights, values, capacity - weights[i], i + 1)
    #         self.path.pop()
    #
    # def bag(self, weights, values, capacity):
    #     self.result = []
    #     self.path = []
    #     self.dfs(weights, values, capacity, 0)
    #     print(self.result)
    #     return

weights = [3, 5, 7, 2, 6] # [3, 5, 2]
values = [6, 10, 12, 4, 8]
bagWeight = 10

a = Solution()
result = a.bag(weights, values, bagWeight)
print(result)

