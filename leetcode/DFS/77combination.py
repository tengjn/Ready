# 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
# 你可以按 任何顺序 返回答案。

# 输入：n = 4, k = 2
# 输出：
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]

class Solution(object):
    def __init__(self):
        self.result = []
        self.path = []
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.backtrace(n, k, 1)
        return self.result

    def backtrace(self, n, k, start_index):
        if len(self.path) == k:
            self.result.append(self.path[:])
            return
        for i in range(start_index, n + 1):
            self.path.append(i)
            self.backtrace(n, k, i + 1)
            self.path.pop()

a = Solution()
result = a.combine(4, 2)
print(result)

