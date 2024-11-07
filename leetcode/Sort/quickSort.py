# 输入：[1,10,4,5,2,7,3,9,6,8]


class Solution(object):
    def partition(self, nums, left, right):
        ref = nums[left]
        while left < right:
            while (left < right and nums[right] >= ref):
                right -= 1
            nums[left] = nums[right]
            while (left < right and nums[left] <= ref):
                left += 1
            nums[right] = nums[left]
        nums[left] = ref
        return left

    def quickSort(self, nums, left, right):
        if left < right:
            privor_idx = self.partition(nums, left, right)
            self.quickSort(nums, left, privor_idx-1)
            self.quickSort(nums, privor_idx + 1, right)


    def findTopK(self, nums, left, right, K):
        if left < right:
            privor_idx = self.partition(nums, left, right)
            if privor_idx == K - 1:
                print(nums[:K])
                return
            elif privor_idx > K - 1:
                self.findTopK(nums, left, privor_idx - 1, K)
            else:
                self.findTopK(nums, privor_idx + 1, right, K)



nums = [1,10,4,5,2,7,3,9,6,8]
# a = Solution()
# a.quickSort(nums, 0, len(nums)-1)
# a.findTopK(nums, 0, len(nums)-1, 2)


## 指定idx做partition, 将比他小的搬到左边, 比他大的搬到右边，用交换实现更方便
left = 0
right = len(nums) - 1

ref_idx = 3
ref = nums[ref_idx]
while (left < right):
    while (left < right and nums[right] >= ref):
        right -= 1

    while (left < right and nums[left] <= ref):
        left += 1
    nums[right], nums[left] = nums[left], nums[right]

nums[ref_idx], nums[left] = nums[left], nums[ref_idx]

print(nums)

