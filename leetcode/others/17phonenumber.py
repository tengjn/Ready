# 输入：digits = "23"
# 输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]

class Solution(object):
    def __init__(self):
        self.results = []
        self.path = []
        self.table = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        self.backtrace(digits, 0)
        return self.results

    def backtrace(self, digits, index):
        if len(self.path) == len(digits):
            path_str = ""
            for i in self.path:
                path_str += i
            self.results.append(path_str)
            return
        for i in self.table[digits[index]]:
            self.path.append((i))
            self.backtrace(digits, index + 1)
            self.path.pop()

a = Solution()
results = a.letterCombinations("2")
print(results)