class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n_arr = len(nums)
        n_set = len(set(nums))
        if n_arr != n_set:
            return True
        else:
            return False

        