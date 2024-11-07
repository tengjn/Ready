# (a1,a2,a3,a4,a5)=(-5,11,-4,13,-4-2)时，最大子段和为11+(-4)+13=20
## dp[i]以第i个位置为结尾时的子序列和
class Solution:
    # def maxSum(self, nums):
    #     result = -1
    #     for i, _ in enumerate(nums):
    #         start = 0
    #         for j in range(i, len(nums)):
    #             start += nums[j]
    #             result = max(result, start)
            
    #     return result
    
    
    def maxSum(self, nums):
        dp = [nums[0]] * len(nums)
        result = dp[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i-1] + nums[i]) ## dp[i - 1] < 0 or not
            result = max(result, dp[i])
        return result
    
nums = [-5,11,-4,13,-4-2]
a = Solution()
print(a.maxSum(nums))