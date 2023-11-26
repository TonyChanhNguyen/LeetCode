# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def addTwoNumbers( l1, l2):
    len_max = max(len(l1), len(l2))
    sum = 0
    buffer = 0
    result = []
    for index in range(len_max):
        if (index ) == len(l1):
            value_l1 = 0
        else:    
            value_l1 = l1[index]
        if (index ) == len(l2):
            value_l2 = 0
        else:    
            value_l2 = l2[index]
        sum = (value_l1 + value_l2 + buffer) % 10
        buffer = (value_l1 + value_l2) // 10
        result.append(sum)
    return  result

addTwoNumbers([1,9,3,8,7],[3,3,3,3])

#   1    9   3   8   7
#   3    3   3   3   
#   4    2   7   1   8