#!/usr/bin/env python3
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = start
        for i in range(1,n):
            res^=start+2*i
        return res


## Intuition:
#
# - As per the requirements of the problem, we don't need to return the array itself.
# - So, we can free up any space that would have been otherwise allocated to the array 
# - And instead work with the elements of the array generated each iteration 
# without storing them in a temporary location
# 
## Time Complexity:
#
# O(n)
# - We need to iterate through n elements to get our result
#
## Space Complexity:
#
# O(1)
# - Memory assigned does not depends upon the size of the list/array n, rather the value of the res variable      