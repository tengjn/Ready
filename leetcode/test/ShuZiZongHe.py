# 输入：candidates = [2,3,6,7], target = 7
# 输出：[[2,2,3],[7]]
# 解释：
# 2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
# 7 也是一个候选， 7 = 7 。
# 仅有这两种组合。
# 示例 2：

# 输入: candidates = [2,3,5], target = 8
# 输出: [[2,2,2,2],[2,3,3],[3,5]]

class Solution():
    def solut(self, nums, target):
        self.path = []
        self.results = []
        self.dfs(nums, target, 0)
        return self.results

    def dfs(self, nums, target, start):
        if sum(self.path) == target:
            # self.path.sort()
            # if self.path not in self.results:
            self.results.append(self.path[:])
            return
        if sum(self.path) > target:
            return
        for i in range(start, len(nums)):
            self.path.append(nums[i])
            self.dfs(nums, target, i)
            self.path.pop()
        
a = Solution()
print(a.solut(nums=[2,3,6,7], target=7))