class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        def water(l, r):
            return min(heights[l], heights[r]) * (r - l)
        


        for i in range(len(heights) // 2 + 1):
            if water(left, right) < water(left, right - 1):
                right -= 1

            if water(left, right) < water(left + 1, right):
                left += 1
        
        return water(left, right)