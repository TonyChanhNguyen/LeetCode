## Description
#### URL: [Reverse integer](https://leetcode.com/problems/reverse-integer/)

Given a signed 32-bit integer ``x``, return ``x`` with its digits reversed. If reversing ``x`` causes the value to go outside the signed 32-bit integer range ``[-231, 231 - 1]``, then return ``0``.

##### Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
Example 1:
``````
Input: x = 123
Output: 321
``````
Example 2:
``````
Input: x = -123
Output: -321
``````
Example 3:
``````
Input: x = 120
Output: 21
``````

#### Constraints:

+ -2<sup>31</sup> <= x <= 2<sup>31</sup> - 1

## Idea
Let's exmaple we have a number `num = 1234` and you want to reverse it to `result = 4321`.
+ At you see, we can move the end of `nums` to the begin of `result`, the `third` to `second`.
+ If you split each characters of number `num` into `1`, `2`, `3` and `4` and multiple them with `10`, `10`, `100`, and `1000` mean 10<sup>0</sup>, 10<sup>1</sup>, 10<sup>2</sup> and 10<sup>3</sup>. Then summarizing them, it will be same the `result`?
```
4*1000 + 3*100 + 2*10 + 1*1 = 4321 == result
```
+ How we can write this calculation as code?
 
```python
# Count length of number
length = len(str(num)) # Can not use len() for 'int' type, convert it to 'str' to use
# Define the temporary variable
index   = 0
result  = 0
num1    = 0
num2    = num
for i in range (length):
    # Split the latest character of number
    num1 = num2 % 10 
    # Save the remaining after splitting
    num2 = num2 // 10 
    # Calculate the exponent
    index = length - i -1
    result += num1* 10**index
```

#### Avoid input number is 0:
```python
if(x == 0):
    return 0
```

#### Avoid input number is less than 0:
```python
flag_x = 1
elif( x > 0):
    flag_x = 1
else:
    flag_x = -1
# if number is less than 0, multiple it with `-1`. 
x = flag_x*x
# After calculating `result`, multiple `result` with `-1.
result = result*flag_x
```

#### Avoid out of range
```python
# input number
elif(MIN_INT > x or x > MAX_INT):
    return 0
# Return result
if(MIN_INT > result or result > MAX_INT):
    return 0
else:
    return result    
```
## Example 1
We have a number `num = 123456`, expected `result = 654321`.
```python
if num > 0 => True
    flag_x = 1
num = flag_x*num = 1*123456 = 123456 # Nothing change
length = len(str(num))      = 6
result                      = 0
index                       = 0
num1                        = 0
num2                        = 123456
```
At LOOP 1/6
```python
i = 0
num1  = num2 % 10  = 123456 % 10  = 6
num2  = num2 // 10 = 123456 // 10 = 12345
index = length - i -1 = 6 - 0 - 1 = 5
result += 6* 10**5 = 0 + 6*100000 = 600000     
```
At LOOP 2/6
```python
i = 1
num1  = num2 % 10  = 12345 % 10  = 5
num2  = num2 // 10 = 12345 // 10 = 1234
index = length - i -1 = 6 - 1 - 1 = 4
result += 5* 10**4 = 600000   + 5*10000 = 650000   
```
At LOOP 3/6
```python
i = 2
num1  = num2 % 10  = 1234 % 10  = 4
num2  = num2 // 10 = 1234 // 10 = 123
index = length - i -1 = 6 - 2 - 1 = 3
result += 4* 10**3 = 650000   + 4*1000 = 654000   
```
At LOOP 4/6
```python
i = 3
num1  = num2 % 10  = 123 % 10  = 3
num2  = num2 // 10 = 123 // 10 = 12
index = length - i -1 = 6 - 3 - 1 = 2
result += 3* 10**2 = 654000   + 3*100 = 654300   
```
At LOOP 5/6
```python
i = 4
num1  = num2 % 10  = 12 % 10  = 2
num2  = num2 // 10 = 12 // 10 = 1
index = length - i -1 = 6 - 4 - 1 = 1
result += 2* 10**1 = 654300   + 2*10 = 654320   
```
At LOOP 6/6 (END)
```python
i = 5
num1  = num2 % 10  = 1 % 10  = 1
num2  = num2 // 10 = 1 // 10 = 0
index = length - i -1 = 6 - 5 - 1 = 0
result += 1* 10**0 = 654320   + 1*0 = 654321   
```
#### Multiple result with flag_x
```python
result = result*flag_x = 654321 * 1 = 654321
```

#### Check the condition to avoid the result is out of range
```python
if(MIN_INT > result or result > MAX_INT):   => False
else:                                       => True
    return result (=654321)
```

## Example 2
We have a number `num = -123456`, expected `result = -654321`.
```python
if num < 0 => True
    flag_x = -1
num = flag_x*num = -1*-123456 = 123456
length = len(str(num))      = 6
result                      = 0
index                       = 0
num1                        = 0
num2                        = 123456
```
At LOOP 1/6
```python
i = 0
num1  = num2 % 10  = 123456 % 10  = 6
num2  = num2 // 10 = 123456 // 10 = 12345
index = length - i -1 = 6 - 0 - 1 = 5
result += 6* 10**5 = 0 + 6*100000 = 600000     
```
At LOOP 2/6
```python
i = 1
num1  = num2 % 10  = 12345 % 10  = 5
num2  = num2 // 10 = 12345 // 10 = 1234
index = length - i -1 = 6 - 1 - 1 = 4
result += 5* 10**4 = 600000   + 5*10000 = 650000   
```
At LOOP 3/6
```python
i = 2
num1  = num2 % 10  = 1234 % 10  = 4
num2  = num2 // 10 = 1234 // 10 = 123
index = length - i -1 = 6 - 2 - 1 = 3
result += 4* 10**3 = 650000   + 4*1000 = 654000   
```
At LOOP 4/6
```python
i = 3
num1  = num2 % 10  = 123 % 10  = 3
num2  = num2 // 10 = 123 // 10 = 12
index = length - i -1 = 6 - 3 - 1 = 2
result += 3* 10**2 = 654000   + 3*100 = 654300   
```
At LOOP 5/6
```python
i = 4
num1  = num2 % 10  = 12 % 10  = 2
num2  = num2 // 10 = 12 // 10 = 1
index = length - i -1 = 6 - 4 - 1 = 1
result += 2* 10**1 = 654300   + 2*10 = 654320   
```
At LOOP 6/6 (END)
```python
i = 5
num1  = num2 % 10  = 1 % 10  = 1
num2  = num2 // 10 = 1 // 10 = 0
index = length - i -1 = 6 - 5 - 1 = 0
result += 1* 10**0 = 654320   + 1*0 = 654321   
```
#### Multiple result with flag_x
```python
result = result*flag_x = 654321 * -1 = -654321
```

#### Check the condition to avoid the result is out of range
```python
if(MIN_INT > result or result > MAX_INT):   => False
else:                                       => True
    return result (=-654321)
```

## Full code [here](./ReverseInteger.py)