class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        check = {}

        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in check:
                return [check[diff], i + 1]

            check[numbers[i]] = i + 1

        return []