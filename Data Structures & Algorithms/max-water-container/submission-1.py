class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        res = 0

        while left < right:
            left_height = heights[left]
            right_height = heights[right]

            sum = min(left_height, right_height) * (right - left)
            res = max(sum, res)

            if left_height < right_height:
                left += 1

            else:
                right -= 1

        return res