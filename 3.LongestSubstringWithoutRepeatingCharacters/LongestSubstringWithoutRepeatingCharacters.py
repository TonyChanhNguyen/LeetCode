class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_temp = ""
        s_result = ""
        len_max = 0
        for index in range(len(s)):
          if((index + 1) == len(s)):
            if(len(s_temp) > len_max):
                len_result = s_temp
                s_temp = ""
            else:
                len_result = len_result
          else:
            if s[index] not in s_temp:
                s_temp += s[index]
            else:
                if(len(s_temp) > len_max):
                  len_max = len(s_temp)
                  len_result = s_temp
                  s_temp = ""
                else:
                  continue
                s_temp = s[index]

        return len(len_result)

# Tesing stage
test = Solution()
print(test.lengthOfLongestSubstring("abcbbxyzk"))