# 括号生成
# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.result = []
        self.path = []
        self.dfs(n, 0, 0)
        return self.result

    def dfs(self, n, left, right):
        if left == n and right == n:
            self.result.append(''.join(self.path[:]))
            return
        if left < n:
            self.path.append("(")
            self.dfs(n, left + 1, right)
            self.path.pop()
        if left > 0 and right < n and right < left:
            self.path.append(")")
            self.dfs(n, left, right + 1)
            self.path.pop()

nums = 4
a = Solution()
result = a.generateParenthesis(nums)
print(result)