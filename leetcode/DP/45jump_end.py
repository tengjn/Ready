# 输入: nums = [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
# 从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。

### 维护每个位置能被跳过来的起跳位置再dp
class Solution:
    def jump(self, nums):
        dp = [1000000] * len(nums)
        dp[0] = 0
        dict = {}
        for i in range(0, len(nums)):
            for j in range(i, i + nums[i] + 1):
                if j < len(nums):
                    if not j in dict:
                        dict[j] = []
                    dict[j].append(i)

        for i in range(1, len(nums)):
            for v in dict[i]:
                dp[i] = min(dp[v] + 1, dp[i])

    def jump2(self, nums):
        ans = 0
        start = 0
        end = 1
        while end < len(nums):
            maxPose = 0
            for i in range(start, end):
                maxPose = max(maxPose, i + nums[i])
            start = end + 1
            end += maxPose
        return ans

# a = Solution()
# a.jump2([2,3,1,1,4])
