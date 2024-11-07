class Stairs(object):

    def search(self):
        self.path = []
        self.results = []
        self.dfs()

    def dfs(self):
        if sum(self.path) == 10:
            self.results.append(self.path[:])
            return
        if sum(self.path) > 10:
            return

        self.path.append(1)
        self.dfs()
        self.path.pop()

        self.path.append(2)
        self.dfs()
        self.path.pop()
    def solve2(self, n):
        dp = [0 for i in range(n + 1)]
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

a = Stairs()
a.search()
print(len(a.results))
