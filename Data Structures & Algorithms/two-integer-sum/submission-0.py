class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pre_map = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in pre_map:
                return [pre_map[diff], i]
            else:
                pre_map[num] = i