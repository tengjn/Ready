# 输入：x = 123
# 输出：321
# 示例 2：
#
# 输入：x = -123
# 输出：-321
# 示例 3：
#
# 输入：x = 120
# 输出：21

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg_flag = False
        if x < 0:
            x = -x
            neg_flag = True
        str_x = self.int2str(x)
        result = 0

        zero_flag = True
        for idx, i in enumerate(str_x):
            if not i == "0":
                zero_flag = False
            if not zero_flag:
                result = 10*result + int(i)
        if neg_flag:
            return -result
        return result


    def int2str(self, x):
        result = ""
        while (x > 0):
            digit = x % 10
            print(digit)
            x = x // 10
            result += str(digit)
        return result

nums = 901000
a = Solution()
result = a.reverse(nums)
print(result)