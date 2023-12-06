### Description
#### URL: https://leetcode.com/problems/add-two-numbers/
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
```
Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
```
```
Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]
```
```
Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
```
Constraints:

+ The number of nodes in each linked list is in the range [1, 100].
+ ```0 <= Node.val <= 9```
+ It is guaranteed that the list represents a number that does not have leading zeros.

### Idea
```
# Run a loop a get value of each element in l1 and l2. if is None return 0, else return it's value.
                l1_value = l1.val if l1 else 0
                l2_value = l2.val if l2 else 0
```
```
# Calculate 'total'.
                total = l1_value + l2_value + carry
```

```
# Input remainder of dividing 'total' with 10 into a ListNode. This will be a part of our result.
                current.next = ListNode(total % 10)
```
```
# Calculate 'carry'. It is quotient of dividing 'total' with 10.
                carry = total // 10
```

```
# Get value for next round
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            current = current.next
```

### Full code [here](../AddTwoNumber/AddTwoNumber.py)
