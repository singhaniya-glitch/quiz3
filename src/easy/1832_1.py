#!/usr/bin/env python3
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence)==0:
            return False
        return len(set(sentence)) == 26


# Goal: We need to check if all the letters from a-z have occured atleast once or not in a given sentence

# ### Approach:

# - If the string is empty, it's definitely not a pangram
# - We don't care if any letter between a-z occurs more than once.
# - So we get only the single occurances of each character in the string by converting it into a set which is an ordered sequence of unique elements.
# - Now, we need to check if all the elements between a-z are there. In other words, if our resulting set has all  the 26 letters of English alphabet
# - So we just check if it's length is 26.

# Time Complexity: O(n)

# - set(str) would be O(k) where k is the length of the string k . Reference: https://stackoverflow.com/questions/34642155/what-is-time-complexity-of-a-list-to-set-conversion/34642209
# - len() has O(1) in python.  Reference: https://stackoverflow.com/questions/1115313/cost-of-len-function