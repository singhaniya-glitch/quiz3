#!/usr/bin/env python3
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        even_d_count = 0
        for i in nums:
            d_count = 0
            while i>0:
                i=i//10
                d_count +=1
            if d_count%2 == 0:
                even_d_count+=1
        return even_d_count