# 括号生成
# 输入：n = 3

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 1:
            return [1]
        if n == 2:
            return [[1],[1, 1]]
        result = [[1], [1,1]]
        for i in range(n - 2):
            source = result[-1]
            tmp_result = [1]
            for j in range(len(source)- 1):
                tmp_result.append(source[j] + source[j+1])
            tmp_result.append(1)
            result.append(tmp_result)
        print(result)

nums = 5
a = Solution()
result = a.generateParenthesis(nums)
print(result)