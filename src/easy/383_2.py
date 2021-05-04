#!/usr/binv/env python3
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if not ransomNote or not magazine:
            return False
        m_list = list(magazine)
        r_list = list(ransomNote)
        for letter in r_list:
            if letter not in m_list or r_list.count(letter)>m_list.count(letter):
                return False
        return True

## Intuition
#
# - Convert the magazine and ransomNote strings into corresponding list
# - Iterate the ransomNote list
# - For each element of the the ransomNote list check if the count of it in the ransomNote list is greater than it's count in the magazine list
# - When the condition is satisfied, we know that the ransomNote cannot be constructed from the magazine and return False without having the need to check for the remaining of the letters.
# - Otherwise, return True if the condition is never satisfied implying the ransomNote was indeed constructed from the given magazine.
#
## Time Complexity
# 
# - O(r*(m+r)) or O(n**2)
# - Iterating through the list of r ransomNote elements takes O(r)
# - For each element, it's count in r_list takes O(r) to compute and that in m_list takes O(m) to compute
#
## Space Complexity
#
# - O(r+m) or O(n)
# - If the strings on converting to their corresponding lists are stored in different variables
# - As, r_list takes O(r) space
# - and m_list takes O(m) space
# - 
# - O(1)
# - If the strings on converting to their corresponding lists are stored in the same variables
