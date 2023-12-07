## Description
Given a string 's', find the length of the longest 
substring
 without repeating characters.

Example 1:
```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

Example 2:
```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

Example 3:
```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```
## Explaination about subsequence and substring.
+ A substring is a contiguous part of a string.
+ A subsequence is a sequence that can be derived from another sequence by removing zero or more elements, without changing the order of the remaining elements.
```
String = "geeks"
+ substring start with:
    + g: 
        + g
        + ge
        + gee
        + geek
        + geeks
    + e:
        + e
        + ee
        + eek
        + eeks
    + e:
        + e
        + ek
        + eks
    + ....
+ subsequence start with:
    g, e, e, k, s,
    ge, ge, gk, gs, ee, ek, es, ek, es, ks,
    gee, gek, ges, gek, ges, gks, eek, ees, eks, eks,
    geek, gees, eeks,
    geeks
```

## Idea
#### Check if in the end of loop. Compare length of temporary variable less than s_temp, do nothing. Else, temporary variable is the result
```
        if((index + 1) == len(s)):
            if(len(s_temp) > len_max):
                len_result = s_temp
                s_temp = ""
            else:
                len_result = len_result
```
#### Define temporary variable
```
        s_temp = ""     # Temporary variable to save substring
        s_result = ""   # Variable to store the result
        len_max = 0     # Calculate length of temporary variable
```
#### Get each element of string.
```
        for index in range(len(s)):
``` 

#### If this item do not exist in temporary variable. Put it into temporary variable.
```
        if s[index] not in s_temp:
            s_temp += s[index]
```

#### If this item exist in temporary variable. Check length of temporary variable if lager than len_max. Set it for len_max and save value of temporary variable to result. Reset temporary variable to blank.
```
        if(len(s_temp) > len_max):
            len_max = len(s_temp)
            len_result = s_temp
            s_temp = ""
```

#### Else, continue with next element.
```
        else:
            continue
```
####  Set value of temporary variable as item.
```
        s_temp = s[index]
```   

#### Return the longest length of substring.
```
        return len(len_result)
```

#### Example
s = "abcbbxyzk" => Expected result: ``5``, which returned substring is ``bxyzk``.
+ Loop 0/9: (Not yet start)
```
        index       = null
        s[index]    = ""
        s_temp      = ""     
        s_result    = ""   
        len_max     = 0     
```
+ Loop 1/9: 
```
        index       = 0
        s[index]    = "a"        # s[index] do not exist in s_temp 
        s_temp      = "a"        # Then, add s[index] to s_temp
        s_result    = ""  
        len_max     = 0    
```
+ Loop 2/9: 
```
        index       = 1
        s[index]    = "b"       # s[index] do not exist in s_temp 
        s_temp      = "ab"      # Then, add s[index] to s_temp  
        s_result    = ""   
        len_max     = 0     
```
+ Loop 3/9: 
```
        index       = 2
        s[index]    = "c"       # s[index] do not exist in s_temp 
        s_temp      = "abc"     # Then, add s[index] to s_temp  
        s_result    = ""   
        len_max     = 0     
```
+ Loop 4/9: 
```
        index       = 3
        s[index]    = "b"       # s[index] exist in s_temp 
        s_temp      = ""        # Reset s_temp to blank
        s_result    = "abc"     # Save value before resetting of s_temp to result
        len_max     = 3         # Calculate length of s_temp before resetting
```
+ Loop 5/9: 
```
        index       = 4
        s[index]    = "b"       # s[index] do not exist in s_temp 
        s_temp      = "b"       # Then, add s[index] to s_temp
        s_result    = "abc"     
        len_max     = 3         
```
+ Loop 6/9: 
```
        index       = 5
        s[index]    = "x"       # s[index] do not exist in s_temp 
        s_temp      = "bx"      # Then, add s[index] to s_temp
        s_result    = "abc"     
        len_max     = 3         
```
+ Loop 7/9: 
```
        index       = 6
        s[index]    = "y"      # s[index] do not exist in s_temp 
        s_temp      = "bxy"    # Then, add s[index] to s_temp
        s_result    = "abc"     
        len_max     = 3         
```
+ Loop 8/9: 
```
        index       = 7
        s[index]    = "z"      # s[index] do not exist in s_temp 
        s_temp      = "bxyz"   # Then, add s[index] to s_temp
        s_result    = "abc"     
        len_max     = 3         
```
+ Loop 9/9 (end of loop): 
```
        index       = 8         # At the end of loop, len(s_temp) is 5 lager than 3.
        s[index]    = "k"       # s[index] do not exist in s_temp 
        s_temp      = ""        # Reset s_temp to blank
        s_result    = "bxyzk"   # The result is value of s_temp  
        len_max     = 5        
```

## Full code [here](./LongestSubstringWithoutRepeatingCharacters.py)