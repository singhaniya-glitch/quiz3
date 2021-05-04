class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return nums
        else:
            sum = 0
            running_sum = []
            for x in nums:
                sum += x
                running_sum.append(sum)
            return running_sum