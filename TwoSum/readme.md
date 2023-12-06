### Description
#### URL: https://leetcode.com/problems/two-sum/
Given an array of integers 'nums' and an integer 'target', return indices of the two numbers such that they add up to 'target'.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
```
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```
```
Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

```
```
Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
```

Constraints:

+ ``2 <= nums.length <= 104``
+ ``-109 <= nums[i] <= 109``
+ ``-109 <= target <= 109``
+ Only one valid answer exists.

### Idea
```
# Run 2 loops to get each element in 'nums'
        for x in range(len(nums)):
            for y in range(len(nums)):
            # Set a condition to avoid the same element twice
                if(x == y): 
                    continue
                else:
                    # Find the result when sum of two element of 'mums' equal to 'target'
                    if(nums[x] + nums[y] == target):
                        # Return the index of two element that match requirement.
                        return [x,y]
                    # If there is no result valid, continue the loop to check two another element
                    else:
                        continue
        # At the and of loop, if there is no result valid it will be return 'null'
        return []

```

### Full code [here](../TwoSum/TwoSum.py)