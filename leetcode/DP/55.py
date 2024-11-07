# 跳跃游戏
# 输入：nums = [2,3,1,1,4]
# 输出：true
# 解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        idx = 0

        while idx < len(nums):
            if idx == len(nums) - 1:
                return True
            if nums[idx] == 0:
                return False

            jump = nums[idx]
            idx += jump
            if idx >= len(nums):
                return False


nums = [2,3,1,1,4]
a = Solution()
result = a.canJump(nums)
print(result)