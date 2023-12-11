class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x < 0):
            return False
        else:
            temp_x = x
            reverse_x = 0
            while temp_x != 0:
                reverse_x = reverse_x*10 + temp_x%10
                temp_x = temp_x //10
            return reverse_x == x

test = Solution()
print(test.isPalindrome(-123))
print(test.isPalindrome(1221))
