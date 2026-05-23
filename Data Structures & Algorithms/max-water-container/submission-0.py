class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, (len(heights) - 1)
        max_vol = 0
        while left < right:
            curr_vol = (right - left) * min(heights[left], heights[right])
            max_vol = max(curr_vol, max_vol)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return max_vol
