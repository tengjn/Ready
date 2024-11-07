# 要 解码 已编码的消息，所有数字必须基于上述映射的方法，反向映射回字母（可能有多种方法）。例如，"11106" 可以映射为：
# "AAJF" ，将消息分组为 (1 1 10 6)
# "KJF" ，将消息分组为 (11 10 6)


class Solution(object):
    def numDecodings(self, nums):
        """
        :type s: str
        :rtype: int
        """
        self.path = []
        self.results = []
        self.dfs(0, nums)
        print(self.results)

    def dfs(self, idx, nums):
        if idx == len(nums):
            self.results.append(self.path[:])
            return
        if idx > len(nums):
            return

        if '0' == nums[idx]:
            pass
        else:
            self.path.append(nums[idx])
            self.dfs(idx + 1, nums)
            self.path.pop()

            self.path.append(nums[idx:idx + 2])
            self.dfs(idx + 2, nums)
            self.path.pop()

nums = "11106"
a = Solution()
result = a.numDecodings(nums)
print(result)
