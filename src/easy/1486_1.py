#!/usr/bin/env python3
from functools import reduce
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [start+2*i for i in range(n)]
        return reduce(lambda x,y:x^y,nums)

## Time Complexity:
#
# O(2*n) ~= O(n)
# - First we need to iterate through n elements to form our array/list
# - Second we need to iterate through all those elements again for calculating the XOR (the reduce function)
#
## Space Complexity:
#
# O(n)
# - Memory assigned depends upon the size of the list/array n 