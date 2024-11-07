# 输入：nums = [1,2,3]
# 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.results = []
        self.out = []
        self.dfs(nums, 0)
        return self.results
    def dfs(self, nums, idx):
        self.results.append(self.out[:])
        
        for i in range(idx, len(nums)):
            self.out.append(nums[i])
            self.dfs(nums, i+1)
            self.out.pop()
    

nums = [1,2,3]
a = Solution()
result = a.subsets(nums)
print(result)