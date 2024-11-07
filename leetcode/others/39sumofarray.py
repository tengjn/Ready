# 输入：candidates = [2,3,6,7], target = 7
# 输出：[[2,2,3],[7]]


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.result = []
        self.path = []
        self.dfs(0, candidates, target)
        return self.result
    def dfs(self, start_index, candidates, target):
        if sum(self.path) == target:
            self.result.append(self.path[:])
            return
        if sum(self.path) > target:
            return
        for i in range(start_index, len(candidates)):
            self.path.append(candidates[i])
            self.dfs(i, candidates, target)
            self.path.pop()
        # for idx, item in enumerate(candidates[start_index:]):
        #     self.path.append(item)
        #     self.dfs(idx + start_index, candidates, target)
        #     self.path.pop()

candidates = [2,3,5]
target = 8
a = Solution()
result = a.combinationSum(candidates, target)
print(result)