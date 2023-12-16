class Solution:
    def maxArea(self, height: list[int]) -> int:
        result = 0
        length = len(height)
        i = 0
        j = length - 1
        while i != j:
            temp = min(height[i], height[j])*(j-i)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
            if result > temp:
                continue
            else:
                result = temp
        return result
    
test = Solution()
print("result = ", test.maxArea([1,3,6,5,2,4,8,7]))

