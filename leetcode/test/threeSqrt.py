
class Solution:
    def threeSqrt(self, num):
        if num < 0:
            neg_flag = True
        if num > 0:
            neg_flag = False
        if num == 0:
            return 0
        num = abs(num)
        
        if num > 1:
            left = 1
            right = num
            
        elif num < 1:
            left = num
            right = 1
        else:
            return 1
        middle = (left + right) / 2
        while abs(middle * middle * middle - num) > 0.0001:
            if (middle * middle * middle) > num:
                right = middle
            elif (middle * middle * middle) < num:
                left = middle
            else:
                return middle
            middle = (left + right) / 2
        
            
        
        if neg_flag:
            middle = -middle
        
        return middle


if __name__ == '__main__':
    num = 0.008
    a = Solution()
    
    result = a.threeSqrt(num)
    print(num, result)
