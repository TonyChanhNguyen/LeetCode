## Description
#### URL: [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
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

#### Define temporary variable
```python
        result = {}       # To store the result
        left = 0          # Break point
        length = 0        # The longest length
```
#### Get each element of string.
```python
        for right in range(len(s)):
``` 

#### If this item exist in temporary variable and its index larger or equal than ``left``. Calculate ``left`` by sum of its index plus 1.
```python
        if char in seen and seen[char] >= left:
            l = seen[char] + 1
```

#### Else, calculate length.
```python
        else:
            length = max(length, right - left + 1)
```

#### Then, update index of char with right.
```python
        seen[char]  = right
```
#### Return the longest length of substring.
```python
        return length
```

#### Example
s = "abcbbxyzk" => Expected result: ``5``, which returned substring is ``bxyzk``.
+ Loop 0/9: (Not yet start)
```python
        seen        = null
        char        = null
        left        = null
        right       = null   
        length      = null
```
+ Loop 1/9: 
```python
        seen        = {"a" : 0,}
        char        = "a"
        left        = 0
        right       = 0  
        length      = max(0 , 0 - 0 + 1) = 1
```
+ Loop 2/9: 
```python
        seen        = {"a" : 0,"b" : 1}
        char        = "b"
        left        = 0
        right       = 1  
        length      = max(1 , 1 - 0 + 1) = 2
```
+ Loop 3/9: 
```python
        seen        = {"a" : 0,"b" : 1,"c" : 2}
        char        = "c"
        left        = 0
        right       = 2  
        length      = max(2 , 2 - 0 + 1) = 3
```
+ Loop 4/9: 
```python
        seen        = {"a" : 0,"b" : 3,"c" : 2}
        char        = "b"
        left        = 1 + 1 = 2 # seen["b"] = 1
        right       = 3  
        length      = max(3 , 3 - 2 + 1) = 3
```
+ Loop 5/9: 
```python
        seen        = {"a" : 0,"b" : 4,"c" : 2}
        char        = "b"
        left        = 3 + 1 = 4 # seen["b"] = 3
        right       = 4  
        length      = max(3 , 4 - 4 + 1) = 3   
```
+ Loop 6/9: 
```python
        seen        = {"a" : 0,"b" : 4,"c" : 2,"x" : 3}
        char        = "x"
        left        = 4
        right       = 5  
        length      = max(3 , 5 - 4 + 1) = 3          
```
+ Loop 7/9: 
```python
        seen        = {"a" : 0,"b" : 4,"c" : 2,"x" : 5,"y" : 6}
        char        = "y"
        left        = 4
        right       = 6  
        length      = max(3 , 6 - 4 + 1) = 3            
```
+ Loop 8/9: 
```python
        seen        = {"a" : 0,"b" : 4,"c" : 2,"x" : 5,"y" : 6,"z" : 7}
        char        = "z"
        left        = 4
        right       = 7  
        length      = max(3 , 7 - 4 + 1) = 4      
```
+ Loop 9/9 (end of loop): 
```python
        seen        = {"a" : 0,"b" : 4,"c" : 2,"x" : 5,"y" : 6,"z" : 7,"k" : 8}
        char        = "k"
        left        = 4
        right       = 8  
        length      = max(3 , 8 - 4 + 1) = 5  
```

## Full code [here](./LongestSubstringWithoutRepeatingCharacters.py)