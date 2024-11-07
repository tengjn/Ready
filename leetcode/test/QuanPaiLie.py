class Solution:
    def solut(self, nums):
        self.path = []
        self.result = []
        self.dfs(nums)
        return self.result

    def dfs(self, nums):
        if len(self.path) == len(nums):
            self.result.append(self.path[:])
        for i in range(len(nums)):
            if not nums[i] in self.path:
                self.path.append(nums[i])
                self.dfs(nums)
                self.path.pop()
                
a = Solution()
print(a.solut(nums=[1,2,3]))