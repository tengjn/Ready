
## 递增栈: 遇到小的才开始pop, 找右侧第一个比自己小的元素
## 递减栈：遇到大的才开始pop, 找右侧第一个比自己大的元素

class Solution:
    def solve(self, nums):
        stack = []
        ans = nums.copy()
        for i in range(len(nums)):
            print(nums[i])
            print([nums[item] for item in stack])
            while stack and nums[i] < nums[stack[-1]]: ## 递增or递减
                ans[stack.pop()] = nums[i]
            
            stack.append(i)
        print([nums[item] for item in stack])
        return ans
    
    def solve2(self, nums): ## 找左边
        stack = []
        ans = nums.copy()
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[i] < nums[stack[-1]]:
                ans[stack.pop()] = nums[i]
            stack.append(i)
        return ans


a = Solution()
print(a.solve(nums=[3,4,2,6,9,7,8]))
# print(a.solve2(nums=[3,4,2,6,9,7,8]))

