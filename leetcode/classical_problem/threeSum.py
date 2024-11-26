# 找出三个数之和恰好为0的组合
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]

class Solution():
    def solve(self, nums, target):
        result = []
        nums.sort()
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] == target:
                    result.append([nums[i], nums[left], nums[right]])

                elif nums[i] + nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1

                while nums[left] == nums[left + 1]:
                    left += 1
                left += 1
                while nums[right] == nums[right - 1]:
                    right -= 1
                right -= 1
        return result

a = Solution()
print(a.solve(nums=[-1,0,1,2,-1,-4], target=0))
