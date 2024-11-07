
# 输入: nums = [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。

# 输入: nums = [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组

class Solution():
    def solut(self, nums):
        if len(nums) == 1:
            return nums[0]
        dpmax = [0] * len(nums)
        dpmin = [0] * len(nums)
        dpmax[0] = nums[0]
        dpmin[0] = nums[0]
        result = max(dpmax[0], dpmin[0])
        
        for i in range(1, len(nums)):
            dpmax[i] = max(nums[i], dpmax[i - 1]*nums[i], dpmin[i - 1] * nums[i])
            dpmin[i] = min(nums[i], dpmax[i - 1]*nums[i], dpmin[i - 1] * nums[i])

            result = max(result, dpmax[i], dpmin[i])
            
        return result

a = Solution()
print(a.solut(nums=[-2, 3, -4]))