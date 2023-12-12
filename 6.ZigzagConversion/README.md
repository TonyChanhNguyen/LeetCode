## Description
#### URL: [Zigzag Conversion](https://leetcode.com/problems/zigzag-conversion)

The string ``"PAYPALISHIRING"`` is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
```
P   A   H   N
A P L S I I G
Y   I   R
```
And then read line by line: ``"PAHNAPLSIIGYIR"``
Write the code that will take a string and make this conversion given a number of rows:
```python
string convert(string s, int numRows);
```

#### Example 1:
``````
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
``````
#### Example 2:
``````
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
``````
#### Example 3:
``````
Input: s = "A", numRows = 1
Output: "A"
``````

#### Constraints:

+ ``1 <= s.length <= 1000``
+ ``s`` consists of English letters (lower-case and upper-case), ``','`` and ``'.'``.
+ ``1 <= numRows <= 1000``

## Idea
Let's example we have a string ``s = "HelloWorld"`` with ``numRows = 3``.
The Zigzag string will be:
```
H     o     l
e  l  W  r  d
l     o
```
Imaging it is a 2D array, it should be:
```
[
  0  []H     o     l
  1  []e  l  W  r  d
  2  []l     o
]
```
Now when look at 2D array, we can map index 2D array into string s like:
```
H   e   l   l   o   W   o   r   l   d
0   1   2   1   0   1   2   1   0   1
```
The index of 2D array for each characters of string S will be increased from 0 to 2 with step is 1 and decreased with step is -1. The range from 0 to 2 can be calculated by ``numRows - 1``.

Next, let's example again with string ``s = "a"`` with ``numRows = 1``.
The Zigzag string will be only:
```
a
```
So if the string is a single character, the returned Zigzag string should be itself.

Final, let's example again with string ``s = "abcs"`` with ``length = 4`` and ``numRows = 5``, larger than its length.
The Zigzag string will be:
```
a
b
c
s
```
So if the length of string is less than or equal numRows, the returned Zigzag string should be itself, too.
#### Set a condition to check if the string is only one character or length of it less than or equal to numRows. Return itself.
```python
if numRows == 1 or numRows >= len(s):
            return s
```

#### Define an empty 2D array to store the temporary result. 
```python
rows = [[]for row in range(numRows)]
```
#### Define temporary variables index and step.
```python
index = 0
step = 1
```

#### Set a loop run get each characters in string:
```python
for char in s:
```

#### Append it into rows at index.
```python
rows[index].append(char)
```

#### Set a condition to check if index at the begin of array, set step is 1.
``````python
if index == 0:
    step = 1
``````
#### Else if index at the end of array, set step is -1.
``````python
elif index == numRows - 1:
    step = -1
``````
#### Calculate index by step.
```python
index += step # If step is 1 => Increase index. If step is -1 => Decrease index.
```

#### At the end of loop, the result is saved to 2D array. Now, we will perform join the result of each row.
```python
for i in range(numRows):
    rows[i] = ''.join(rows[i])
```

#### After join characters of each rows, we will join the result of all rows into a string. That is our expected resulted.
``````python
return ''.join(rows)
``````

## Example
We have a string ``s = "FirstCloudJourney"`` with ``numRows = 4``. Expected Zigzag string is ``"FluiCoorrtuJnysde"``

At LOOP 1:
```python
2D array rows
[
    []              # index 0
    []              # index 1
    []              # index 2
    []              # index 3
]
index   = 0
step    = 1
char    = "F"
rows[0].append("F")
If index == 0 => TRUE
    step = 1
index += step = 0 + 1 = 1
'''
2D array rows
[
    ["F"]           # index 0
    []              # index 1
    []              # index 2
    []              # index 3
]
'''
```
At LOOP 2:
```python
2D array rows
[
    ["F"]           # index 0
    []              # index 1
    []              # index 2
    []              # index 3
]
index   = 1
step    = 1
char    = "i"
rows[1].append("i")
If index == 0 => FALSE
ELSE if index(=1) == numRows - 1(4-1=3) => FALSE
value of step no change, keep 1.
index += step = 1 + 1 = 2
2D array rows
[
    ["F"]           # index 0
    ["i"]           # index 1
    []              # index 2
    []              # index 3
]
```
At LOOP 3:
```python
2D array rows
[
    ["F"]           # index 0
    ["i"]           # index 1
    []              # index 2
    []              # index 3
]
index   = 2
step    = 1
char    = "r"
rows[2].append("r")
If index == 0 => FALSE
ELSE if index(=2) == numRows - 1(4-1=3) => FALSE
value of step no change, keep 1.
index += step = 2 + 1 = 3
2D array rows
[
    ["F"]           # index 0
    ["i"]           # index 1
    ["r"]           # index 2
    []              # index 3
]
```
At LOOP 4:
```python
2D array rows
[
    ["F"]           # index 0
    ["i"]           # index 1
    ["r"]           # index 2
    []              # index 3
]
index   = 3
step    = 1
char    = "s"
rows[3].append("s")
If index == 0 => FALSE
ELSE if index(=3) == numRows - 1(4-1=3) => TRUE
    step = -1
index += step = 3 + -1 = 2
2D array rows
[
    ["F"]           # index 0
    ["i"]           # index 1
    ["r"]           # index 2
    ["s"]           # index 3
]
```
At LOOP 5:
```python
2D array rows
[
    ["F"]           # index 0
    ["i"]           # index 1
    ["r"]           # index 2
    ["s"]           # index 3
]
index   = 2
step    = -1
char    = "t"
rows[2].append("t")
If index == 0 => FALSE
ELSE if index(=2) == numRows - 1(4-1=3) => FALSE
value of step no change, keep -1.
index += step = 2 + -1 = 1
2D array rows
[
    ["F"]           # index 0
    ["i"]           # index 1
    ["r","t"]       # index 2
    ["s"]           # index 3
]
```
At LOOP 6:
```python
2D array rows
[
    ["F"]           # index 0
    ["i"]           # index 1
    ["r","t"]       # index 2
    ["s"]           # index 3
]
index   = 1
step    = -1
char    = "C"
rows[1].append("C")
If index == 0 => FALSE
ELSE if index(=1) == numRows - 1(4-1=3) => FALSE
value of step no change, keep -1.
index += step = 1 + -1 = 0
2D array rows
[
    ["F"]               # index 0
    ["i",   "C"]        # index 1
    ["r","t"]           # index 2
    ["s"]               # index 3
]
```
At LOOP 7:
```python
2D array rows
[
    ["F"]               # index 0
    ["i",   "C"]        # index 1
    ["r","t"]           # index 2
    ["s"]               # index 3
]
index   = 0
step    = -1
char    = "l"
rows[0].append("l")
If index == 0 => TRUE
    step = 1
index += step = 0 + 1 = 1
2D array rows
[
    ["F",       "l"]        # index 0
    ["i",   "C"]            # index 1
    ["r","t"]               # index 2
    ["s"]                   # index 3
]
```
At LOOP 8:
```python
2D array rows
[
    ["F",       "l"]        # index 0
    ["i",   "C"]            # index 1
    ["r","t"]               # index 2
    ["s"]                   # index 3
]
index   = 1
step    = 1
char    = o"
rows[1].append("o")
If index == 0 => FALSE
ELSE if index(=1) == numRows - 1(4-1=3) => FALSE
value of step no change, keep 1.
index += step = 1 + 1 = 2
2D array rows
[
    ["F",       "l"]        # index 0
    ["i",   "C","o"]        # index 1
    ["r","t"]               # index 2
    ["s"]                   # index 3
]
```
At LOOP 9:
```python
2D array rows
[
    ["F",       "l"]        # index 0
    ["i",   "C","o"]        # index 1
    ["r","t"]               # index 2
    ["s"]                   # index 3
]
index   = 2
step    = 1
char    = u"
rows[2].append("u")
If index == 0 => FALSE
ELSE if index(=2) == numRows - 1(4-1=3) => FALSE
value of step no change, keep 1.
index += step = 2 + 1 = 3
2D array rows
[
    ["F",       "l"]        # index 0
    ["i",   "C","o"]        # index 1
    ["r","t",   "u"]        # index 2
    ["s"]                   # index 3
]
```
At LOOP 10:
```python
2D array rows
[
    ["F",       "l"]        # index 0
    ["i",   "C","o"]        # index 1
    ["r","t",   "u"]        # index 2
    ["s"]                   # index 3
]
index   = 3
step    = 1
char    = "d"
rows[3].append("d")
If index == 0 => FALSE
ELSE if index(=3) == numRows - 1(4-1=3) => TRUE
    step = -1
index += step = 3 + -1 = 2
2D array rows
[
    ["F",       "l"]        # index 0
    ["i",   "C","o"]        # index 1
    ["r","t",   "u"]        # index 2
    ["s",       "d"]        # index 3
]
```
At LOOP 11:
```python
2D array rows
[
    ["F",       "l"]        # index 0
    ["i",   "C","o"]        # index 1
    ["r","t",   "u"]        # index 2
    ["s",       "d"]        # index 3
]
index   = 2
step    = -1
char    = "J"
rows[2].append("J")
If index == 0 => FALSE
ELSE if index(=2) == numRows - 1(4-1=3) => FALSE
value of step no change, keep -1.
index += step = 2 + -1 = 1
2D array rows
[
    ["F",       "l"]        # index 0
    ["i",   "C","o"]        # index 1
    ["r","t",   "u","J"]    # index 2
    ["s",       "d"]        # index 3
]
```
At LOOP 12:
```python
2D array rows
[
    ["F",       "l"]        # index 0
    ["i",   "C","o"]        # index 1
    ["r","t",   "u","J"]    # index 2
    ["s",       "d"]        # index 3
]
index   = 1
step    = -1
char    = "o"
rows[1].append("o")
If index == 0 => FALSE
ELSE if index(=1) == numRows - 1(4-1=3) => FALSE
value of step no change, keep -1.
index += step = 1 + -1 = 0
2D array rows
[
    ["F",       "l"]                # index 0
    ["i",   "C","o",    "o"]        # index 1
    ["r","t",   "u","J"]            # index 2
    ["s",       "d"]                # index 3
]
```
At LOOP 13:
```python
2D array rows
[
    ["F",       "l"]                # index 0
    ["i",   "C","o",    "o"]        # index 1
    ["r","t",   "u","J"]            # index 2
    ["s",       "d"]                # index 3
]
index   = 0
step    = -1
char    = "u"
rows[0].append("u")
If index == 0 => TRUE
    step = 1
index += step = 0 + 1 = 1
2D array rows
[
    ["F",       "l",        "u"]    # index 0
    ["i",   "C","o",    "o"]        # index 1
    ["r","t",   "u","J"]            # index 2
    ["s",       "d"]                # index 3
]
```
At LOOP 14:
```python
2D array rows
[
    ["F",       "l",        "u"]    # index 0
    ["i",   "C","o",    "o"]        # index 1
    ["r","t",   "u","J"]            # index 2
    ["s",       "d"]                # index 3
]
index   = 1
step    = 1
char    = "r"
rows[1].append("r")
If index == 0 => FALSE
ELSE if index(=1) == numRows - 1(4-1=3) => FALSE
value of step no change, keep 1.
index += step = 1 + 1 = 2
2D array rows
[
    ["F",       "l",        "u"]    # index 0
    ["i",   "C","o",    "o","r"]    # index 1
    ["r","t",   "u","J"]            # index 2
    ["s",       "d"]                # index 3
]
```
At LOOP 15:
```python
2D array rows
[
    ["F",       "l",        "u"]    # index 0
    ["i",   "C","o",    "o","r"]    # index 1
    ["r","t",   "u","J"]            # index 2
    ["s",       "d"]                # index 3
]
index   = 2
step    = 1
char    = "n"
rows[2].append("n")
If index == 0 => FALSE
ELSE if index(=2) == numRows - 1(4-1=3) => FALSE
value of step no change, keep 1.
index += step = 2 + 1 = 3
2D array rows
[
    ["F",       "l",        "u"]    # index 0
    ["i",   "C","o",    "o","r"]    # index 1
    ["r","t",   "u","J",    "n"]    # index 2
    ["s",       "d"]                # index 3
]
```
At LOOP 16:
```python
2D array rows
[
    ["F",       "l",        "u"]    # index 0
    ["i",   "C","o",    "o","r"]    # index 1
    ["r","t",   "u","J",    "n"]    # index 2
    ["s",       "d"]                # index 3
]
index   = 3
step    = 1
char    = "e"
rows[3].append("e")
If index == 0 => FALSE
ELSE if index(=3) == numRows - 1(4-1=3) => TRUE
    step = -1
index += step = 3 + -1 = 2
2D array rows
[
    ["F",       "l",        "u"]    # index 0
    ["i",   "C","o",    "o","r"]    # index 1
    ["r","t",   "u","J",    "n"]    # index 2
    ["s",       "d",        "e"]    # index 3
]
```
At LOOP 17 (END):
```python
2D array rows
[
    ["F",       "l",        "u"]    # index 0
    ["i",   "C","o",    "o","r"]    # index 1
    ["r","t",   "u","J",    "n"]    # index 2
    ["s",       "d",        "e"]    # index 3
]
index   = 2
step    = -1
char    = "y"
rows[2].append("y")
If index == 0 => FALSE
ELSE if index(=2) == numRows - 1(4-1=3) => FALSE
value of step no change, keep -1.
index += step = 2 + -1 = 1
2D array rows
[
    ["F",       "l",        "u"]        # index 0
    ["i",   "C","o",    "o","r"]        # index 1
    ["r","t",   "u","J",    "n","y"]    # index 2
    ["s",       "d",        "e"]        # index 3
]
```

#### Now, we will perform join the result of each row.
At LOOP 1:
```python
2D array rows
[
    ["Flu"]                             # index 0
    ["i",   "C","o",    "o","r"]        # index 1
    ["r","t",   "u","J",    "n","y"]    # index 2
    ["s",       "d",        "e"]        # index 3
]
```
At LOOP 2:
```python
2D array rows
[
    ["Flu"]                             # index 0
    ["iCoor"]                           # index 1
    ["r","t",   "u","J",    "n","y"]    # index 2
    ["s",       "d",        "e"]        # index 3
]
```
At LOOP 3:
```python
2D array rows
[
    ["Flu"]                             # index 0
    ["iCoor"]                           # index 1
    ["rtuJny"]                          # index 2
    ["s",       "d",        "e"]        # index 3
]
```
At LOOP 4:
```python
2D array rows
[
    ["Flu"]                             # index 0
    ["iCoor"]                           # index 1
    ["rtuJny"]                          # index 2
    ["sde"]                             # index 3
]
```

#### After join characters of each rows, we will join the result of all rows into a string. That is our expected resulted.
```python
return "FluiCoorrtuJnysde"
```

## Full code [here](./ZigzagConversion.py)