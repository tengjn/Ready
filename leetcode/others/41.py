# 给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。
#
# 输入：nums = [1,2,0]
# 输出：3
#
# 输入：nums = [3,4,-1,1]
# 输出：2



class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash = []
        for item in nums:
            if item >= 0:
                hash[item]


a = Solution()
nums = [3,4,-1,1]
target = 1
result = a.searchRange(nums, target)
print(result)

