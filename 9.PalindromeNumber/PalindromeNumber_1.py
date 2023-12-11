class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s[:len(s)] == s[::-1]


test = Solution()
print(test.isPalindrome(121))
