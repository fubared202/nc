class Solution:
    def trap(self, height: List[int]) -> int:
        total_vol = 0
        left = 0
        right = len(height) - 1

        # Use two pointers, and move the pointer whose height is less.
        while left < right:
            if height[left] < height[right]:
                i = left + 1
                unusable = 0
                
                while i < right and height[i] < height[left]:
                    # The height of the bars itself is unusable, even if the 
                    # bar is not a boundary.                    
                    unusable += height[i]
                    i += 1

                # We reached a bounding wall. Calculate the volume
                # storable from left to i, and add it to the total.
                total_vol += (((i - left - 1) * min(height[i], height[left])) - unusable)
                left = i
            else:
                i = right - 1
                unusable = 0

                while i > left and height[i] < height[right]:
                    # The height of the bars itself is unusable, even if the 
                    # bar is not a boundary.
                    unusable += height[i]
                    i -= 1

                # We reached a bounding wall. Calculate volume
                # storable from i to right, and add it to the total.
                total_vol += (((right - i - 1) * min(height[i], height[right])) - unusable)
                right = i

        return total_vol
                

