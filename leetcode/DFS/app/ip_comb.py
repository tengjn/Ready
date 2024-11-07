# 输入"25525522135",返回["255.255.22.135", "255.255.221.35"]
# 输入"1111",返回[1.1.1.1]
# 1ip地址由四个整数组成；
# 2每个整数的范围是[0,255]；
# 3四个整数通过逗号分隔符连接
# 4每个整数除了它本身是0的情况之外，不能以0开头


class Solution:
    def solve(self, str):
        self.path = []
        self.result = []
        self.dfs(str, 0)
        return self.result
    def dfs(self, str, idx):
        if len(self.path) > 4:
            return
        if idx > len(str):
            return
        if idx == len(str) and len(self.path) == 4:
            return self.result.append(self.path[:])

        if idx + 1 > len(str) or str[idx:idx+1][0] == '0':
            return
            
        self.path.append(str[idx:idx+1])
        self.dfs(str, idx+1)
        self.path.pop()

        if idx + 2 > len(str) or str[idx:idx+2][0] == '0':
            return
        self.path.append(str[idx:idx+2])
        self.dfs(str, idx+2)
        self.path.pop()

        if idx + 3 > len(str) or str[idx:idx+3][0] == '0':
            return
        if int(str[idx:idx+3]) <= 255:
            self.path.append(str[idx:idx+3])
            self.dfs(str, idx+3)
            self.path.pop()

a = Solution()
print(a.solve(str="25525522135"))
print(a.solve(str="1111"))
print(a.solve(str="000256"))