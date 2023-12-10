## Description
#### URL: [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)

Given two sorted arrays ``nums1`` and ``nums2`` of size ``m`` and ``n`` respectively, return the median of the two sorted arrays.

The overall run time complexity should be ``O(log (m+n))``.

#### Example 1:
```
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
```
#### Example 2:
```
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
```

#### Constraints:

+ nums1.length == m
+ nums2.length == n
+ 0 <= m <= 1000
+ 0 <= n <= 1000
+ 1 <= m + n <= 2000
+ -106 <= nums1[i], nums2[i] <= 106

## Idea

#### Merge to list
```
nums3 = nums1 + nums2
```

#### Sort list from small to large
```
nums3.sort()
```

#### Calculate length of merged list
```
length = len((nums3))
```

#### Identify the index of middle of merged list
```
mid = int(length / 2)
```
#### Check if length is even number. Calculate the median by summary value at middle index and index - 1 of merged list divide by 2.
```
if(length % 2 == 0):
    return float((nums3[mid-1] + nums3[mid]) /2)
```
#### Else length is odd number. The median will be value of middle index of merged list.
```
else:
    return float(nums3[mid])
```

## Example 1
nums1 = [1,4,2,9,5,3] nums2 = [6,8,7,0]. Expected Median = 4.5

```
nums3 = nums1 + nums2 = [1,4,2,9,5,3,6,8,7,0]
nums3.sort() = [0,1,2,3,4,5,6,7,8,9]
length = 10
mid = 5
Since length = 10 is Even number:
    Median =  (nums3[5-1] + nums3[5])/2 = (4 + 5)/2 = 4.5
```

## Example 2
nums1 = [4,2,9] nums2 = [1,6]. Expected Median = 4.0

```
nums3 = nums1 + nums2 = [4,2,9,1,6]
nums3.sort() = [1,2,4,6,9]
length = 5
mid = 2
Since length = 5 is Odd number:
    Median =  nums3[2] = 4.0
```

## Full code [here](./MedianofTwoSortedArrays.py)

