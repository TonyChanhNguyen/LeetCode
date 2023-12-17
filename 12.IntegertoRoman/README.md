## Description
#### URL:

Roman numerals are represented by seven different symbols: ``I``, ``V``, ``X``, ``L``, ``C``, ``D`` and ``M``.
```
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```
For example, ``2`` is written as ``II`` in Roman numeral, just two one's added together. ``12`` is written as ``XII``, which is simply ``X + II``. The number ``27`` is written as ``XXVII``, which is ``XX + V + II``.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not ``IIII``. Instead, the number four is written as ``IV``. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as ``IX``. There are six instances where subtraction is used:

+ ``I`` can be placed before ``V`` (5) and ``X`` (10) to make 4 and 9. 
+ ``X`` can be placed before ``L`` (50) and ``C`` (100) to make 40 and 90. 
+ ``C`` can be placed before ``D`` (500) and ``M`` (1000) to make 400 and 900.
+ Given an integer, convert it to a roman numeral.

#### Example 1:
```
Input: num = 3
Output: "III"
Explanation: 3 is represented as 3 ones.
```

#### Example 2:
```
Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
```

#### Example 3:
```
Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
```
#### Constraints
+ ```1<= num <= 3999```

## Idea
See the Roman string of each number from 1 to 10, you can divide 4 numbers that will make symbol change is 1 (I), 4 (form 3(III) to IV), 5 (from 4(IV) to V), 9 (from 8 (VIII) to IX) and 10 (from IX to X).

#### So we can set a dictionary to store these special case.
```python
num_map = {
    1: "I",
    5: "V",    4: "IV",
    10: "X",   9: "IX",
    50: "L",   40: "XL",
    100: "C",  90: "XC",
    500: "D",  400: "CD",
    1000: "M", 900: "CM",
}
```
#### Initialize a variable to store the result.
```python
# Result Variable
r = ''
```

#### Set a loop of list to compare with ``num`` and calculate the result.
```python
for n in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
    # If n in list then add the roman value to result variable
    while n <= num:
        r += num_map[n]
        num-=n
return r
```

#### Example 
We have ``num = 2897``, expected ``result = MMDCCCXCVII ``.

At LOOP 1
```python
num_map = {
    1: "I",
    5: "V",    4: "IV",
    10: "X",   9: "IX",
    50: "L",   40: "XL",
    100: "C",  90: "XC",
    500: "D",  400: "CD",
    1000: "M", 900: "CM",
        }
num = 2897
n = 1000
r = ''
n <= num (1000 <= 2897): => True
    r = '' + num_map[1000] = 'M' 
    num = num - n = 2897 - 1000 = 1897
n <= num (1000 <= 1897): => True
    r = 'M' + num_map[1000] = 'MM' 
    num = num - n = 1897 - 1000 = 897
n <= num (1000 <= 897): => False
```
At LOOP 2
```python
num_map = {
    1: "I",
    5: "V",    4: "IV",
    10: "X",   9: "IX",
    50: "L",   40: "XL",
    100: "C",  90: "XC",
    500: "D",  400: "CD",
    1000: "M", 900: "CM",
        }
num = 897
n = 900
r = 'MM'
n <= num (900 <= 897): => False
```
At LOOP 3
```python
num_map = {
    1: "I",
    5: "V",    4: "IV",
    10: "X",   9: "IX",
    50: "L",   40: "XL",
    100: "C",  90: "XC",
    500: "D",  400: "CD",
    1000: "M", 900: "CM",
        }
num = 897
n = 500
r = 'MM'
n <= num (500 <= 897): => True
    r = 'MM' + num_map[500] = 'MMD' 
    num = num - n = 897 - 500 = 397
n <= num (500 <= 397): => False
```
At LOOP 4
```python
num_map = {
    1: "I",
    5: "V",    4: "IV",
    10: "X",   9: "IX",
    50: "L",   40: "XL",
    100: "C",  90: "XC",
    500: "D",  400: "CD",
    1000: "M", 900: "CM",
        }
num = 397
n = 400
r = 'MMD'
n <= num (400 <= 397): => False
```
At LOOP 5
```python
num_map = {
    1: "I",
    5: "V",    4: "IV",
    10: "X",   9: "IX",
    50: "L",   40: "XL",
    100: "C",  90: "XC",
    500: "D",  400: "CD",
    1000: "M", 900: "CM",
        }
num = 397
n = 100
r = 'MMD'
n <= num (100 <= 397): => True
    r = 'MMD' + num_map[100] = 'MMDC' 
    num = num - n = 397 - 100 = 297
n <= num (100 <= 297): => True
    r = 'MMDC' + num_map[100] = 'MMDCC' 
    num = num - n = 297 - 100 = 197
n <= num (100 <= 197): => True
    r = 'MMDCC' + num_map[100] = 'MMDCCC'
    num = num - n = 197 - 100 = 97
n <= num (100 <= 97): => False
```
At LOOP 6
```python
num_map = {
    1: "I",
    5: "V",    4: "IV",
    10: "X",   9: "IX",
    50: "L",   40: "XL",
    100: "C",  90: "XC",
    500: "D",  400: "CD",
    1000: "M", 900: "CM",
        }
num = 97
n = 90
r = 'MMDCCC'
n <= num (90 <= 97): => True
    r = 'MMDCCC' + num_map[90] = 'MMDCCCXC' 
    num = num - n = 97 - 90 = 7
n <= num (90 <= 7): => False  
```
At LOOP 6
```python
num_map = {
    1: "I",
    5: "V",    4: "IV",
    10: "X",   9: "IX",
    50: "L",   40: "XL",
    100: "C",  90: "XC",
    500: "D",  400: "CD",
    1000: "M", 900: "CM",
        }
num = 7
n = 50
r = 'MMDCCCXC'
n <= num (50 <= 7): => False
```
At LOOP 7
```python
num_map = {
    1: "I",
    5: "V",    4: "IV",
    10: "X",   9: "IX",
    50: "L",   40: "XL",
    100: "C",  90: "XC",
    500: "D",  400: "CD",
    1000: "M", 900: "CM",
        }
num = 7
n = 10
r = 'MMDCCCXC'
n <= num (10 <= 7): => False
```
At LOOP 8
```python
num_map = {
    1: "I",
    5: "V",    4: "IV",
    10: "X",   9: "IX",
    50: "L",   40: "XL",
    100: "C",  90: "XC",
    500: "D",  400: "CD",
    1000: "M", 900: "CM",
        }
num = 7
n = 9
r = 'MMDCCCXC'
n <= num (9 <= 7): => False
```
At LOOP 9
```python
num_map = {
    1: "I",
    5: "V",    4: "IV",
    10: "X",   9: "IX",
    50: "L",   40: "XL",
    100: "C",  90: "XC",
    500: "D",  400: "CD",
    1000: "M", 900: "CM",
        }
num = 7
n = 5
r = 'MMDCCCXC'
n <= num (5 <= 7): => True
    r = 'MMDCCCXC' + num_map[5] = 'MMDCCCXCV' 
    num = num - n = 7 - 5 = 2
```
At LOOP 10
```python
num_map = {
    1: "I",
    5: "V",    4: "IV",
    10: "X",   9: "IX",
    50: "L",   40: "XL",
    100: "C",  90: "XC",
    500: "D",  400: "CD",
    1000: "M", 900: "CM",
        }
num = 2
n = 4
r = 'MMDCCCXCV'
n <= num (4 <= 2): => False
```
At LOOP 9
```python
num_map = {
    1: "I",
    5: "V",    4: "IV",
    10: "X",   9: "IX",
    50: "L",   40: "XL",
    100: "C",  90: "XC",
    500: "D",  400: "CD",
    1000: "M", 900: "CM",
        }
num = 2
n = 1
r = 'MMDCCCXCV'
n <= num (1 <= 2): => True
    r = 'MMDCCCXCV' + num_map[1] = 'MMDCCCXCVI' 
    num = num - n = 2 - 1 = 1
n <= num (1 <= 1): => True
    r = 'MMDCCCXCVI' + num_map[1] = 'MMDCCCXCVII' 
    num = num - n = 1 - 1 = 0
n <= num (1 <= 0): => False
return r = 'MMDCCCXCVII' 
```