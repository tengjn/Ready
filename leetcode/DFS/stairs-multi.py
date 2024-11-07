## 每次爬1-k步
class Solution:
    def solve(self, height, k):
        dp = [0 for i in range(height + 1)]
        
        dp[0] = 1 ## attention

        for i in range(1, height + 1):
            for j in range(1, k + 1):
                if i >= j:
                    dp[i] += dp[i - j]
        return dp[height]

    def solve2(self, height, k):
        self.path = []
        self.result = []
        self.dfs(height, k)
        return self.result
    
    def dfs(self, n, k):
        if sum(self.path) > n:
            return
        if sum(self.path) == n:
            self.result.append(self.path[:])
            return
        for i in range(1, k + 1): ## 没有0步
            self.path.append(i)
            self.dfs(n, k)
            self.path.pop()

a = Solution()

print(len(a.solve2(height=10, k=3)))
print(a.solve(height=10, k=3))
print(a.solve2(height=10, k=3))