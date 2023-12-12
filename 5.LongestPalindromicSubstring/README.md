## Description
#### URL: [Longest Palindromic substring](https://leetcode.com/problems/longest-palindromic-substring)
Given a string s, return the longest palindromic substring in s.

#### Example 1:
```
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
```
#### Example 2:
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
```python
def expand(l,r):
    while (l >=0 and r < len(s) and s[l] == s[r]):
        l -= 1
        r += 1
    return s[l+1:r]
```

#### Run a loop with range is length of string
```python
for i in range (len(s)):
``` 
#### Define a temporary value to save the result
```python
result = ""
```
#### Input each index of string into expend function
```python
sub1 = expand(i , i)
```

#### Check if length of returned value is larger than length of result. Save its value to result, else do nothing.
```python
if(len(sub1) > len(result)):
    result = sub1
```

#### Do the same step with index and next index.
```python
sub2 = expand (i, i+1)
if(len(sub2) > len(result)):
    result = sub2
```

#### At the end of loop. Return value of result
```python
return result
```


## Example 1
String s = "zaday", length of s is ``5``. Expected result is ``ada``.

At LOOP 1:
```python
    result  = ""
    i       = 0
    # Call function expand with l = 0, r = 0.
        (l = 0) >= 0 and (r = 0) < (len(s) = 5) and (s[l] = z) == (s[r] = z) => TRUE
            => l = 0 -1 = -1, r = 0 + 1 = 1.
        (l = -1) >= 0 => FALSE
        return s[-1+1;1] = "z"
    sub1 = "z", len(sub1)=1 > len(result)=0 => TRUE
        => result = sub1 = "z"
    # Call function expand with l = 0, r = 0 + 1 = 1.
    (l = 0) >= 0 and (r = 1) < (len(s) = 5) and (s[l] = z) != (s[r] = a) => FALSE
        return s[0+1;1] = "a"
    sub2 = "a", len(sub2)=1 > len(result)=1 => FALSE
```  
At LOOP 2 :
``` python
    result  = "z"
    i       = 1
    # Call function expand with l = 1, r = 1.
        (l = 1) >= 0 and (r = 1) < (len(s) = 5) and (s[l] = a) == (s[r] = a) => TRUE
            => l = 1 -1 = 0, r = 1 + 1 = 2.
        (l = 0) >= 0 and (r = 2) < (len(s) = 5) and (s[l] = z) == (s[r] = d) => FALSE
        return s[0+1;2] = "a"
    sub1 = "a", len(sub1)=1 > len(result)=1 => FALSE
    # Call function expand with l = 1, r = 1 + 1 = 2.
    (l = 1) >= 0 and (r = 2) < (len(s) = 5) and (s[l] = a) != (s[r] = d) => FALSE
        return s[1+1;2] = "d"
    sub2 = "d", len(sub2)=1 > len(result)=1 => FALSE
``` 
At LOOP 3 :
``` python
    result  = "z"
    i       = 2
    # Call function expand with l = 2, r = 2.
        (l = 2) >= 0 and (r = 2) < (len(s) = 5) and (s[l] = d) == (s[r] = d) => TRUE
            => l = 2 -1 = 1, r = 2 + 1 = 3.
        (l = 1) >= 0 and (r = 3) < (len(s) = 5) and (s[l] = a) == (s[r] = a) => TRUE
            => l = 1 -1 = 0, r = 3 + 1 = 4.
        (l = 0) >= 0 and (r = 4) < (len(s) = 5) and (s[l] = z) == (s[r] = y) => FALSE
        return s[0+1;4] = "ada"
    sub1 = "ada", len(sub1)=3 > len(result)=1 => TRUE
        => result = sub1 = "ada"
    # Call function expand with l = 2, r = 2 + 1 = 3.
    (l = 2) >= 0 and (r = 3) < (len(s) = 5) and (s[l] = d) != (s[r] = a) => FALSE
        return s[2+1;3] = "d"
    sub2 = "d", len(sub2)=1 > len(result)=3 => FALSE
``` 
At LOOP 4 :
``` python
    result  = "ada"
    i       = 3
    # Call function expand with l = 3, r = 3.
        (l = 3) >= 0 and (r = 3) < (len(s) = 5) and (s[l] = a) == (s[r] = a) => TRUE
            => l = 3 -1 = 2, r = 3 + 1 = 4.
        (l = 2) >= 0 and (r = 4) < (len(s) = 5) and (s[l] = d) == (s[r] = y) => FALSE
        return s[2+1;4] = "ay"
    sub1 = "ay", len(sub1)=2 > len(result)=3 => FALSE
    # Call function expand with l = 3, r = 3 + 1 = 4.
    (l = 3) >= 0 and (r = 4) < (len(s) = 5) and (s[l] = a) != (s[r] = y) => FALSE
        return s[3+1;4] = "y"
    sub2 = "y", len(sub2)=1 > len(result)=3 => FALSE
``` 
At LOOP 5 (END):
``` python
    result  = "ada"
    i       = 4
    # Call function expand with l = 4, r = 4.
        (l = 4) >= 0 and (r = 4) < (len(s) = 5) and (s[l] = y) == (s[r] = y) => TRUE
            => l = 4 -1 = 3, r = 4 + 1 = 5.
        (l = 3) >= 0 and (r = 4) < (len(s) = 5) => FALSE
        return s[3+1;5] = "yz"
    sub1 = "yz", len(sub1)=2 > len(result)=3 => FALSE
    # Call function expand with l = 4, r = 4 + 1 = 5.
    (l = 3) >= 0 and (r = 5) < (len(s) = 5) => FALSE
        return s[4+1;5] = "z"
    sub2 = "z", len(sub2)=1 > len(result)=3 => FALSE
Return result  = "ada".
```
## Example 2
String s = "ncbbcm", length of s is ``6``. Expected result is ``cbbc``.

At LOOP 1:
```python
    result  = ""
    i       = 0
    # Call function expand with l = 0, r = 0.
        (l = 0) >= 0 and (r = 0) < (len(s) = 6) and (s[l] = n) == (s[r] = n) => TRUE
            => l = 0 -1 = -1, r = 0 + 1 = 1.
        (l = -1) >= 0 => FALSE
        return s[-1+1;1] = "n"
    sub1 = "n", len(sub1)=1 > len(result)=0 => TRUE
        => result = sub1 = "n"
    # Call function expand with l = 0, r = 0 + 1 = 1.
    (l = 0) >= 0 and (r = 1) < (len(s) = 6) and (s[l] = n) != (s[r] = c) => FALSE
        return s[0+1;1] = "c"
    sub2 = "c", len(sub2)=1 > len(result)=1 => FALSE
```  
At LOOP 2 :
``` python
    result  = "n"
    i       = 1
    # Call function expand with l = 1, r = 1.
        (l = 1) >= 0 and (r = 1) < (len(s) = 6) and (s[l] = c) == (s[r] = c) => TRUE
            => l = 1 -1 = 0, r = 1 + 1 = 2.
        (l = 0) >= 0 and (r = 2) < (len(s) = 6) and (s[l] = n) == (s[r] = b) => FALSE
        return s[0+1;2] = "c"
    sub1 = "c", len(sub1)=1 > len(result)=1 => FALSE
    # Call function expand with l = 1, r = 1 + 1 = 2.
    (l = 1) >= 0 and (r = 2) < (len(s) = 6) and (s[l] = c) != (s[r] = b) => FALSE
        return s[1+1;2] = "b"
    sub2 = "b", len(sub2)=1 > len(result)=1 => FALSE
``` 
At LOOP 3 :
``` python
    result  = "n"
    i       = 2
    # Call function expand with l = 2, r = 2.
        (l = 2) >= 0 and (r = 2) < (len(s) = 6) and (s[l] = b) == (s[r] = b) => TRUE
            => l = 2 -1 = 1, r = 2 + 1 = 3.
        (l = 1) >= 0 and (r = 3) < (len(s) = 6) and (s[l] = c) == (s[r] = b) => FALSE
        return s[1+1;3] = "b"
    sub1 = "b", len(sub1)=1 > len(result)=1 => FALSE
    # Call function expand with l = 2, r = 2 + 1 = 3.
    (l = 2) >= 0 and (r = 3) < (len(s) = 6) and (s[l] = b) == (s[r] = b) => TRUE
        => l = 2 -1 = 1, r = 3 + 1 = 4.
    (l = 1) >= 0 and (r = 4) < (len(s) = 6) and (s[l] = c) == (s[r] = c) => TRUE
        => l = 1 -1 = 0, r = 4 + 1 = 5.
    (l = 1) >= 0 and (r = 5) < (len(s) = 6) and (s[l] = n) != (s[r] = m) => FALSE
        return s[0+1;5] = "cbbc"
    sub2 = "cbbc", len(sub2)=4 > len(result)=1 => TRUE
        result =  sub2 = "cbbc"
``` 
At LOOP 4 :
``` python
    result  = "cbbc"
    i       = 3
    # Call function expand with l = 3, r = 3.
        (l = 3) >= 0 and (r = 3) < (len(s) = 6) and (s[l] = b) == (s[r] = b) => TRUE
            => l = 3 -1 = 2, r = 3 + 1 = 4.
        (l = 2) >= 0 and (r = 4) < (len(s) = 6) and (s[l] = b) != (s[r] = c) => FALSE
        return s[2+1;4] = "b"
    sub1 = "b", len(sub1)=1 > len(result)=4 => FALSE
    # Call function expand with l = 3, r = 3 + 1 = 4.
    (l = 3) >= 0 and (r = 4) < (len(s) = 6) and (s[l] = b) != (s[r] = c) => FALSE
        return s[3+1;4] = "c"
    sub2 = "c", len(sub2)=1 > len(result)=4 => FALSE
``` 
At LOOP 5 :
``` python
    result  = "cbbc"
    i       = 4
    # Call function expand with l = 4, r = 4.
        (l = 4) >= 0 and (r = 4) < (len(s) = 6) and (s[l] = c) == (s[r] = c) => TRUE
            => l = 4 -1 = 3, r = 4 + 1 = 5.
        (l = 3) >= 0 and (r = 5) < (len(s) = 6) and (s[l] = b) != (s[r] = m) => FALSE
        return s[3+1;5] = "c"
    sub1 = "c", len(sub1)=1 > len(result)=4 => FALSE
    # Call function expand with l = 4, r = 4 + 1 = 5.
    (l = 4) >= 0 and (r = 5) < (len(s) = 6) and (s[l] = c) != (s[r] = m) => FALSE
        return s[4+1;5] = "m"
    sub2 = "m", len(sub2)=1 > len(result)=4 => FALSE
``` 
At LOOP 6 (END) :
``` python
    result  = "cbbc"
    i       = 5
    # Call function expand with l = 5, r = 5.
        (l = 5) >= 0 and (r = 5) < (len(s) = 6) and (s[l] = m) == (s[r] = m) => TRUE
            => l = 5 -1 = 4, r = 5 + 1 = 6.
        (l = 4) >= 0 and (r = 6) < (len(s) = 6) => FALSE
        return s[4+1;6] = "m"
    sub1 = "m", len(sub1)=1 > len(result)=4 => FALSE
    # Call function expand with l = 5, r = 5 + 1 = 6.
    (l = 5) >= 0 and (r = 6) < (len(s) = 6) => FALSE
        return s[5+1;6] = "n"
    sub2 = "n", len(sub2)=1 > len(result)=4 => FALSE
Return result = "cbbc"
``` 
## Full code [here](./LongestPalindromicSubstring.py)