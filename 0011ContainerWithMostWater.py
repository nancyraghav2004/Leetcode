from typing import List
# My Solution
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_area = 0
        for i in range(left, right):
            width = right - left
            heights = min(height[left], height[right])
            area = width * heights
            max_area = max(max_area, area)
            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1
        return (max_area)

# Good Solution
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        max_area=0
        while left<right:
            width=right-left
            current_height=min(height[left],height[right])
            current_area=width*current_height
            max_area=max(max_area,current_area)

            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max_area