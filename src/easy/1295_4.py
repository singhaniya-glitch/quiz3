#!/usr/bin/env python3
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        return sum([1 for x in nums if len(str(x))%2 ==0])