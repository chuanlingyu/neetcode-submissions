class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0

        left = 0
        right = len(heights) - 1

        while left < right:
            left_height = heights[left]
            right_height = heights[right]

            area = max(area, (right - left) * min(left_height, right_height))

            if left_height > right_height:
                right -= 1

            else:
                left += 1

        return area