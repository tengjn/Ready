def maxWeight(nums):
    stack = [0]*len(nums)
    result = -1

    for i in range(len(nums)):
        while stack and nums[stack[-1]] > nums[i]:
            tmp = nums[stack.pop()]
            if stack:
                left = stack[-1]
            else:
                left = -1
            result = max(result, tmp * (i - left - 1))
        stack.append(i)
    return result

result = maxWeight([9,8,7,2,7,8,9])
print(result)