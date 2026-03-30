from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def backtrack(start: int):
            # Add the current subset (copy) to the result
            result.append(subset.copy())

            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtrack(i + 1)
                subset.pop()

        backtrack(0)
        return result
