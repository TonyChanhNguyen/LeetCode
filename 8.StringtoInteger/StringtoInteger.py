class Solution:
    def myAtoi(self, s: str) -> int:
        MAX_INT = 2 ** 31 - 1 # 2,147,483,647
        MIN_INT = -2 ** 31    #-2,147,483,648
        def checkOutOfRange(num : int) -> int:
            if (num > MAX_INT):
                return MAX_INT
            elif (num < MIN_INT):
                return MIN_INT
            else:
                return num
        list_accept = "0123456789"
        isNumberStarted = False
        isPositive  = True
        num = 0
        for i in range(len(s)):
            if s[i] in list_accept:
                num = num*10 + int(s[i])
                isNumberStarted = True
            elif(isNumberStarted):
                break
            else:
                if s[i] == "+":
                    isPositive = True
                    isNumberStarted = True
                elif s[i] == "-":
                    isPositive = False
                    isNumberStarted  = True
                elif s[i] == " ":
                    continue
                else:
                    break  
        return checkOutOfRange(num if isPositive else num*-1)

test = Solution()
print(test.myAtoi(" 123c456 HelloWorld"))
