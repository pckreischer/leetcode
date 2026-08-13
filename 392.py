# 392. Is Subsequence

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if len(s) == 0:
            return True
        j = 0
        for i in range(len(t)):
            if t[i] == s[j]:    # character match
                if j == len(s) - 1:  # we've found all the letters of the substring
                    return True
                else:   # keep iterating through substring
                    j += 1
        return False
            
