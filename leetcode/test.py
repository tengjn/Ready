# 一个正整数数组，寻找连续区间使得和等于target
# [2,3,1,4,6,3] target=6
class Solution():
    def solve(self, nums, target): ## 只有正整数
        left = 0
        right = left
        sum = nums[left]
        result = []
        while left <= right and right < len(nums):
            if sum < target:
                right += 1
                if right < len(nums):
                    sum += nums[right]
            elif sum > target:
                sum -= nums[left]
                left += 1
            elif sum == target:
                result.append(nums[left:right+1])
                right += 1
                if right < len(nums):
                    sum += nums[right]
        return result
    
    ## 有负数的情况, 我第一时间的想法, dp[i]代表以第i个元素为结尾的全部区间和的情况
    def solve2(self, nums, target): 
        dp = [0] * len(nums)
        dp[0] = [nums[0]]
        result = []
        for i in range(1, len(nums)):
            dp[i] = [nums[i] + item for item in dp[i - 1]]
            dp[i].append(nums[i])
        
        for i in range(len(dp)):
            for j in range(len(dp[i])):
                if dp[i][j] == target:
                    result.append(nums[j : i + 1])

        print(result)

    ## 有负数的情况, 官方解法前缀和
    def solve3(self, nums, target):

        prefix_sum_map = {0: -1}  # 初始化前缀和为0的索引为-1, 对应0号元素前缀和为0的情况
        current_sum = 0
        result = []

        for i in range(len(nums)):
            current_sum += nums[i]

            if (current_sum - target) in prefix_sum_map:
                start = prefix_sum_map[current_sum - target] + 1
                result.append((start, i))

            prefix_sum_map[current_sum] = i

        return result



a = Solution()
# print(a.solve(nums=[2,3,1,4,6,3], target=6))
print(a.solve3(nums=[2,-1,3,-4,5], target=4))