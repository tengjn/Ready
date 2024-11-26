# 给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。
# 返回这三个数的和。
# 假定每组输入只存在恰好一个解。
## [-4, -1, 1, 2]
# 输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2)。

class Solution():
    def solve(self, nums, target):
        nums.sort()
        diff = 100000
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[i] + nums[right] + nums[left]
                if sum < target:
                    left += 1
                if sum > target:
                    right -= 1
                if sum == target:
                    return sum


                if abs(sum - target) < diff:
                    diff = abs(sum - target)
                    result = sum
                
        return result
a = Solution()
print(a.solve(nums=[-1,2,1,-4], target=1))
print(a.solve(nums=[0,0,0], target=1))
