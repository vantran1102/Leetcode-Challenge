class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left,right = 0,len(height)-1
        while left < right:
            area = (right-left)*min(height[left],height[right])
            if height[left] <= height[right]:
                left+=1
            elif height[left] > height[right]:
                right-=1
            max_area = max(max_area,area)
        return max_area