## Q1
# 输入：nums = [1,2,3]
# 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

## Q2
# 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
# 你可以按 任何顺序 返回答案。
# 输入：n = 4, k = 2
# 输出：[[2,4],[3,4],[2,3],[1,2],[1,3],[1,4]]

## Q3
# 输入: candidates = [2,3,5], target = 8
# 输出: [[2,2,2,2],[2,3,3],[3,5]]

## Q4 全排列
# 输入: [1,2,3]
# 输出: [1,2,3] [1,3,2] ...

class Solution:
    def solve(self, nums):
        self.path = []
        self.result = []
        self.dfs(0, nums)
        return self.result
    
    def dfs(self, index, nums):
        if self.path not in self.result:
            self.result.append(self.path[:])
        for i in range(index, len(nums)):
            self.path.append(nums[i])
            self.dfs(i + 1, nums)
            self.path.pop()


a = Solution()
print(a.solve(nums = [1,2,3]))