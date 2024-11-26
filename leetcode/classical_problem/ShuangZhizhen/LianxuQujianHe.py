# 一个正整数数组，寻找连续区间使得和等于target
# [2,3,1,4,6,3] target=6
class Solution():
    def solve(self, nums, target):
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

a = Solution()
print(a.solve(nums=[2,3,1,4,6,3], target=6))