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
            tmp_cnt = 1
            print(right)
            while right < len(nums) and nums[right] == base:

                if tmp_cnt <= 2:
                    nums[left] = base
                    left += 1
                    cnt += 1
                    tmp_cnt += 1

                tmp_cnt += 1
                right += 1
            if right < len(nums):
                base = nums[right]
                nums[left] = base
                left += 1
                right += 1
                cnt += 1

        return cnt

a = Solution()
nums = [1,1,1,2,2,3]
a.removeDuplicates(nums)