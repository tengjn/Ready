# 给一个数组
# 对于原数组中的第i个元素, 至少往右走多少步, 才能遇到一个比自己大的元素
# 没有则返回-1
# input: [5,3,1,2,4]
# return: -1 3 1 1 -1

class Solution():
    def solve(self, nums):
        stack = []
        ans = [-1] * len(nums)
        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                cur_idx = stack.pop()
                ans[cur_idx] = i - cur_idx
            stack.append(i)
        print(ans)

a = Solution()
a.solve(nums=[5,3,1,2,4])

