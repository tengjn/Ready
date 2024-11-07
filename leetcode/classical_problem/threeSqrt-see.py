def findThreeSqrt(target):

    # 负数情况
    neg_flag = False
    if target < 0:
        neg_flag = True
        target = -target
    # 对于小数情况 left从0搜, right不能从target搜, 要从1搜
    if abs(target) < 1:
        left = 0
        right = max(1, target)
    else:
        left = 1
        right = target

    a = (right + left) / 2
    while(abs(a*a*a - target) > 0.000001):
        if a*a*a < target:
            left = a
        else:
            right = a
        a = (right + left) / 2
    if neg_flag:
        return -a
    return a

# result = findThreeSqrt(8)
# print(result)