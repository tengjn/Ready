## 操作只包括删除/替换/添加
## dp[i][j] str1的前i个字符到str2的前j个字符编辑需要的最小次数

class Solution:
    def solve(self, str1, str2):
        m, n = len(str1), len(str2)
        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
            


        return dp[m][n]
    
a = Solution()
str1 = "intention"
str2 = "execution"
print(a.solve(str1, str2))