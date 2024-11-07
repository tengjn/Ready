# 输入：nums = [0,0,1,1,1,2,2,3,3,4]
# 输出：5, nums = [0,1,2,3,4]
# 解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。

class Solution:
    def removeDuplicates(self, nums):
        left = 1
        right = 1
        cnt = 1
        base = nums[0]

        while (left <= right and left < len(nums) and right < len(nums)):
            if nums[right] == base:
                right += 1
            else:
                base = nums[right]
                nums[left] = base
                left += 1
                right += 1
                cnt += 1


        # print(cnt)
        # print(nums[:cnt])
        return cnt

a = Solution()
a.removeDuplicates([1,2,3])