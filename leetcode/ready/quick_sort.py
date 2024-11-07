class QucikSort(object):
    def solution(self, nums, l, r):
        i = l
        j = r
        temp = nums[l]
        if j < i:
            return
        while(i < j):
            while(nums[j] > temp and i < j):
                j -= 1
            while(nums[i] < temp and i < j):
                i += 1

            nums[i], nums[j] = nums[j], nums[i]

        nums[l] = nums[i]
        nums[i] = temp

        self.solution(nums, i + 1, r)
        self.solution(nums, l, i - 1)