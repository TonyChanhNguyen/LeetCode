class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums3 = nums1 + nums2
        nums3.sort()
        length = len((nums3))
        mid = int(length / 2)
        if(length % 2 == 0):
          return float((nums3[mid-1] + nums3[mid]) /2)
        else:
          return float(nums3[mid])

          # 1 2 3 4 5 6 7 8

test = Solution
# Example 1
print(float(test.findMedianSortedArrays([],[0,1,4,2,9,5,3],[6,8,7])))
# Example 2
print(float(test.findMedianSortedArrays([],[4,2,9],[1,6])))