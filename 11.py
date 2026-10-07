# 11. Container With Most Water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        max_vol = 0
        left, right = 0, len(height) - 1
        while True:
            vol = min(height[left], height[right]) * (right - left)
            if vol > max_vol:
                max_vol = vol
            if left + 1 == right:
                break
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return max_vol