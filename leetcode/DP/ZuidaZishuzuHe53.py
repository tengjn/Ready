# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4] 输出：6
# 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
# 输入：nums = [1] 输出：1
# 输入：nums = [5,4,-1,7,8] 输出：23

# dp[i] = max(nums[i], dp[i - 1] + nums[i])
class Solution():
    def solve(self, nums):
        if len(nums) == 1:
            return nums[0]
        result = float('-inf')
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
            result = max(result, dp[i])
        return result
    

a = Solution()
print(a.solve(nums=[-2,1,-3,4,-1,2,1,-5,4]))
print(a.solve(nums=[1]))
print(a.solve(nums=[5,4,-1,7,8]))