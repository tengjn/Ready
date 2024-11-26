## heights = [2,1,5,6,2,3] return 10
## heights = [2,4] return 4

# class Solution(object):
#     def largestRectangleArea(self, heights):
#         """
#         :type heights: List[int]
#         :rtype: int
#         """
#         stack = []
#         ans = [-1] * len(heights)
#         for i in range(len(heights)):
#             while stack and heights[i] < heights[stack[-1]]: ## 注意比较的是值 而stack存的是索引
#                 ans[stack.pop()] = i
#             stack.append(i)
#         result = -1
#         for i in range(len(heights)):
#             if ans[i] == -1:
#                 cur_height = heights[i]
#             else:
#                 cur_height = heights[i] * (ans[i] - i)
#             result = max(result, cur_height)
#         while stack:
#             idx = stack.pop()
#             result = max(result, heights[idx] * (len(heights) - idx))
#         return result


class Solution(object): ## 还是双向的
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        result = 0
        newHeights = heights.copy()
        newHeights.insert(0, 0)
        newHeights.append(0)
        stack.append(0)
        ans = [-1] * len(newHeights)
        for i in range(1, len(newHeights)):
            while stack and newHeights[i] < newHeights[stack[-1]]: ## 注意比较的是值 而stack存的是索引
                cur_index = stack.pop()
                currentHeight = newHeights[cur_index]
                if currentHeight == 1:
                    print(stack, i)
                width = i - stack[-1] - 1
                result = max(result, currentHeight * width)
            stack.append(i)
        return result


a = Solution()
# print(a.largestRectangleArea(heights=[2,1,5,6,2,3])) ## 10
# print(a.largestRectangleArea(heights=[2,4]))         ## 4
# print(a.largestRectangleArea(heights=[1,1]))         ## 2
print(a.largestRectangleArea(heights=[2,1,2]))       ## 3