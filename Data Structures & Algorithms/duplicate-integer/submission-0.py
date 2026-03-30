class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = set(nums)
        if len(nums) > len(a):
            return True
        return False
