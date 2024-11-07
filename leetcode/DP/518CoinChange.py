# 给定不同面额的硬币 coins 和金额 amount。写出函数来计算可以凑成该金额的硬币组合数。假设每一种面额的硬币有无限个。
## 不重复的方案数

# 输入: amount = 5, coins = [1, 2, 5]
# 输出: 4
# 解释: 有四种方式可以凑成总金额:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1

## 去重的完全背包
# class Solution():
#     def solve(self, coins, target):
#         dp = [0 for i in range(target + 1)]
#         dp[0] = 1
#         for j in range(len(coins)):
#             for i in range(1, target + 1):
#                 if i >= coins[j]:
#                     dp[i] += dp[i - coins[j]]
            
#         return dp[target]


## dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 5] 
class Solution():
    def solve(self, coins, target):
        dp = [0 for i in range(target + 1)]
        dp[0] = 1
        combinations = [[] for _ in range(target + 1)]
        combinations[0] = [[]]
        for coin in coins:
            for i in range(target+1):
                if i >= coin:
                    dp[i] += dp[i - coin]
                    for prev_combination in combinations[i - coin]:
                        new_combination = prev_combination + [coin]
                        combinations[i].append(new_combination)
        return dp[target], combinations
    

a = Solution()
result, combinations = a.solve(coins=[1,2,5], target=5)
for comb in combinations:
    print(comb)








# 先遍历物品，再遍历背包容量，dp数组存储的是方案组合数；先遍历背包容量，再遍历物品，dp数组存储的就是方案排列数。
# 01背包的遍历顺序分为两种：
# 一维dp数组只能先遍历物品，再遍历背包，即外层物品，内层背包，且内层倒序，从大到小
# 二维dp数组内外层无要求，先背包先物品均可

# 完全背包的遍历顺序要视情况而定：
# 纯完全背包的一维dp数组实现，背包和物品的先后顺序无要求，均是从小到大
# 求排列数时，外层背包，内层物品
# 求组合数时，外层物品，内层背包


# 倒序遍历是为了保证物品i只被放入一次！。但如果一旦正序遍历了，那么物品0就会被重复加入多次！
# 举一个例子：物品0的重量weight[0] = 1，价值value[0] = 15
# 如果正序遍历
# dp[1] = dp[1 - weight[0]] + value[0] = 15
# dp[2] = dp[2 - weight[0]] + value[0] = 30
# 此时dp[2]就已经是30了，意味着物品0，被放入了两次，所以不能正序遍历。
# 为什么倒序遍历，就可以保证物品只放入一次呢？
# 倒序就是先算dp[2]
# dp[2] = dp[2 - weight[0]] + value[0] = 15  （dp数组已经都初始化为0）
# dp[1] = dp[1 - weight[0]] + value[0] = 15
# 所以从后往前循环，每次取得状态不会和之前取得状态重合，这样每种物品就只取一次了。
# 那么问题又来了，为什么二维dp数组历的时候不用倒序呢？
# 因为对于二维dp，dp[i][j]都是通过上一层即dp[i - 1][j]计算而来，本层的dp[i][j]并不会被覆盖！


# 再来看看两个嵌套for循环的顺序，代码中是先遍历物品嵌套遍历背包容量，那可不可以先遍历背包容量嵌套遍历物品呢？
# 不可以！
# 因为一维dp的写法，背包容量一定是要倒序遍历（原因上面已经讲了），如果遍历背包容量放在上一层，那么每个dp[j]就只会放入一个物品，即：背包里只放入了一个物品。
# （这里如果读不懂，就在回想一下dp[j]的定义，或者就把两个for循环顺序颠倒一下试试！）