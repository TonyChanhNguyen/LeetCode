## Description
#### URL: [String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/)

Implement the ``myAtoi(string s)`` function, which converts a string to a 32-bit signed integer (similar to C/C++'s ``atoi`` function).

The algorithm for ``myAtoi(string s)`` is as follows:
1. Read in and ignore any leading whitespace.
2. Check if the next character (if not already at the end of the string) is ``'-'`` or ``'+'``. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
3. Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
4. Convert these digits into an integer (i.e. ``"123" -> 123``, ``"0032" -> 32``). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
5. If the integer is out of the 32-bit signed integer range ``[-231, 231 - 1]``, then clamp the integer so that it remains in the range. Specifically, integers less than -2<sup>31</sup>` should be clamped to -2<sup>31</sup>, and integers greater than 2<sup>31</sup> - 1 should be clamped to 2<sup>31</sup> - 1.
6. Return the integer as the final result.
Note:

+ Only the space character `' '`` is considered a whitespace character.
+ Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
Example 1:
``````
Input: s = "42"
Output: 42
Explanation: The underlined characters are what is read in, the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
The parsed integer is 42.
Since 42 is in the range [-231, 231 - 1], the final result is 42.
``````
Example 2:
``````
Input: s = "   -42"
Output: -42
Explanation:
Step 1: "   -42" (leading whitespace is read and ignored)
            ^
Step 2: "   -42" ('-' is read, so the result should be negative)
             ^
Step 3: "   -42" ("42" is read in)
               ^
The parsed integer is -42.
Since -42 is in the range [-231, 231 - 1], the final result is -42.
``````
Example 3:
``````
Input: s = "4193 with words"
Output: 4193
Explanation:
Step 1: "4193 with words" (no characters read because there is no leading whitespace)
         ^
Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "4193 with words" ("4193" is read in; reading stops because the next character is a non-digit)
             ^
The parsed integer is 4193.
Since 4193 is in the range [-231, 231 - 1], the final result is 4193.
``````

### Constraints:

+ ``0 <= s.length <= 200``
+ ``s`` consists of English letters (lower-case and upper-case), digits ``(0-9)``, ``' '``, ``'+'``, ``'-``, and ``'.'``.

## Idea

#### Define a function to avoid out of range.
```python
MAX_INT = 2 ** 31 - 1 # 2,147,483,647
MIN_INT = -2 ** 31    #-2,147,483,648
def checkOutOfRange(num : int) -> int:
    if (num > MAX_INT):
        return MAX_INT
    elif (num < MIN_INT):
        return MIN_INT
    else:
        return num
```

#### Define a list of number.
```python
list_accept = "0123456789"  
```

#### Define temporary variables.
```python
isNumberStarted = False # Identify when starting receive first number
isPositive  = True  # Check the expected result is positive or negative
num = 0 # Store the result
```

#### Run a loop to get each character in string.
```python
for i in range(len(s)):
```

#### Set first condition, if character is number. Calculate num and set flag isNumberStarted to ``True``.
```python
if s[i] in list_accept:
    num = num*10 + int(s[i])
    isNumberStarted = True
```
#### Set second condtion, if character is not number and previous characters is number. Break the loop.
```
elif(isNumberStarted):
            break
```

#### Else case mean previous characters is NOT number. Check if character is ``+`` or ``-`` to set flag ``isPositive`` and ``isNumberStarted``.
```python
else:
    if s[i] == "+":
        isPositive = True
        isNumberStarted = True
    elif s[i] == "-":
        isPositive = False
        isNumberStarted  = True
```

#### If character is space, ignore and continue the loop.
```python
    elif s[i] == " ":
        continue
```
#### Else case mean none of characters are number.
```python
else:
    break  
```
#### At the end of loop, check and return result by calling function ``checkOutOfRange``.
```python
return checkOutOfRange(num if isPositive else num*-1)
```
## Example 1
We have string ``s = "-42"``, expected result ``num = -42``
At LOOP 1
```python
s[0]            = "-"
isNumberStarted = False
isPositive      = True
num             = 0
if s[i] in list_accept: => False
elif(isNumberStarted):  => False
else:                   => True
    if s[i] == "+":     => False
    elif s[i] == "-":   => True
        isPositive          = False
        isNumberStarted     = True
num = 0 

```
At LOOP 2
```python
s[i]            = "4"
isNumberStarted = True
isPositive      = False
num             = 0
if s[i] in list_accept: => True
    num = num*10 + int(s[i])    = 0*10 + int("4") = 4
num = 4
```
At LOOP 3 (END)
```python
s[i]            = "2"
isNumberStarted = True
isPositive      = False
num             = 0
if s[i] in list_accept: => True
    num = num*10 + int(s[i])    = 4*10 + int("2") = 42
return checkOutOfRange(num if isPositive else num*-1) => return checkOutOfRange(num*-1)
    if (num > MAX_INT):     => False
    elif (num < MIN_INT):   => False
    else:                   => True
    return num = - 42
```

## Example 2
We have string ``s = " 123c456 HelloWorld"``, expected result ``num = 123``
At LOOP 1:
```python
s[i]            = " "
isNumberStarted = False
isPositive      = True
num             = 0
if s[i] in list_accept: => False
elif(isNumberStarted):  => False
else:                   => True
    if s[i] == "+":     => False
    elif s[i] == "-":   => False
    elif s[i] == " ":   => True
        continue
num  = 0
```
At LOOP 2:
```python
s[i]            = "1"
isNumberStarted = False
isPositive      = True
num             = 0
if s[i] in list_accept: => True
    num = num*10 + int(s[i]) = 0*10 + int(1)    = 1
    isNumberStarted                             = True
        
```
At LOOP 3:
```python
s[i]            = "2"
isNumberStarted = True
isPositive      = True
num             = 1
if s[i] in list_accept: => True
    num = num*10 + int(s[i]) = 1*10 + int(2)    = 12
    isNumberStarted                             = True
```
At LOOP 4:
```python
s[i]            = "3"
isNumberStarted = True
isPositive      = True
num             = 12
if s[i] in list_accept: => True
    num = num*10 + int(s[i]) = 12*10 + int(3)    = 123
    isNumberStarted                             = True
```
At LOOP 5:
```python
s[i]            = "c"
isNumberStarted = True
isPositive      = True
num             = 123
if s[i] in list_accept: => False
elif(isNumberStarted):  => True
    break
return checkOutOfRange(num if isPositive else num*-1) => return checkOutOfRange(num)
    if (num > MAX_INT):     => False
    elif (num < MIN_INT):   => False
    else:                   => True
        return num = 123
```

## Full code [here](./StringtoInteger.py)