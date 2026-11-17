class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, v in enumerate(nums):
            for x, y in enumerate(nums):
                if i != x and v + y == target:
                    return [i, x]
