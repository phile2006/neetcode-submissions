class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = height[0]
        max_right = height[len(height) - 1]
        left = 0
        right = len(height) - 1
        volume = []
        
        while left <= right:

            if max_left < max_right:
                vol = min(max_left, max_right) - height[left]
                volume.append(vol if vol > 0 else 0)

                if height[left] > max_left:
                    max_left = height[left]

                left += 1
            else:
                vol = min(max_left, max_right) - height[right]
                volume.append(vol if vol > 0 else 0)

                if height[right] > max_right:
                    max_right = height[right]

                right -= 1
        return sum(volume)

