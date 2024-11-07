# 给定一个候选人编号的集合candidates和一个目标数target，找出candidates中所有可以使数字和为target的组合。
#
# candidates中的每个数字在每个组合中只能使用一次。
#
# 注意：解集不能包含重复的组合。
#
# 输入: candidates =[10,1,2,7,6,1,5], target =8,
# 输出:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# 输入: candidates = [2,5,2,1,2], target = 5,
# 输出:
# [
# [1,2,2],
# [5]

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.path = []
        self.result = []
        candidates.sort()
        self.dfs(0, candidates, target)
        return self.result
    def dfs(self, start_index, candidates, target):
        if sum(self.path) == target:
            self.result.append(self.path[:])
            return
        if sum(self.path) > target:
            return
        for i in range(start_index, len(candidates)):
            if i > start_index and candidates[i-1] == candidates[i]:   # 去重
                continue
            self.path.append(candidates[i])
            self.dfs(i + 1, candidates, target)
            self.path.pop()

candidates = [10,1,2,7,6,1,5]
target = 8
a = Solution()
result = a.combinationSum2(candidates, target)
print(result)
