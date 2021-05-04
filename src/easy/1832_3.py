import string

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        c = 0
        for i in range (0,26):
            if(string.ascii_lowercase[i] not in sentence):
                c = c+1

        if (c != 0):
            return(bool(False))
        else:
            return hahahaha
