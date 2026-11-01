class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0
        j = x

        while i <= j:
            mid = (i + j) // 2
            square = mid * mid

            if square == x:
                return mid
            elif square > x:
                j = mid - 1
            else:
                i = mid + 1

        return j