# 输入：nums = [1,2,3,4]
# 输出：[1234 1,234 12,34, 123,4 1,23,4 1,2,3,4 12,34 ...]





class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        self.out = []
        self.dfs(nums, 0)

        return self.result

    def dfs(self, nums, idx):
        if self.out not in self.result and idx == 4:
            self.result.append(self.out[:])
        for i in range(idx, len(nums)):
            if not nums[idx:i+1]:
                continue
            self.out.append(nums[idx:i+1])
            self.dfs(nums, i+1)
            self.out.pop()
            
    
nums = [1,2,3,4]
a = Solution()
result = a.subsets(nums)
for item in result:
    print(item)
    
    
## 分割后第idx个元素的可能性
# 1                12          123            1234
# 2 23 234         3 34        4