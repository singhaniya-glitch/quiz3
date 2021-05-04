import itertools
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return nums
        else:
            return itertools.accumulate(nums)