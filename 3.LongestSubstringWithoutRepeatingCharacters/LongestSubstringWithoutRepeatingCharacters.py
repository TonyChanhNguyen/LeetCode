class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        length = 0
        for right in range(len(s)):
            char = s[right]
            if char in seen and seen[char] >= left:
                left = seen[char] + 1
            else:
                length = max(length, right - left + 1)
            seen[char]  = right
        return length


# Tesing stage
test = Solution()
print(test.lengthOfLongestSubstring("dvdf"))

