class island(object):
    def dfs(self, island, isvisited, i, j):
        if island[i][j] == '0' or isvisited[i][j] or i > len(island) or j > len(island[0]):
            return
        isvisited[i][j] = 1
        self.dfs(island, isvisited, i - 1, j)
        self.dfs(island, isvisited, i + 1, j)
        self.dfs(island, isvisited, i, j - 1)
        self.dfs(island, isvisited, i, j + 1)



    def solution(self, island):
        isvisited = []
        result = 0
        for i in range(len(island)):
            for j in range(len(island[0])):
                if island[i][j] == "0" or isvisited[i][j]:   ## !!!
                    continue                                 ## !!!
                self.dfs(island, isvisited, i, j)            ## !!!
                result += 1