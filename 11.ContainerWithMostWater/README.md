## Description
#### URL: [Container With Most Water](https://leetcode.com/problems/container-with-most-water)
You are given an integer array ``height`` of length ``n``. There are ``n`` vertical lines drawn such that the two endpoints of the i<sup>th</sup> line are ``(i, 0)`` and ``(i, height[i])``.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

*Return the maximum amount of water a container can store*.

**Notice** that you may not slant the container.

#### Example 1:
![Example 1](./images/question_11.jpg)
```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
```

#### Example 2:
```
Input: height = [1,1]
Output: 1
```

#### Constraints:
+ ```n == height.length```
+ ```2 <= n <= 105```
+ ```0 <= height[i] <= 104```

## Idea
#### Initialize the variables
+ i: to represent the left pointer, starting at the beginning of the container (index 0).
+ j: to represent the right pointer, starting at the end of the container (index len(height) - 1).
+ result: to keep track of the maximum area found, initially set to 0.
```python
result = 0
length = len(height)
i = 0
j = length - 1
```

#### Set a loop to check when i is not j.
```python
 while i != j:
```

#### Calculate the temporary maximum amount of water a container can store. 
```python
temp = min(height[i], height[j])*(j-i)
```

#### Set condition to compare height of index ``i`` or ``j`` is larger than. If height of index ``i`` larger than ``j``, move ``j`` to left. Else, move ``i`` to right. 
```python
if height[i] < height[j]:
    i += 1
else:
    j -= 1
```

#### Set a condition to find the maximum of ``result`` and ``temp``.
```python
if result > temp:
    continue
else:
    result = temp
```

#### After the loop, return ``result``.
```python
return result
```

## Example
We have ``height = [1,3,6,5,2,4,8,7]``, length ``len(height) = 8`` and expected ``result = 30``.

At loop 1
```python
i           = 0
j           = 8 - 1 = 7
result      = 0
while i != j: => True
    temp        = min(height[0], height[7])*(7-0) = min(1,7)*7 = 7
    if height[0] < height[7]: => True
        i = i + 1 = 1
    if result > temp: => False
    else:             => True
        result = temp = 7
```
At loop 2
```python
i           = 1
j           = 7
result      = 7
while i != j: => True
    temp        = min(height[1], height[7])*(7-1) = min(3,7)*6 = 18
    if height[1] < height[7]: => True
        i = i + 1 = 2
    if result > temp: => False
    else:             => True
        result = temp = 18
```
At loop 3
```python
i           = 2
j           = 7
result      = 18
while i != j: => True
    temp        = min(height[2], height[7])*(7-2) = min(6,7)*5 = 30
    if height[2] < height[7]: => True
        i = i + 1 = 3
    if result > temp: => False
    else:             => True
        result = temp = 30
```
At loop 4
```python
i           = 3
j           = 7
result      = 30
while i != j: => True
    temp        = min(height[3], height[7])*(7-3) = min(5,7)*4 = 20
    if height[3] < height[7]: => True
        i = i + 1 = 4
    if result > temp: => True
```
At loop 5
```python
i           = 4
j           = 7
result      = 30
while i != j: => True
    temp        = min(height[4], height[7])*(7-4) = min(2,7)*3 = 6
    if height[4] < height[7]: => True
        i = i + 1 = 5
    if result > temp: => True
        continue
```
At loop 6
```python
i           = 5
j           = 7
result      = 30
while i != j: => True
    temp        = min(height[5], height[7])*(7-5) = min(4,7)*2 = 8
    if height[5] < height[7]: => True
        i = i + 1 = 6
    if result > temp: => True
        continue
```
At loop 7
```python
i           = 6
j           = 7
result      = 30
while i != j: => True
    temp        = min(height[6], height[7])*(7-6) = min(8,7)*2 = 14
    if height[6] < height[7]: => True
        i = i + 1 = 7
    if result > temp: => True
        continue
```
At loop 8 (END)
```python
i           = 7
j           = 7
result      = 30
while i != j: => False
```