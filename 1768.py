#1768. Merge Strings Alternately

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        len1 = len(word1)
        len2 = len(word2)

        i1 = 0
        i2 = 0

        output = ''

        while i1 < len1 or i2 < len2:
            if i1 < len1:
                output += word1[i1]
                i1 += 1
            if i2 < len2:
                output += word2[i2]
                i2 += 1

        return output
        
        return output
