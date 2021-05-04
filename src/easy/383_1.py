#!/usr/bin/env python3
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if not ransomNote or not magazine:
            return False
        ransomNote_letters = Counter(ransomNote)
        magazine_letters = Counter(magazine)
        for letter,count in ransomNote_letters.items():
            if count > magazine_letters[letter]:
                return False
        return True

## Intuition:
#
# - The ransomNote can only be constructed if all the letters in the ransomNote are present in the magazine
# - In other words, the ransomNote is not possible to have been constructed from a magazine if the count of any letter in the ransomNote is greater than the count of that particular letter in the magazine.
# (i.e. if the magazine does not have that letter or the magazine does not have enough occurances of that letter)
# - Thus we use a Counter object to create a hashmap of the number of letters and their corresponding frequency for both the ransomNote and magazine strings.
# - Now, for each letter in the ransomNote counter object we check if it's corresponding count is less than the count of that letter in the maganize counter object 
# - When the condition is satisfied, we know that the ransomNote cannot be constructed from the magazine and return False without having the need to check for the remaining of the letters.
# - Otherwise, return True if the condition is never satisfied implying the ransomNote was indeed constructed from the given magazine.
#
# Time Complexity
# 
# - O(r+m+r)
# - Iterating through all r elements in the string ransomNote to form the corresponding Counter object takes O(r)
# - Followed by iterating through all m the string magazine to form the corresponding Counter object takes O(m)
# - Finally to check if count of a letter in ransomNote counter object is equal to that in the magazine count object takes O(r)
#
## Space Complexity

# - O(r+m) or O(n)
# - If the strings on converting to their corresponding counter objects are stored in different variables
# - As, counter object of ransomNote string takes O(r) space
# - and counter object of magazine string takes takes O(m) space
# - 
# - O(1)
# - If the strings on converting to their corresponding counter objects are stored in the same variables
