#!/usr/bin/env python3
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not g or not s:
            return 0
        g.sort()
        s.sort()
        n_content_children = 0
        cookie_p = len(s) - 1
        child_p = len(g) - 1
        while cookie_p>=0 and child_p>=0:
            if s[cookie_p] >= g[child_p]:
                cookie_p -= 1
                child_p -= 1
                n_content_children += 1
            else:
                child_p -= 1
        
        return n_content_children
        

## Intuition:
#
# We have i children each of greed g[i] and j cookies of size s[j]
# Giving any child more than 1 cookie is not allowed
# Take the largest cookie and try to give it to the child with the highest greed
# If that child is content, take the second largest cookie and try to give it to the child with the next highest greed
# If the child is not content, try to give the same cookie to child with the next highest greed
# Repeat this till either there are no children left to try giving a cookie or no cookies left