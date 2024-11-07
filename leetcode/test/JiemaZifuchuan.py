# input: "abc3[mn]xy"
# return: "abcmnmnmnxy"

## "bb3[a2[c]]"
## "bbaccaccacc"
class Solution:
    def decodeString(self, s):
        result = ""
        idx = 0
        stack = [] ## stack.append() stack.pop() stack[-1]
        for idx in range(len(s)):
            if s[idx] == "]":
                ## start to pop
                tmp = ""
                while True:
                    ## pop until meet [
                    if len(stack) > 0 and stack[-1] == "[":
                        stack.pop()
                        break
                    tmp += stack.pop()
                copy_num = int(stack.pop())
                for i in range(copy_num):
                    for ch in tmp[::-1]:
                        stack.append(ch)
            else:
                stack.append(s[idx])
        for item in stack:
            result += item
        return result

a = Solution()
print(a.decodeString(s="bb3[a2[c]]"))