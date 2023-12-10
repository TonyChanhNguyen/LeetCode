## Description
#### URL: https://leetcode.com/problems/longest-palindromic-substring
Given a string s, return the longest palindromic substring in s.

Example 1:
```
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
```
Example 2:
```
Input: s = "cbbd"
Output: "bb"
```


#### Constraints:

+ 1 <= s.length <= 1000
+ s consist of only digits and English letters.

## Idea
#### Define a function name 'expand' with input parameter 'l' and 'r'.
+ Set a loop condition with l larger than or equal to 0, r less than length of string 's' and value of string at index r and l equal each other.
    + Decrease l with 1
    + Increase r with 
+ Return value of string s at index 'l+1' to 'r'. 
```
def expand(l,r):
    while (l >=0 and r < len(s) and s[l] == s[r]):
        l -= 1
        r += 1
    return s[l+1:r]
```