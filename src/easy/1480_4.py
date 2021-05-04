class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return nums
        else:
            for i in range(1,len(nums)): 
                nums[i]+=nums[i-1]
            return nums



## Time Complexity:
#
# - O(n)
# - Iterating through all n elements of the list sum takes O(n)
#
## Space Complexity:
#
# - O(1)
# - Due to inplace computation, the memory allocated in independent on the size of the input list