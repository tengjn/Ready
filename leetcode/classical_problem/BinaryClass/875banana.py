

# 珂珂喜欢吃香蕉。这里有 n 堆香蕉，第 i 堆中有 piles[i] 根香蕉。警卫已经离开了，将在 h 小时后回来。
# 珂珂可以决定她吃香蕉的速度 k （单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 k 根。
# 如果这堆香蕉少于 k 根，她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉。  
# 返回她可以在 h 小时内吃掉所有香蕉的最小速度 k（k 为整数）

## 查找首先想到二分
## 闭区间模板
class Solution():    
    def solve(self, piles, h):
        left = 1  ## 注意不能是0
        right = max(piles)
        while left <= right:
            mid = left + ((right - left) // 2)
            print(left, right, mid)
            cost = sum([(pile-1)//mid+1 for pile in piles])
            if cost > h:
                left = mid + 1
            else:
                right = mid - 1

        return left
a = Solution()

# print(a.solve(piles=[3,6,7,11], h=8)) ## 4
# print(a.solve(piles=[30,11,23,4,20], h=5)) ## 30
# print(a.solve(piles=[30,11,23,4,20], h=6)) ## 23
print(a.solve(piles=[312884470], h=968709470))







