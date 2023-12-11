## Description
#### URL: [Palindrome Number](https://leetcode.com/problems/palindrome-number)

Given an integer ``x``, return ``true`` if ``x`` is a 
palindrome
, and ``false`` otherwise.

 

Example 1:
```
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
```
Example 2:
```
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
```
Example 3:
```
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 ```

## Constraints:

-2<sup>31</sup> <= x <= 2<sup>31</sup> - 1

## Idea 1
#### Convert number to string and check it with its reverse.
```
s = str(x)
return s[:len(s)] == s[::-1]
```
## Idea 2 (Without converting the integer to a string)
#### Set a condition if number is negative, return ``False``.
```python
if(x < 0):
    return False
```
#### Else, set a loop to split each element of number and save it to reverse number.
```python
else:
    temp_x = x
    reverse_x = 0
    while temp_x != 0:
        reverse_x = reverse_x*10 + temp_x%10
        temp_x = temp_x //10
```
#### Then, compare the number with its reverse number and return the result.
```python
return reverse_x == x
```
## Full code idea 1 [here](./PalindromeNumber_1.py)
## Full code idea 2 (Without converting the integer to a string) [here](./PalindromeNumber_2.py)