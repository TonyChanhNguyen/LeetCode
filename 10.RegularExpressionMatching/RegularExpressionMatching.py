class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # full_right_flag = False
        # result = False
        # for i in range(len(p)):
        #     if(p[i] == "*"):
        #         if(p[i-1] == "."):
        #             return True
        #         else:
        #             full_right = p[i-1]
        #             full_right_flag = True
        #     elif(p[i] == "."):
        #         continue
        #     else:
        #         if(full_right_flag):
        #             if(s[i] == full_right):
        #                 result = True
        #             else:
        #                 return False
        #         else:
        #             if(s[i] == p[i]):
        #                 continue
        #             else:
        #                 return False
        # return result
        for i in range(len(p)):
            if(p[i:i+2] ==".*"):
                return True
            else:
                if(a[i] == p[i]):
                    continue
                else:
                    if(p[i+1] == "*"):
                        continue
                    else:
                        return False
test = Solution()
print(test.isMatch("abs","a*s"))