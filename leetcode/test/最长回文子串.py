class Solution():
    def solu(self, str):
        result = ""
        for idx in range(len(str)):
            for cmp_idx_l in [idx, idx - 1]:
                cmp_idx_r = idx + 1
                while(cmp_idx_l >= 0 and cmp_idx_r < len(str) and str[cmp_idx_l] == str[cmp_idx_r]):
                    cmp_idx_l -= 1
                    cmp_idx_r += 1
                
                cmp_idx_l += 1
                cmp_idx_r -= 1
                if len(str[cmp_idx_l:cmp_idx_r + 1]) > len(result):
                    result = str[cmp_idx_l:cmp_idx_r + 1]
        return result
a = Solution()
print(a.solu(str="ckkakkcb"))