class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2 ** 31 - 1 # 2,147,483,647
        MIN_INT = -2 ** 31    #-2,147,483,648
        flag_x = 1
        if(x == 0):
            return 0
        elif( x > 0):
            flag_x = 1
        elif(MIN_INT > x or x > MAX_INT):
            return 0
        else:
            flag_x = -1
        x = flag_x*x
        length = len(str(x))
        result = 0
        index = 0
        num_1 = 0
        num_2 = x
        for i in range(length):
            num_1 = num_2 % 10          
            num_2 = num_2 // 10                
            index = length - i -1       
            result += num_1* 10**index
        result = result*flag_x
        if(MIN_INT > result or result > MAX_INT):
            return 0
        else:
            return result
test = Solution()
print(test.reverse(-123))

