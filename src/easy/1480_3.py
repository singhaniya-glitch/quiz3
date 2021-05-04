class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return nums
        else:
            s = 0
            return [(s:= s+num) for num in nums]