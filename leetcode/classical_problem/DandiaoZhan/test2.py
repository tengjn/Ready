## 环形数组的单调栈问题 [2,1,2,4,3] 
## 返回数组, 每个元素而言下一个比它大的元素 [4,2,4,-1,4], 左右都算


class Solution():
    def solve(self, nums):
        ans = [-1] * len(nums)
        stack = []
        for i in range(2*len(nums)):
            i = i % len(nums)
            while stack and nums[i] > nums[stack[-1]]:
                ans[stack.pop()] = nums[i]
            stack.append(i)
        return ans

a = Solution()
print(a.solve(nums=[2,1,2,4,3]))
            
