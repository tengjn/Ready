
def findNoRepeat(nums):
    l = 0
    r = len(nums) - 1
    result = []
    while (l < r):
        if abs(nums[l]) > abs(nums[r]):
            result.append(abs(nums[l]))
            l += 1
            while l < r and nums[l] == nums[l - 1]:
                l += 1

        elif abs(nums[l]) < abs(nums[r]):
            result.append(abs(nums[r]))
            r -= 1
            while l < r and nums[r] == nums[r + 1]:
                r -= 1
        else:
            result.append(abs(nums[l]))
            l += 1
            r -= 1
            while l < r and nums[l] == nums[l - 1]:
                l += 1
            while l < r and nums[r] == nums[r + 1]:
                r -= 1


    print(result)

findNoRepeat([-5, -5, -4, 0, 3, 4, 5, 5, 6])
