## 不用额外空间移除指定元素
# 输入：nums = [3,2,2,3], val = 3
# 输出：2, nums = [2,2]
# 解释：函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。你不需要考虑数组中超出新长度后面的元素。例如，函数返回的新长度为 2 ，而 nums = [2,2,3,3] 或 nums = [2,2,0,0]，也会被视作正确答案。
class Solution:
    def removeElement(self, nums, val):
        right = 0
        left = 0
        new_len = 0
        while (right <= left and right < len(nums) and left < len(nums)):
            if not nums[left] == val:
                nums[right] = nums[left]
                right += 1
                new_len += 1
            left += 1

a = Solution()
a.removeElement([0,1,2,2,3,0,4,2], 2)


