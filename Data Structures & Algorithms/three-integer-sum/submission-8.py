class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        track = []

        for i in range(len(nums)):
            cur_val = nums[i]
            if cur_val > 0:
                break

            if i > 0 and cur_val == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                left_val = nums[left]
                right_val = nums[right]

                sum = left_val + right_val + cur_val

                if sum == 0:
                    track.append([cur_val, left_val, right_val])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif sum < 0:
                    left += 1

                else:
                    right -= 1

        return track